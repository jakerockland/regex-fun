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

# returns number of times the word occurs in the input string
def count_word(word, string):
    return  len(re.findall(r'\b{}\b'.format(word), string))

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

# finds number of occurences of a substring in the given text
def num_substrings(text, substring):
    # - substring must be preceded and succeeded by letters or numerics or an underscore
    return len(re.findall(r'\B{}\B'.format(substring), text))


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

    def test_check_username(self):
        self.assertTrue(check_username('_0898989811abced_'))
        self.assertFalse(check_username('_abce'))
        self.assertFalse(check_username('_09090909abcD0'))

    def test_split_number(self):
        self.assertEquals(split_number('91-011-23413627'), ('91', '011', '23413627'))
        self.assertEquals(split_number('1 877 2638277'), ('1', '877', '2638277'))
        self.assertEquals(split_number('891-454-9195497623'), ('891', '454', '9195497623'))

    def test_num_substrings(self):
        self.assertEquals(num_substrings('existing pessimist optimist this is', 'is'), 3)
        self.assertEquals(num_substrings('existing pessimist optimist this is', 'ti'), 2)
        self.assertEquals(num_substrings('existing pessimist optimist this is', 'st'), 1)
        self.assertEquals(num_substrings('existing pessimist optimist this is', 'ex'), 0)


if __name__ == '__main__':
    unittest.main()
