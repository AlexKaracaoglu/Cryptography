#Caesar shift cipher.  In the homework you will work
#with a binary version, in which the shift is a single
#byte (=one ASCII character) rather than a letter.

#sample plaintexts. The second contains no occurrence of the letter e.

#convert upper-case ASCII letter to number (A-0...Z-25)


import string

def aton(c):
    return ord(c)-ord('A')

#convert number back to letter
def ntoa(n):
    return chr(n+ord('A'))

#convert a string to upper-case (skip all non-letters, and
#convert lower-case letters to upper-case)
def convert(s):
    t=''
    for c in s:
        if c in string.letters:
            t+=c.upper()
    return t


#Caesar-encrypt plaintext s with shift letter k. Note
#that any plaintext string will be accepted, but only
#letters in the plaintext will be encrypted.

def caesar_encrypt(s,k):
    shiftval=aton(k)
    ptext=convert(s)
    ctext=''
    for c in ptext:
        ctext+=ntoa((aton(c)+shiftval)%26)
    return ctext

#Decryption is the same as encryption, where we subtract rather
#than add.  The original plaintext is not restored, only the
#letters, and these will all appear in upper-case.

def caesar_decrypt(s,k):
    shiftval=aton(k)
    ctext=s
    ptext=''
    for c in ctext:
        ptext+=ntoa((aton(c)-shiftval)%26)
    return ptext

#Exhaustive search attack against a single ciphertext:  Print
#all 26 decryptions and find the right answer by visual inspection.

def brute_force(s):
    for k in string.uppercase:
        print k+':'+caesar_decrypt(s,k)+'\s'


#Let's try this stuff out, first to make sure encryption and decryption
#are working correctly, and then to test the statistical cryptanalysis.

def demo():
    print 'The two plaintexts:\n\n'
    ptext1= 'Fourscore and seven years ago, our fathers'\
          ' brought forth on this continent a new nation,'\
          ' conceived in liberty, and dedicated to the '\
          'proposition that all men are created equal.'
    print ptext1+'\n\n'
    ptext2='I am writing to you today to discuss a difficult '\
            'affair that, if known, risks provoking a most '\
            'damaging crisis.'
    print ptext2+'\n\n'
    print 'The second plaintext is special, designed to foil the statistical method!\n'
    print 'Encryptions of the two plaintexts with keys P and Y, respectively:\n\n'
    ctext1= caesar_encrypt(ptext1,'P')
    print ctext1
    print '\n\n'
    ctext2= caesar_encrypt(ptext2,'Y')
    print ctext2
    print '\n\n'
    print 'And, just for a sanity check, their decryptions:\n\n'
    print caesar_decrypt(ctext1,'P')
    print '\n\n'
    print caesar_decrypt(ctext2,'Y')
    print "\n\nNow let's brute-force attack the second ciphertext, trying out all keys.\n\n"
    brute_force(ctext2)

#Here we try decryption by statistical analysis.  We first give an 'Englishness' score to
#a candidate plaintext, by summing over all letters L, f_1(L)*f_2(L), where f_1(L) is the relative
#frequency of L in the text, and f_2(L) is the expected frequency. The argument s is assumed
#to contain only upper-case letters.



def english_score(s):
    #frequencies of letters in English text.
    freq=[0.0817, 0.0153, 0.0224, 0.0470, 0.121, 0.0217,\
          0.0210, 0.0606, 0.0724, 0.0010, 0.0090, 0.0379,\
          0.0315, 0.0684, 0.0773, 0.0170, 0.0009, 0.0575,\
          0.0605, 0.0885, 0.0283, 0.0092, 0.0260, 0.0013,\
          0.0226, 0.0002]
    #tabulate frequencies in the candidate text s
    table=[0]*26
    for c in s:
        table[aton(c)]+=1
    for j in range(26):
        table[j]=1.0*table[j]/len(s)
    return sum([freq[j]*table[j] for j in range(26)])

#Now we have our improved attack.  It is still brute-force, but does not require
#visual inspection of the candidate plaintexts to select the most likely one.

#This also prints out the actual score associated with each key:  the printing was
#initially put in for debugging purposes, but I found that it is useful for the demo.

def brute_force2(s):
    maxscore=0

    for k in string.uppercase:
        newscore=english_score(caesar_decrypt(s,k))
        print k,newscore
        if newscore>maxscore:
            maxscore=newscore
            maxkey=k
    return caesar_decrypt(s,maxkey)

#The new demo replaces visual inspection of all the candidate plaintexts
#by this statistical analysis.

def demo2():
    print 'The two plaintexts:\n\n'
    ptext1= 'Fourscore and seven years ago, our fathers'\
          ' brought forth on this continent a new nation,'\
          ' conceived in liberty, and dedicated to the '\
          'proposition that all men are created equal.'
    print ptext1+'\n\n'
    ptext2='I am writing to you today to discuss a difficult '\
            'affair that, if known, risks provoking a most '\
            'damaging crisis.'
    print ptext2+'\n\n'
    print 'The second plaintext is special, designed to foil the statistical method!\n'
    print 'Encryptions of the two plaintexts with keys P and Y, respectively:\n\n'
    ctext1= caesar_encrypt(ptext1,'P')
    print ctext1
    print '\n\n'
    ctext2= caesar_encrypt(ptext2,'Y')
    print ctext2
    print '\n\n'
    print 'And, just for a sanity check, their decryptions:\n\n'
    print caesar_decrypt(ctext1,'P')
    print '\n\n'
    print caesar_decrypt(ctext2,'Y')
    print "\n\nNow let's brute-force attack the first ciphertext, using statistical analysis to select the plaintext.\\n"
    print brute_force2(ctext1)
    print "\n\nRepeat with the second ciphertext.\n\n"
    print brute_force2(ctext2)

def demo3():
    ctext=raw_input('Enter ciphertext, all in upper-case letters.')
    print '\n\n'
    print 'Exhaustive search prints all possible plaintexts:\n\n'
    brute_force(ctext)
    raw_input('Hit return to continue')
    print '\n\n'
    print 'Exhaustive search coupled with statistical analysis'
    print 'automatically selects correct ciphertext.  The values'
    print 'displayed are the "Englishiness" scores for the different'
    print 'possible shifts.\n\n'
    print brute_force2(ctext)
