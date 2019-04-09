import unittest
from change_password import changePassword
import time

class ChangePasswordTest(unittest.TestCase):
    
    
    def test_change_password_with_minimum_18_chars_in_new_password_positive_case(self):
        '''
            Test case to test whether user is able to set password when user tries with 18 chars
        '''
        self.cpswd = changePassword
        self.assertTrue(self.cpswd('Q!1qwertyuiopasdfg', 'Q!1iwjwazfsoxlxmnb'))
        print 'TEST NAME: test_change_password_with_minimum_18_chars_in_new_password_positive_case \n \n'
        time.sleep(0.5)


    def test_change_password_less_than_18_chars_in_new_password_negative_case(self):
        '''
            Test case to test whether user shouldn't be allowed to set password when user tries with  less than 18 chars
        '''
        self.cpswd = changePassword
        self.assertFalse(self.cpswd('Q!1qwertyuiopasdfg', 'Q!1iwjwazfsb'))
        print 'TEST NAME: test_change_password_less_than_18_chars_in_new_password_negative_case \n \n'
        time.sleep(0.5)


    def test_change_password_with_minimum_one_upper_case_positive_case(self):
        '''
           Test case to verify if the user tries to set password with one or more than one upper case in char, user should be able to reset new password
        '''
        self.cpswd = changePassword
        self.assertTrue(self.cpswd('Q!1qwertyuiopasdfg', 'Q!1IWjwazfsoxlxmnb'))
        print 'TEST NAME: test_change_password_with_minimum_one_upper_case_positive_case \n \n'
        time.sleep(0.5)


    def test_change_password_without_any_upper_case_nagative_case(self):
        '''
            Test case to verify if the user tries to set password with no upper case in char, user shouldn't be able to reset new password
        '''
        self.cpswd = changePassword
        self.assertFalse(self.cpswd('Q!1qwertyuiopasdfg', 'q!1iwjwazfsoxlxmnb'))
        print 'TEST NAME: test_change_password_without_any_upper_case_nagative_case \n \n'
        time.sleep(0.5)


    def test_change_password_with_minimum_one_lower_case_positive_case(self):
        '''
            Test case to verify if the user tries to set password with one or more than one lower case in char, user should be able to reset new password
        '''
        self.cpswd = changePassword
        self.assertTrue(self.cpswd('Q!1qwertyuiopasdfg', 'Q!1iWJWAZFSOXLXMNb'))
        print 'TEST NAME: test_change_password_with_minimum_one_lower_case_positive_case \n \n'
        time.sleep(0.5)


    def test_change_password_without_any_lower_case_nagative_case(self):
        '''
            Test case to verify if the user tries to set password with no lower case in char, user shouldn't be able to reset new password
        '''
        self.cpswd = changePassword
        self.assertTrue(self.cpswd('Q!1qwertyuiopasdfg', 'Q!1iWJWAZFSOXLXMNB'))
        print 'TEST NAME: test_change_password_without_any_lower_case_nagative_case \n \n'
        time.sleep(0.5)


    def test_change_password_with_atleast_one_valid_special_char_positive_case(self):
        '''
            Test case to verify if the user tries to set password with one or more special char, user should be able to reset new password
        '''
        self.cpswd = changePassword
        self.assertTrue(self.cpswd('Q!1qwertyuiopasdfg', 'Q!$iwjwazfsoxlxmnb1'))
        print 'TEST NAME: test_change_password_with_atleast_one_valid_special_char_positive_case \n \n'
        time.sleep(0.5)


    def test_change_password_with_more_than_four_valid_special_char_negative_case(self):
        '''
            Test case to verify if the user tries to set password with  more than 4 special char, user shouldn't be able to reset new password
        '''
        self.cpswd = changePassword
        self.assertFalse(self.cpswd('Q!1qwertyuiopasdfg', 'Q!$&&@wazf!oxlxmnb1'))
        print 'TEST NAME: test_change_password_with_more_than_four_valid_special_char_negative_case \n \n'
        time.sleep(0.5)


    def test_change_password_with_no_special_char_negative_case(self):
        '''
            Test case to verify if the user tries to set password with no special char, user shouldn't be able to reset new password
        '''
        self.cpswd = changePassword
        self.assertFalse(self.cpswd('Q!1qwertyuiopasdfg', 'Q!()iwjwazfsoxlxmnb1'))
        print 'TEST NAME: test_change_password_with_no_special_char_negative_case \n \n'
        time.sleep(0.5)


    def test_change_password_with_invalid_special_char_negative_case(self):
        '''
            Test case to verify if the user tries to set password with invalid special char, user shouldn't be able to reset new password
        '''
        self.cpswd = changePassword
        self.assertFalse(self.cpswd('Q!1qwertyuiopasdfg', 'QLKJiwjwazfsoxlxmnb1'))
        print 'TEST NAME: test_change_password_with_invalid_special_char_negative_case \n \n'
        time.sleep(0.5)


    def test_change_password_with_4_or_more_repeatitive_char_negative_case(self):
        '''
            Test case to verify if the user tries to set password with 4 or more repeatitive char, user shouldn't be able to reset new password
        '''
        self.cpswd = changePassword
        self.assertFalse(self.cpswd('Q!1qwertyuiopasdfg', 'QLKJiwjwazfsoxlxmnb1'))
        print 'TEST NAME: test_change_password_with_4_or_more_repeatitive_char_negative_case \n \n'
        time.sleep(0.5)
    

    def test_change_password_with_atleast_one_digit_positive_case(self):
        '''
            Test case to verify if the user tries to set password with one or more digits user should be able to reset new password
        '''
        self.cpswd = changePassword
        self.assertTrue(self.cpswd('Q!1qwertyuiopasdfg', 'Q!$i12wazfsoxlxmnb99'))
        print 'TEST NAME: test_change_password_with_atleast_one_digit_positive_case \n \n'
        time.sleep(0.5)


    def test_change_password_with_more_than_50_percent_digits_negative_case(self):
        '''
            Test case to verify if the user tries to set password with more than 50% of digits, user shouldn't be able to reset new password
        '''
        self.cpswd = changePassword
        self.assertFalse(self.cpswd('Q!1qwertyuiopasdfg', 'Q!$i560891234514nb99'))
        print 'TEST NAME: test_change_password_with_more_than_50_percent_digits_negative_case \n \n'
        time.sleep(0.5)


    def test_change_password_with_no_digits_negative_case(self):
        '''
            Test case to verify if the user tries to set password with no digits, user shouldn't be able to reset new password
        '''
        self.cpswd = changePassword
        self.assertFalse(self.cpswd('Q!1qwertyuiopasdfg', 'Q!$iwjwazfsoxlxmnbxx'))
        print 'TEST NAME: test_change_password_with_no_digits_negative_case \n \n'
        time.sleep(0.5)


    def test_change_password_with_no_new_password_negative_case(self):
        '''
            Test case to verify if the user tries to set password with no new password, user shouldn't be able to reset new password
        '''
        self.cpswd = changePassword
        self.assertFalse(self.cpswd('Q!1qwertyuiopasdfg', ''))
        print 'TEST NAME: test_change_password_with_no_new_password_negative_case \n \n'
        time.sleep(0.5)


if __name__ == '__main__':
    unittest.main()
