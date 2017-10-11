import conversions
import string
from timeit import default_timer as timer

# NAME: ALEX KARACAOGLU

# Code for number 2 (Some pieces may be used later on as well)
# The cipher text was given in hex, I will convert them to ascii and use them

ciphertext1_in_b64 = "EjctKjswcH5+GjF+JzErfik/MCp+KjF+NTAxKX4/fi07PSw7KmF+fhoxficxK34uLDEzNy07fjAxKn4qMX4qOzIyYX5+HTIxLTsscH5+EjsqfjM7fik2Ny0uOyx+NzB+JzErLH47Pyxw"
ciphertext1_in_as = conversions.b64_to_as(ciphertext1_in_b64)

ciphertext2_in_b64 = "mvS+86C886e6oba387y186e7uqDzp7ykvfOku7ahtvO2pbahqvOnvL20prbzuqDzpLK0tLq9tPOku7a987altqGq87GysLjzuqDzp6ahvba3/fPzh7u2qvShtvOntr+/ur2086C2sKG2p6Dzp7uyp/Ogu7ymv7fzvbaltqHzsbbzobaltrK/trf9"
ciphertext2_in_as = conversions.b64_to_as(ciphertext2_in_b64)

# individual_xor: function that takes in a cipher character and the key and returns the xor result
def individual_xor(ct,k):
   plain = conversions.xor(ct,k*len(ct))
   return plain

# brute: Takes in a string and returns a list of all 256 possible decryptions
def brute(text):
    for key in range(256):
        print str(chr(key)) + ":" +individual_xor(text,chr(key))

# count_printable: takes in a string and returns the number of printable characters
def count_printable(text):
    count=0
    for i in range(len(text)):
        if text[i] in string.printable:
            count = count + 1
        else:
            count = count
    return count

# count_letters: takes in a string and returns the number of letters
def count_letters(text):
    count = 0
    for i in range(len(text)):
        if text[i] in string.ascii_letters:
            count = count + 1
        else:
            count = count
    return count

# add: Takes in an array and returns a float that is the value after adding all the entries together
def add(a):
   b = 0.0
   for i in range(len(a)):
      b = b + a[i]
   return b  

#Final_counts: takes in an array and returns a smaller array, used as a helper function in counts
def finalCounts(dist):
   final = [0] * 26
   for i in range(len(final)):
      final[i] = dist[i]+dist[i+26]
   return final

#counts: Takes in a string and returns an array of the distribution of the letters
def counts(text):
   a = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
   dist = [0] * 52
   for i in range(len(text)):
      b = text[i]
      for j in range(len(dist)):
         if b == a[j]:
            dist[j] = dist[j]+1
         else:
            dist[j] = dist[j]
   return dist

#englishy: takes in a text and returns a negative value corresponding to how "englishy" the input text is. (Closer to 0.0 is more "englishy")
def englishy(text):
   a = finalCounts(counts(text))
   length = float(len(text))
   b = [(x / length) for x in a]
   freq =[0.0817, 0.0153, 0.0224, 0.0470, 0.121, 0.0217, 0.0210, 0.0606, 0.0724, 0.0010, 0.0090, 0.0379, 0.0315, 0.0684, 0.0773, 0.0170, 0.0009, 0.0575, 0.0605, 0.0885, 0.0283, 0.0092, 0.0260, 0.0013, 0.0226, 0.0002]
   score = [0] *26
   for i in range(26):
      score[i] = -(abs(b[i]-freq[i]))
   c = add(score)
   return c * 5

# all_scores: Takes in a string and prints out a series of keys and their resulting scores
def all_scores(text):
   for i in range(256):
        rating = (1 * count_printable(individual_xor(text,chr(i)))) +(.75 * count_letters(individual_xor(text,chr(i))))+ (englishy(individual_xor(text,chr(i))))
        print str(i) + ":" + str(rating)

def best_score(text):
    max_score = 0
    max_score_character = ''
    rating = 0
    for i in range(256):
         rating = (1 * count_printable(individual_xor(text,chr(i)))) +(.75 * count_letters(individual_xor(text,chr(i))))+ (englishy(individual_xor(text,chr(i))))
                                                                                                                         
         if rating >= max_score:
            max_score = rating
            max_score_character = chr(i)
    return str(max_score)

# best_key: Takes in a string and prints out the best key and the best score when ran through the scoring alcgorithm I created. (Larger score is better)
def best_key(text):
   max_score = 0
   max_score_character = ''
   rating = 0
   for i in range(256):
        rating = (1 * count_printable(individual_xor(text,chr(i)))) +(.75 * count_letters(individual_xor(text,chr(i))))+ (englishy(individual_xor(text,chr(i))))
        if rating >= max_score:
           max_score = rating
           max_score_character = chr(i)
   return str(max_score_character)
   
# one_byte_xor: Takes in a ciphertext, in form of an ascii string, and returns the decrypted message
def one_byte_xor(ciphertext):
   key = best_key(ciphertext)
   plaintext = individual_xor(ciphertext,key)
   return plaintext

# Code for number 3 (Some pieces may be used later on as well)

# mod: takes in two integers and retrns the first mod the second
def mod(a,b):
    return a % b

# new_xor: Takes in string and a key and returns the xor of the text using the given key
def new_xor(text,key):
    plain = conversions.xor(text,key)
    return plain

# remove: Takes in a string and removes all non printable items and replaces them with ''
def remove(text):
    s = ''
    for i in range(len(text)):
        if text[i] not in string.printable:
            s = s + ""
        else:
            s = s + text[i]
    return s


# recover: Takes in a word file and returns the cipher text that is taken from the body of the document
def recover(filename):
    f = open(filename,'rb')
    s = f.read()
    a = s[540]
    b = s[541]
    c = ord(a)
    d = ord(b)
    final = (d*256)+c+512
    cipher = s[2560:final]
    return cipher

# repeating_byte_xor: Takes in a string and a key and modifies the key to be repeating and of the same length as the text, then performs an xor
def repeating_byte_xor(text,key):
   a = len(text)
   b = len(key)
   c = (a/b)
   d = mod(a,b)
   new_key = (key*c) + key[:d]
   f = conversions.xor(text,new_key)
   return f

# decrypt_msword: Takes in a word file, opens the file, reads the file and extracts the body (ciphertext) then decrypts it using the repating key xor
# The key was given to us, so I will convert it to ascii and use it: hex("b624bd2ab42a39a235a0b4a9b6a734cd")
key_for_number_3_in_hex = "b624bd2ab42a39a235a0b4a9b6a734cd"
key_for_number_3_in_as = conversions.hex_to_as(key_for_number_3_in_hex)
def decrypt_msword(filename, key):
    ciphertext = recover(filename)
    plaintext = repeating_byte_xor(ciphertext, key)
    finaltext = remove(plaintext)
    final = finaltext.replace('\r',"")
    return final

# Code for Number 4

# timeSingleDecrypt: Returns how long it takes the computer to perform one decryption of key length 16 on 'MSWord1.doc'
def timeSingleDecrypt():
   start = timer()
   decrypt_msword('MSWordXOR1.doc',key_for_number_3_in_as)
   end = timer()
   return(end - start)

def timemanydecrypts():
   total = 0.0
   for i in range(10000):
      total = total + timeSingleDecrypt()
   final = float(total / (10000))
   return final

# getTotalTime: Returns the number of YEARS it would take to do all (256**16) decrptions (Brute force method) 
def getTotalTime():
   a = timemanydecrypts()
   numberKeys = 256 ** 16
   totalSeconds = float(a * numberKeys)
   secondsInYear = 31536000
   transfer = long (totalSeconds / secondsInYear)
   return str(transfer) 

# Code for number 6

# extract_subtexts: Takes in a string and a key length, and builds a list of subtexts as discussed in class
def extract_subtexts(ciphertext,keylength):
    subtexts=['']*keylength
    for j in range(len(ciphertext)):
        subtexts[j%keylength]+=ciphertext[j]
    return subtexts

# make_key: Takes in the subtexts and contructs the best possible key using my scoring system
def make_key(extracted_subtexts):
    s = ''
    for i in range(16):
        s = s + best_key(extracted_subtexts[i])
    return s

# ct_only_msword: Takes in a file and then returns the plain text decryption to the best of its ability
def ct_only_msword(filename):
    ciphertext = recover(filename)
    subtexts = extract_subtexts(ciphertext, 16)
    key = make_key(subtexts)
    plaintext = repeating_byte_xor(ciphertext, key)
    final = remove(plaintext)
    plain = final.strip('\n')
    plain2 = plain.strip('\r')
    plain3 = plain2.replace('\r','')
    plain4 = plain3.replace('\x0b','')
    plain5 = plain4.replace('\n','')
    return plain5






   





