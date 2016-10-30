#!/usr/bin/env python
from passwords import CreateUser
#Author: Tyler Bellerose
#Course: CIS166AF
#Assignment: P5 Password Class
#Last Changed: 2 April 2016

'''Tester module for passwords.py CreateUser class and modules.'''

good_user = CreateUser('user1','Aa1@De#5a$')
bad_user_min = CreateUser('user2', 'Aa!2')
bad_user_max = CreateUser('user3', 'Aa#3AdAd$5AA3aH67&86^dD')
bad_user_forbid = CreateUser('user4', '1@dAA3R(')
bad_user_missing1 = CreateUser('user5', 'AA@@22SS@@')
bad_user_missing2 = CreateUser('user6', 'aa@@22aa@@')
bad_user_missing3 = CreateUser('user7', 'aaAA@@aaAA@@')
bad_user_missing4 = CreateUser('user8', 'aaAA22aaAA22')
bad_user_user = CreateUser('user9', '1984user9@A2')
bad_user_multiple = CreateUser('user10', 'a*')

print
print('This should return true')
print(good_user.passcheck())
print
print('This should return false with an error for min length.')
print(bad_user_min.passcheck())
print
print('This should return false with an error for max length.')
print(bad_user_max.passcheck())
print
print('This should return false with an error for forbidden characters.')
print(bad_user_forbid.passcheck())
print
print('This should return false with an error for missing characters.')
print(bad_user_missing1.passcheck())
print
print('This should return false with an error for missing characters.')
print(bad_user_missing2.passcheck())
print
print('This should return false with an error for missing characters.')
print(bad_user_missing3.passcheck())
print
print('This should return false with an error for missing characters.')
print(bad_user_missing4.passcheck())
print
print('This should return false with an error for username in password.')
print(bad_user_user.passcheck())
print
print('This should return false with multiple error messages.')
print(bad_user_multiple.passcheck())
print
print('Here is a random password.')
print(CreateUser.passgen(20))
print
print('Here we create a new user with a randomly generated password.')
good_user_2 = CreateUser('user11', CreateUser.passgen(20))
print('Username: {0}, Password: {1}'.format(*good_user_2.info.values()))
