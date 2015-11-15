# Implementation of various functions to practice using regular expressions in Python
# By: Jacob Rockland

import re
import unittest

# returns true if the input string contains the word 'hello'
def contains_hello(string):
    return True if re.search(r'hello', string) else False

# extracts a list of emails from an input string
def extract_emails(string):
    return re.findall(r'[\w.-]+@[\w.-]+', string)

# finds number of occurences of a substring in the given text
def count_substring(substring, text):
    # - substring must be preceded and succeeded by letters or numerics or an underscore
    return len(re.findall(r'\B{}\B'.format(substring), text))

# returns number of times the word occurs in the input text
def count_word(word, text):
    return  len(re.findall(r'\b{}\b'.format(word), text))

# returns true if input username is valid, false otherwise
def check_username(username):
    # valid username must meet the following:
    # - begin with either an underscore '_' or a dot '.'
    # - be immediately followed by one or more occurrences of digits numbered 0-9
    # - it can then have letters, both uppercase or lowercase, 0 or more in number
    # - it can then end with an optional '_'
    return True if re.match(r'^[\._][0-9]+[a-zA-Z]*_?$', username) else False

# splits a phone number into its country code, area code, and phone number
def split_number(number):
    # - phone number is in the format [Country code]-[Local Area Code]-[Number]
    # - the country and local area codes can have 1-3 numerals each
    # - the number section can have 4-10 numerals each
    # - will either be a '-', or a ' ' between the segments
    split_number = re.search(r'([0-9]{1,3})[\- ]([0-9]{1,3})[\- ]([0-9]{4,10})', number)
    return split_number.group(1), split_number.group(2), split_number.group(3)

# tests if an ip address meets IPv4 standards, IPv6 standards, or neither
def ip_validation(string):
    # - format of an IPv4 address is A.B.C.D where A, B, C and D are integers lying between 0 and 255
    # - the 128 bits of an IPv6 address are represented in 8 groups of 16 bits each
    # - each group is written as 4 hexadecimal digits and the groups are separated by colons (:)
    IPv4_range = r'([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])'
    IPv6_range = r'([0-9a-fA-F]{1,4})'
    if re.search(r'^{0}\.{0}\.{0}\.{0}$'.format(IPv4_range), string):
        return 'IPv4'
    elif re.search(r'^{0}:{0}:{0}:{0}:{0}:{0}:{0}:{0}$'.format(IPv6_range), string):
        return 'IPv6'
    else:
        return None


# test methods for regex functions
class TestRegexFun(unittest.TestCase):

    def test_contains_hello(self):
        self.assertTrue(contains_hello("thisisahelloworldstring"))
        self.assertTrue(contains_hello("hellohellohello"))
        self.assertFalse(contains_hello("thisstringisnot"))

    def test_extract_emails(self):
        self.assertEquals(extract_emails('purple alice@google.com, blah monkey bob@abc.com blah dishwasher'), ['alice@google.com', 'bob@abc.com'])
        self.assertEquals(extract_emails('purple alicegoogle.com, blah monkey babc.com blah dishwasher'), [])

    def test_count_word(self):
        self.assertEquals(count_word("foo", "foo bar (foo) bar foo-bar foo_bar foo'bar bar-foo bar, foo."), 6)
        self.assertEquals(count_word("bar", "foo bar (foo) bar foo-bar foo_bar foo'bar bar-foo bar, foo."), 6)

    def test_count_substring(self):
        self.assertEquals(count_substring('is', 'existing pessimist optimist this is'), 3)
        self.assertEquals(count_substring('ti', 'existing pessimist optimist this is'), 2)
        self.assertEquals(count_substring('st', 'existing pessimist optimist this is'), 1)
        self.assertEquals(count_substring('ex', 'existing pessimist optimist this is'), 0)

    def test_check_username(self):
        self.assertTrue(check_username('_0898989811abced_'))
        self.assertFalse(check_username('_abce'))
        self.assertFalse(check_username('_09090909abcD0'))

    def test_split_number(self):
        self.assertEquals(split_number('91-011-23413627'), ('91', '011', '23413627'))
        self.assertEquals(split_number('1 877 2638277'), ('1', '877', '2638277'))
        self.assertEquals(split_number('891-454-9195497623'), ('891', '454', '9195497623'))

    def test_ip_validation(self):
        self.assertEquals(ip_validation('This line has junk text.'), None)
        self.assertEquals(ip_validation('35'), None)
        self.assertEquals(ip_validation('1051:1000:4000:abcd:5:600:300c:326b'), 'IPv6')
        self.assertEquals(ip_validation('1050:1000:2000:ab00:5:600:300c:326a'), 'IPv6')
        self.assertEquals(ip_validation('22.231.113.164'), 'IPv4')
        self.assertEquals(ip_validation('222.231.113.64'), 'IPv4')


if __name__ == '__main__':
    unittest.main()
