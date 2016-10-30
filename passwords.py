#!/usr/bin/env python
import re
from random import choice, randint
from string import ascii_lowercase, ascii_uppercase
from getpass import getpass
#Author: Tyler Bellerose
#Course: CIS166AF
#Assignment: P5 Password Class
#Last Changed: 4 April 2016

class CreateUser(object):
    '''Create a new user.

    Args:
        username (str): User's name.
        password (str): User's password.
        minlength (optional[int]): Minimum length for password. Default = 8
        maxlength (optional[int]): Maximum length for password. Default = 20

    Attributes:
        info (dict of str:str): 'username':username, 'password':password
        minlength (int): Minimum length for password.
        maxlength (int): Maximum length for password.
        main_pattern (str): Pattern for regex['main'].
        regex (dict of str:re):
            'main': main_pattern(For exclusion of forbidden characters.)
            'sub': list of patterns.(For inclusion of needed characters.)
            'user': username(For inclusion of username)
        error_list (dict of str:str):
            'min': minimum length error string
            'max': maximum length error string
            'forbid': main regex fail error string
            'missing': sub regex fail error string
            'user': user regex fail error string

    '''


    def __init__(self, username, password, minlength = 8, maxlength = 20):
        self.info = {
                'username': username,
                'password': password
                }
        self.minlength = minlength
        self.maxlength = maxlength
        self.main_pattern = '^[a-zA-Z0-9!@#$%^&]{1,100}$'
        self.regex = {
                'main': re.compile(self.main_pattern),
                'sub': [re.compile(p) for p in ['[a-z]', '[A-Z]',
                    '[0-9]', '[!@#$%^&]']],
                'user': re.compile(username)
                }
        self.error_list = {
                'min': 'Password does not meet minimum length requirement.',
                'max': 'Password exceeds maximum length.',
                'forbid': 'Password contains forbidden characters.',
                'missing': 'Password must contain a lower case letter, upper' +
                ' case letter, number and special character(!@#$%^&).',
                'user': 'Password may not contain username.'
                }

    def passcheck(self):
        '''Check a password for acceptable length and characters.

        Checks a password for acceptable length, lower case letters, upper case
        letters, numbers, and special characters (!@#$%^&).

        Attributes:
            password (str): User's password after .strip()
            results (dict of str:bool): error_str:bool built by result of regex
                                       tests.
            sub_match (list): list of strings built by result of 'sub' regex
                              tests.

        Returns:
            True if:
                Password length is between minlength and maxlength +
                Password contains a lower case letter +
                Password contains an upper case letter +
                Password contains a special character (!@#$%^&)
            False if:
                Password does not meet critera for True return or
                Password contains special characters other than letters,
                numbers, or !@#$%^&.

        '''
        password = self.info['password'].strip() 
        results = {}
        sub_match = []

        #The logic in parts this series of if statements may seem a weird.
        #For the purpose of this section of if statements:
        #'True' means good, 'False' means bad.
        if len(self.info['password']) >= self.minlength:
            results['min'] = True
        else:
            results['min'] = False

        if len(self.info['password']) <= self.maxlength:
            results['max'] = True
        else:
            results['max'] = False

        if self.regex['main'].match(self.info['password']):
            results['forbid'] = True
        else:
            results['forbid'] = False

        #Search the passwords for each sub regex.
        #If any are not matched return False for all of them.
        for regex in self.regex['sub']:
            if regex.search(self.info['password']):
                sub_match.append('match')
            else:
                sub_match.append('no')
        if 'no' in sub_match:
            results['missing'] = False
        else:
            results['missing'] = True

        if self.regex['user'].search(self.info['password']):
            results['user'] = False
        else:
            results['user'] = True

        #If any values in results are False, feed the key for those values
        #to the self.error_list and print the corresponding message.
        if False in results.values():
            for key in results.keys():
                if results[key] == False:
                    print(self.error_list[key])
            return False
        else:
            return True
    
    @staticmethod
    def passgen(length):
        '''Generate a random password of specified length.

        Generate a random password containing lower case letters, upper case
        letters, numbers, and special characters(!@#$%^&) of the specified
        length.

        Args:
            length (int): The length of the password to be generated.

        Attributes:
            length (int): The length of the password to be generated.
            pool (list): A list of lists containing letters, numbers and
                        special characters.
            result (str): An empty string to be filled with random characters.

        Returns:
            result (str): A string of the specified length consisting of lower
                         case letters, upper case letters, numbers and special
                         characters.

        '''

        good_pass = False
        while not good_pass:
            length = length
            pool = [
                    [str(n) for n in range(0, 10)],
                    [l for l in ascii_lowercase],
                    [L for L in ascii_uppercase],
                    [c for c in '!@#$%^&']
                    ]
            result = ''

            i = 0
            while i < length:
                result += choice(pool[randint(0, len(pool) - 1)])
                i += 1
            #Create a generic user instance in order to use passcheck()
            generic_user = CreateUser('generic', result)
            if generic_user.passcheck():
                good_pass = True
            else:
                continue
        return result


if __name__ == '__main__':
    username = raw_input('Enter a username: ')
    done = False
    while not done:
        print('Would you like to generate a random password for this user?')
        option = raw_input('Answer "Yes" or "No": ')
        if option.lower() == 'yes':
            new_user = CreateUser(username, CreateUser.passgen(20))
            print('New user created.')
            print('Username: {0}. Password: {1}'.format(*new_user.info.values()))
            done = True
        elif option.lower() == 'no':
            good_pass = False
            while not good_pass:
                print
                print("""
                        Passwords must contain:
                        \tA lowercase letter.
                        \tAn uppercase letter.
                        \tA number.
                        \tA special character(!@#$%^&)
                        \t8-20 characters.
                        """)
                password = getpass('Please enter a password: ')
                new_user = CreateUser(username, password)
                if new_user.passcheck():
                    print('New user created.')
                    print('Username: {0}. Password: {1}'.format(
                        *new_user.info.values()))
                    good_pass = True
                else:
                    continue
            done = True
        else:
            print("I didn't understand. Let's try again.")
            continue
