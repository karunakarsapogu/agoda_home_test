import re
from difflib import SequenceMatcher


def verify_minimum_18_char_len(psd):
    '''
        added password length limitation to 20 chars
        reason lengthy passwords takes time to type and login, to help users to perform there booking faster
        and easier to remember
    '''
    if len(psd) >= 18 and len(psd) <=20:
        return True
    return False


def verify_atleast_one_lower(psd):
    '''
        method to verify atleast one lower case alphabet in new password
    '''
    lowerCaseCount = 0
    for x in psd:
        if x.islower() == True:
            lowerCaseCount += 1
    return True if lowerCaseCount >= 1 else False


def verify_atleast_one_upper(psd):
    '''
        method to verify atleast one upper case alphabet in new password
    '''
    upperCaseCount = 0
    for x in psd:
        if x.isupper() == True:
            upperCaseCount += 1
    return True if upperCaseCount >= 1 else False


def verify_atleast_one_digit(psd):
    '''
        method to verify atleast one digit in alphabet in new password
    '''
    digitCount = 0
    for x in psd:
        if x.isdigit() == True:
            digitCount += 1
    return True if digitCount >= 1 else False


def verify_valid_special_char(psd):
    '''
        method to find out if there are any invalid special char in new password
    '''
    return True if re.match("^[a-zA-Z0-9!@#$&*]*$", psd) else False


def verify_atleast_one_specia_char(psd):
    '''
        method to verify atleast one valid special char is present in new password
    '''
    specialCharCount = 0
    special_chars = '!@#$&*'
    if verify_valid_special_char(psd) == True:
        for x in psd:
            if x in special_chars:
                specialCharCount += 1
    return True if specialCharCount >= 1 and specialCharCount <=4 else False


def duplicate_counter(psd):
    '''
        method to count duplicates in a new password
    '''
    unique_keys = set(psd)
    count_char_repition = {}
    for x in unique_keys:
        count_char_repition[x] = psd.count(x)
    for y in count_char_repition.values():
        if y > 4:
            return False
        else:
            pass
    return True


def similar_percentage(oldPsd, newp):
    '''
        method to find out the ratio of the old and new password comparrison ratio
    '''
    return SequenceMatcher(None, oldPsd, newp).ratio()*100


def match_old_password(old_psd, new_psd):
    '''
        method to verify old password doesnt match with new password with 80% or more
    '''
    if similar_percentage(old_psd, new_psd) >= 80.00:
        return False
    return True
        

def digit_limit_check_in_pswd(psd):
    '''
        method to verify password doesnt contains 50% or more digits in a new password
    '''
    sumOfDigit = sum(c.isdigit() for c in psd)
    totalPermittedLenOfStringWithDigit = len(psd)/2
    if sumOfDigit > totalPermittedLenOfStringWithDigit:
        return False
    return True


def changePassword(oldp, psd):
    '''
        function to test the new password validity to allow the user to change password or not
    '''
    if verify_minimum_18_char_len(psd) == False:
        print 'invalid new password \n Enter valid password with 18-20 chars and password shouldnt be empty \n cannot reset password'
        return False
    if verify_atleast_one_lower(psd) == False:
        print 'atleast one lower case alphabet is expected \n cannot reset password'
        return False
    if verify_atleast_one_upper(psd) == False:
        print 'atleast one upper case alphabet is expected \n cannot reset password'
        return False
    if verify_atleast_one_digit(psd) == False:
        print 'atleast one digit is expected \n cannot reset password'
        return False
    if verify_atleast_one_specia_char(psd) == False:
        print 'atleast one special char is expected and only from ! @ # $  & * \n cannot reset password'
        return False
    if duplicate_counter(psd) == False:
        print 'please dont repeat single char more than 4 tines \n cannot reset password'
        return False
    if match_old_password(oldp, psd) == False:
        print 'password shouldnt match old password upto 80% \n cannot reset password'
        return False
    if digit_limit_check_in_pswd(psd) == False:
        print 'new password shouldnt contain more than 50% digits \n cannot reset password'
        return False
    print 'can reset password'
    return True

