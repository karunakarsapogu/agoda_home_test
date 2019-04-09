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
    lowerCaseCount = 0
    for x in psd:
        if x.islower() == True:
            lowerCaseCount += 1
    return True if lowerCaseCount >= 1 else False


def verify_atleast_one_upper(psd):
    upperCaseCount = 0
    for x in psd:
        if x.isupper() == True:
            upperCaseCount += 1
    return True if upperCaseCount >= 1 else False


def verify_atleast_one_digit(psd):
    digitCount = 0
    for x in psd:
        if x.isdigit() == True:
            digitCount += 1
    return True if digitCount >= 1 else False


def verify_valid_special_char(psd):
    return True if re.match("^[a-zA-Z0-9!@#$&*]*$", psd) else False


def verify_atleast_one_specia_char(psd):
    specialCharCount = 0
    special_chars = '!@#$&*'
    if verify_valid_special_char(psd) == True:
        for x in psd:
            if x in special_chars:
                specialCharCount += 1
    return True if specialCharCount >= 1 and specialCharCount <=4 else False


def duplicate_counter(psd):
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
    return SequenceMatcher(None, oldPsd, newp).ratio()*100


def match_old_password(old_psd, new_psd):
    if similar_percentage(old_psd, new_psd) >= 80.00:
        return False
    return True
        

def digit_limit_check_in_pswd(psd):
    sumOfDigit = sum(c.isdigit() for c in psd)
    totalPermittedLenOfStringWithDigit = len(psd)/2
    if sumOfDigit > totalPermittedLenOfStringWithDigit:
        return False
    return True


def changePassword(oldp, psd):
    if verify_minimum_18_char_len(psd) == False:
        print 'invalid new password/nEnter valid password with 18-20 chars and password shouldnt be empty\ncannot reset password'
        print 'False'
        return False
    if verify_atleast_one_lower(psd) == False:
        print 'atleast one lower case alphabet is expected\ncannot reset password'
        print 'False'
        return False
    if verify_atleast_one_upper(psd) == False:
        print 'atleast one upper case alphabet is expected\ncannot reset password'
        print 'False'
        return False
    if verify_atleast_one_digit(psd) == False:
        print 'atleast one digit is expected\ncannot reset password'
        print 'False'
        return False
    if verify_atleast_one_specia_char(psd) == False:
        print 'atleast one special char is expected and only from ! @ # $  & *\ncannot reset password'
        print 'False'
        return False
    if duplicate_counter(psd) == False:
        print 'please dont repeat single char more than 4 tines\ncannot reset password'
        print 'False'
        return False
    if match_old_password(oldp, psd) == False:
        print 'password shouldnt match old password upto 80%\ncannot reset password'
        print 'False'
        return False
    if digit_limit_check_in_pswd(psd) == False:
        print 'new password shouldnt contain more than 50% digits\ncannot reset password'
        print 'False'
        return False
    print 'True\ncan reset password'
    return True

