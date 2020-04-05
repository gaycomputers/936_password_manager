from nltk.corpus import words
import hashlib

#change this to produce more or less words
password_word_count = 4
md5 = hashlib.md5()
word_list = words.words()
word_list_len = len(word_list)

# ask user for needed seed and salt
print("Please enter the landing page for the site/service the password will be used for (I.E: https://google.com, ssh://google.com): ")
landing_seed = input()
print("Please enter a rememberable shared secret seed with traditional complexity: ")
shared_salt = input()

shared_binary = ''.join(format(ord(i), 'b') for i in shared_salt)
shared_int = int(shared_binary, 2)

#salt the snail
md5.update(shared_int.to_bytes((shared_int.bit_length() + 7) // 8, 'big'))

landing_binary = ''.join(format(ord(i), 'b') for i in landing_seed)
landing_int = int(landing_binary, 2)
landing_length = int(len(landing_binary)/password_word_count)
landing_binaries_list = []
landing_ints_list = []
password = []

#split the binary seed into enough pieces for the words we need
for i in range(0, password_word_count):
    landing_binaries_list.append(landing_binary[i * landing_length : (i+1) * landing_length])

#make the binary big enough to possibly return any word in the dictionary, and concat to a integer list
for i, binstring in enumerate(landing_binaries_list):
    integer_form = int(str(binstring), 2)
    if integer_form < word_list_len:
        while integer_form < word_list_len:
            integer_form = integer_form**2
        landing_ints_list.append(integer_form)
    else:
        landing_ints_list.append(integer_form)

#take the binaries and md5 them, using the previous chunk as salt, then grab index of our dictionary for resulting chunks binaries (when represented as ints)
for i in landing_ints_list:
    md5.update(i.to_bytes((i.bit_length() + 7) // 8, 'big'))
    password.append(word_list[int.from_bytes(md5.digest(), 'big') % word_list_len])

print(password)