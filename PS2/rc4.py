#implementation of RC4

#The key is a string of bytes,
#which can be up to 128 bits
#long.  The state is a list
#of 256 bytes with integer values.

import conversions
def rc4_initialize(key):
    s = range(256)
    j = 0
    for i in range(256):
        j = (j + s[i] + ord(key[i % len(key)])) % 256
        (s[i], s[j])= (s[j], s[i])
    return s
    
#Given the initial state, update the generator
#of the state and emit the next byte. Do ths
#numbytes times in succession.  The output is a string
#of numbytes bytes
def rc4_genbytes(state, numbytes):
    output =''
    i = j = 0
    for k in range(numbytes):
        i = (i+1) % 256
        j = (j+state[i]) % 256
        (state[i], state[j])= (state[j], state[i])
        output+=chr(state[(state[i]+state[j])%256])
    return output

#Encrypt or decrypt a string of bytes with a given key.
def rc4(key,text):
    initstate=rc4_initialize(key)
    keystream=rc4_genbytes(initstate,len(text))
    return conversions.xor(keystream,text)

def test():
    key='Here is a random key that you cannot possibly guess.'
    plaintext="Once upon a time you dressed so fine, threw the bums a dime in you r prime, didn't you?"
    return rc4(key,plaintext)
