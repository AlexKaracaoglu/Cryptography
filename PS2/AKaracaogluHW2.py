## Alex Karacaoglu

import conversions
import rc4
import time
import string
import javarandom

## Variables to help test 
ct_b64 = "qj+QFfumYvjsQDOWWpeJL28JvwfVwwkPd3pEX2v4Cy258HILVldrzCAtEc/aYNivlsERzlbvIJe6QDAwezJkTz+ap1N7r+ya/VCpaS832ZZ3nafoJ1XdjkLx+XofH3Ujrk6W0l+C5rqyTSREEyduXzehYeyhT4HFK1oTLZA/sTet2j3qmI2s9MmfXozqoMAU8+A4X8ng1eauXDbhcjiEM7y8AtWw/JfMiFjaz1IhFOajkaDSmwvEvif4FHrrhoiCp2g37EH0EgmC3l4eS77I0vnGzzGHkF7JYmP3Ln7KmIY3S5aBXpIlyf0Nwee6xSERHzBfBbhHYBgPX+cybeyrQ6omCHWxOAW4XSPIUeqCGufpkugqjebWSf0GRFH1i39BQ9wcU4pdHIc0daKUkcTxV2rU2J3qc7Fk5Hem7ns7pTD6lTpJZ8tCz5PNxDRUpMEflTDuc54rf8Ul1Bkh3J3s9tgop9I2JJGx39+RfWwEjm+jTkKdVnAiTPqVSHDNz89LMRV3DJpwsaAtLZFw47G3kWyiFd3TvQSPf+HXrOArFm324iBnDyW+BBLCw2ED9MQy5A=="
ct_as = conversions.b64_to_as(ct_b64)
og_key_hex = "7f65a580cb"
key = conversions.hex_to_as(og_key_hex)
iv = ct_as[:3]
ct = ct_as[3:]
fullkey = iv + key
##

## 6a
# rc4_iv_decrypt: Takes in the given og key in as and the cipher in ascii,
# does the conversions concerning the iv and does an rc4 decryption and return the pt
def rc4_iv_decrypt(key,ciphertext):
    iv = ciphertext[:3]
    ct = ciphertext[3:]
    fullkey = iv + key
    plaintext = rc4.rc4(fullkey,ct)
    return plaintext

##6b

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

shiftpoint = 1486262621
start = shiftpoint - (9 * 86400) + 7200
end = start + 90000
textb64 = "jrIYekOf4A+y/JGcPbkWSMIFoEWs/RHSmvQnAR0FC/VZWR6h0ovaZ2zQqdg6WJKxa/dYS1HUL9k8UMnzSugqRkIQZuCD3H4NMc5iJgFtKjyPlSIwybKX3UfBr10YnQjj2Eowa8gDSLxp9MpmPAZFaKRdVMCmvDW8bMZQFVta+6A4L6E6OOD+A/sZ0PyXZR/E2asptx+Eg7OGPsTzT1NeDJCFq6wEsU6EA4MySmaVRUQ+4XT9DQRiFhbQL+9Nw94YbqJkt4TaHU6YBG+yiG8snKz1WzXFfsjgZm8kzae0HIkrC8Bi8rFybv0NjCp2S1Q9u5H8mEAstMo5zcKvF/KCxpnD5MSqB+pWTmLq/gyvKi2WowP4gDa+vbxKD7uruvOqiUKrh414CJ7ABOY3HfPreSDXK0jb71OqpgjZahfPM1+7Tg=="
textas = conversions.b64_to_as(textb64)

def find_key6(ct):
    text = ct[:20]
    max_score = 0
    max_score_key = ''
    rating = 0
    for i in range(start,end):
         rating = (1 * count_printable(rc4.rc4(str(i),text))) +(.75 * count_letters((rc4.rc4(str(i),text))))+ (englishy((rc4.rc4(str(i),text))))                                                                                                                   
         if rating >= max_score:
           max_score = rating
           max_score_key = str(i)
    return max_score_key

##key6b = '1485553999'

## 7

cipher7_b64 = "+TlPSjTjDtFLO8bItE0qLB8oK4Sy1YT1KEkrEitEGH+5gnL/TEePLjHyv2evx3LYivXLt8c9z0FtMj/ESl1/NrYXsoe/lb2QJJnAzLVlwyYgGIx9BLaUCqmT3JO5raBwxTNNN5uGzc+vqXIIp+fP/hIk8lWlUx6JCQ2sKQe56A9ZKurAB1hY/BcaO7umXwT6hJ2b0/kv+FCJHtaQX0yWEQ/IVsG/bqJe5U4zv0ZsYaZEBHAKpicQztFSM4XlgBwsWFdNGLsM29r4q73XYWmP7jHMf0jdkDgA/5gn3kcHKo7n16bffrP1y59dHMDrPVWm+5J6K6z2nTkwsYXE+xUuXONRE2oZ77yypw5uR8VzoOZvxOJKkXjaL0KY72SsMdqL65tsQG33QF94N/n+yBdnV4Ccg/6Hbzvg/3hX5UyrMIhARfSSpOQLzzjCQhwdN5sFSkZGs7s9NX9gWGw9zqGvc5JIgz7eHHpKZsgEl89QuMCw3c+ZYTYKJzB3xUf79W6HeSyc66DxLLTNls3f+TkiteXObY2uLCrBlfDucNP+iaVqSa4DlBDVFlaI9ByZ//hYx6njzbIsHjcoZmMZnduI9hHQZrUFex0Oj/V/g8FaoEP/quGVoh6uQ2CsF/cmh98afM792w744LbhcVj/N1TXdRXlP+yzaePBEEVJQlErU9KoORk/DNe6d08xzigJfJZVzElpvjJwpCCZj9DVCL0yTyUCePKGNRADYAB8jAK3cNnUQnoSvM0+ZzBqRRn0TxNpY96BjSlidgzHFkxPCHIfdTjWsP3Qd7PSJEisTg3WyH3vlZWw1ZnthJrN7NVuY+S5N6zrPvdtWA5qk1SIU3pi74IW8Out3XD+KiCC1Pt3GfG11cdTSx5aRt9Oynjd8ZmOu4ADzEroHeLVKveZNEvAfGLZLubu0jbqxq9vfJkMyRmgQ8OsS6AiHGI8Tk+1aiBIPwoyJ4lCactb/WS2gakI5655Nw1oqp2y/q4Quy1zRPZ2ilephQALRsr2YzebLHounOW3JKPn5d6s0CeoCPwO2V9NczIBG7U+ww=="
cipher7 = conversions.b64_to_as(cipher7_b64)

def binary(num, pre='', length=8, spacer=0):
    return '{0}{{:{1}>{2}}}'.format(pre, spacer, length).format(bin(num)[2:])


theXOR = conversions.as_to_lis(conversions.xor('FROM', cipher7[:4]))
binXOR = bin(191) + binary(107) + binary(0) + binary(7)
ogState = long(binXOR,2)

def make16(s):
    s = s[2:]
    while len(s) < 16:
        s = '0' + s
    s = '0b' + s   
    return s

def splita16(s):
    return s[:10]
def splitb16(s):
    return '0b' + s[10:]


def return_key7(ct):
    first4 = ct[:4]
    first4 = conversions.xor(first4,'FROM')
    text = ct[:20]
    max_score = 0
    max_score_key = ''
    max_score_i = 0
    rating = 0
    for i in range(14814,14815):
         javarandom.state = ogState*(2**16) + i
         keystream = first4 + javarandom.get_bytes(len(ct))
         a = keystream[:len(ct)]
         rating = (1 * count_printable(conversions.xor(text,a))) +(.75 * count_letters(conversions.xor(text,a)))+ (englishy(conversions.xor(text,a)))                                                                                                                  
         if rating >= max_score:
           max_score_i = i
           max_score = rating
           max_score_key = keystream
    return max_score_key

# ogState = what I get after I xor 'FROM' and ct[:4] and then change that to decimal. Calculations above if necessary
def find_key7(ct):
    first4 = ct[:4]
    first4 = conversions.xor(first4,'FROM')
    text = ct[:20]
    max_score = 0
    max_score_key = ''
    max_score_i = 0
    rating = 0
    for i in range(2**16):
         javarandom.state = ogState*(2**16) + i
         keystream = first4 + javarandom.get_bytes(30)
         a = keystream[:20]
         rating = (1 * count_printable(conversions.xor(text,a))) +(.75 * count_letters(conversions.xor(text,a)))+ (englishy(conversions.xor(text,a)))                                                                                                                  
         if rating >= max_score:
           max_score_i = i
           max_score = rating
           max_score_key = keystream
    s = bin(max_score_i)
    s = make16(s)
    b = splita16(s)
    c = splitb16(s)
    bit16 = chr(int(b,2)) +  chr(int(c,2))
    fin = conversions.as_to_hex(bit16)
    return fin


    
    

    
            
		



    
    
        
        

