import warnings
from unittest import TestCase

from deprecator.deprecator import deprecated


class Foo:

    @deprecated
    def deprecated_method(self):
        pass

    def not_deprecated_method(self):
        pass


class DeprecatorTest(TestCase):

    def setUp(self):
        self.foo = Foo

    def _assertWarns(self, warning, funct, isDeprecated):
        with warnings.catch_warnings(record=True) as warning_list:
            warnings.simplefilter('always')
            funct(self.foo)
            if isDeprecated:
                self.assertTrue(any(item.category == warning for item in warning_list))
            else:
                self.assertFalse(any(item.category == warning for item in warning_list))

    def test_call_deprecated_method(self):
        self._assertWarns(
            DeprecationWarning,
            self.foo.deprecated_method,
            True
        )

    def test_call_not_deprecated_method(self):
        self._assertWarns(
            DeprecationWarning,
            self.foo.not_deprecated_method,
            False
        )
