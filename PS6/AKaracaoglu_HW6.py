#Alex Karacaoglu
#HW 6-Hash Functions
#Due Wednesday, April 5

import hashlib
import random
import string
import conversions

         
#Problem 2: birthday2()
#Code follows logic of the 'Lecture 10' notes, specifically the diagram on this low memory attack

#Wrote this helper function to tidy up the code, hashes a string n times, taking the high order 10 hex bytes after each hash
def hashnTimes(s, n):                        #Call hash function n times
    count = 0
    while (count < n):
        s = hashlib.sha1(s).hexdigest()
        s = s[0:10]
        count = count + 1
    return s

def birthday2():
    random_string = ""
    for i in range(100):
        random_string = random_string+random.choice(string.hexdigits)
    random_string = conversions.hex_to_as(random_string)
    h1 = hashnTimes(random_string, 1)     #totalHashCount = 1
    h2 = hashnTimes(random_string, 2)     #totalHashCount = 1 + 2 = 3
    totalHashCount = 3
    while (h1 != h2):
        h1 = hashnTimes(h1, 1)
        h2 = hashnTimes(h2, 2)
        totalHashCount = totalHashCount + 3
    second_stage_h1 = random_string
    second_stage_h1 = hashnTimes(second_stage_h1, 1)
    second_stage_h2 = h1
    second_stage_h2 = hashnTimes(second_stage_h2, 1)
    totalHashCount = totalHashCount + 2
    while(second_stage_h1 != second_stage_h2):
        saved_h1 = second_stage_h1
        saved_h2 = second_stage_h2
        second_stage_h1 = hashnTimes(second_stage_h1, 1)
        second_stage_h2 = hashnTimes(second_stage_h2, 1)
        totalHashCount = totalHashCount + 2
    s = saved_h1
    t = saved_h2
    n = totalHashCount
    return (s, t, n)


          
    
    
        
        
    
    

    
        
        
    

