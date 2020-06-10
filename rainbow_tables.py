# Load the NIST list of 10,000 most commonly used passwords
with open('nist_10000.txt', newline='') as bad_passwords:
    nist_bad = bad_passwords.read().split('\n')
print(nist_bad[1:10])
# The following data is a normalized simplified user table
# Imagine this information was stolen or leaked
leaked_users_table = {
    'jamie': {
        'username': 'jamie',
        'role': 'subscriber',
        'md5': '203ad5ffa1d7c650ad681fdff3965cd2'
    },
    'amanda': {
        'username': 'amanda',
        'role': 'administrator',
        'md5': '315eb115d98fcbad39ffc5edebd669c9'
    },
    'chiaki': {
        'username': 'chiaki',
        'role': 'subscriber',
        'md5': '941c76b34f8687e46af0d94c167d1403'
    },
    'viraj': {
        'username': 'viraj',
        'role': 'employee',
        'md5': '319f4d26e3c536b5dd871bb2c52e3178'
    },
}
# import the hashlib
import hashlib
# example hash
word = 'blueberry'
hashlib.md5(word.encode()).hexdigest()
"""
Your Task!¶
Use the information above and hashlib to:
Create a python dictionary for each word in the nist_bad list. For each word, the dictionary should use the hashlib.md5 string as a key, and the word as the value.
Iterate over each user in the leaked_users_table dictionary and attempt to use the rainbow table to crack their password.
"""
rainbow_table = {}
for word in nist_bad:
    hashed_word = hashlib.md5(word.encode()).hexdigest()
    rainbow_table[hashed_word] = word

# Use the Rainbow table to determine the plain text password
for user in leaked_users_table.keys():
    try:
        print(user + ":\t" + rainbow_table[leaked_users_table[user]['md5']])
    except KeyError:
        print(user + ":\t" + '******* hash not found in rainbow table')
"""
bcrypt,scrypt(one way hashing)are normally used. MD5.SHA-1 are breakable
output
jamie:	hello1
amanda:	qweasdzxc
chiaki:	******* hash not found in rainbow table
viraj:	PASSWORD

In this concept we briefly mention Salt Rounds. 
This is a cost factor for how many times a password and 
salt should be re-hashed. In other words if you choose 10 salt
 rounds, the calculation is performed 2^10 or 1024 times. 
 Each attempt takes the hash from the previous round as an input. 
 The more rounds performed, the more computation is required to 
 compute the hash. This will not cause significant time for a 
 single attempt (i.e. checking a password at login), 
but will introduce significant time when attempting to 
brute force or generate rainbow tables.
What is the primary reason to salt passwords?
to add complexity to make it more time complex to generate hash tables
"""