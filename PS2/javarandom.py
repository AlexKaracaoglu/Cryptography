#The standard random number generator built in to java.util.Random.

#The 48-bit state is is modified by a linear congruential iteration:
#  state<----state*multiplier + modulus mod 2**48

#The nextInt method updates the state and returns a 32-bit result:  bits 47..16
#of the state.

#In this implementation we return the 32-bit output as a 4-byte ASCII string.



import conversions

state=1L

#The key is an ASCII string which we convert to a long, then grab the low-order
#48 bits

def init_state(key):
    global state
    bytelist=conversions.as_to_lis(key)
    val=0
    for by in bytelist:
        val=val*256+by
    state=val&(0xffffffffffffL)
    return state


def update_state():
    global state
    state = (state *0x5deece66dL + 0xb)&(0xffffffffffffL)

#The rng outputs 4 bytes at a time.
def next_bytes():
    update_state()
    #output 32 is bits 47..16 of new state;
    #this is the usual output of nextInt in java.util.Random
    output32=(state>>16)&(0xffffffff)
    blist=[int((output32>>(8*j))&0xff) for j in range(3,-1,-1)]
    return conversions.lis_to_as(blist)

#This gives an output stream of k' "random" characters, where
#k' is the smallest multiple of 4 that is >= k.
def get_bytes(k):
    blocks=k/4
    if k%4!=0:
        blocks+=1
    bstream=''
    for j in range(blocks):
        bstream+=next_bytes()
    return bstream

#encrypt/decrypt plaintext/ciphertext with given key
def encdec(key,message):
    init_state(key)
    keystream=get_bytes(len(message))
    return conversions.xor(keystream,message)
