import unittest
from BloomFilter import BloomFilter


class TestBloomFilter(unittest.TestCase):

    def test_bloom(self):
        bloom = BloomFilter(32)
        str1 = "0123456789"
        str2 = "1234567890"
        str3 = "2345678901"
        str4 = "3456789012"
        str5 = "4567890123"
        str6 = "5678901234"
        str7 = "6789012345"
        str8 = "7890123456"
        str9 = "8901234567"
        str10 = "9012345678"

        bloom.add(str1)

        self.assertEqual(bloom.is_value(str1), True)
        self.assertEqual(bloom.is_value(str2), False)
        self.assertEqual(bloom.is_value(str3), True)
        self.assertEqual(bloom.is_value(str4), False)
        self.assertEqual(bloom.is_value(str5), True)
        self.assertEqual(bloom.is_value(str6), False)
        self.assertEqual(bloom.is_value(str7), True)
        bloom.add(str2)
        self.assertEqual(bloom.is_value(str2), True)
        self.assertEqual(bloom.is_value("heasdad;riyqwepiruq[et"), False)


