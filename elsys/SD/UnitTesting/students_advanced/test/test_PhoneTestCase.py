from src.phone import Phone, PhoneNumber
import unittest


class PhoneTestCase(unittest.TestCase):

    def test_init_number(self):
        p = PhoneNumber()
        flag = p is not None and p.number is not None
        self.assertTrue(flag)

    def test_init_phone(self):
        ph = Phone()
        flag = ph is not None and ph.number is not None \
               and ph.vendor is not None \
               and ph.conn_provider is not None
        self.assertTrue(flag)
