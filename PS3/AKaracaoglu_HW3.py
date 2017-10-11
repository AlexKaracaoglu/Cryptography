## Alex Karacaoglu
## Crypto HW 3

import conversions     # I have included both of these files in my zip
import webserver_msgs


def pad_length(ciphertext):
    blocksize = 8   
    if (len(ciphertext) > 48):
        start = 32
        end = 34
    else:
        start = 16
        end = 18
    length = 8
    error_message = 'HTTP/' 
    for i in range(blocksize):
        if (ciphertext[start:end] == 'ff'):
            test = ciphertext[:start] + 'fe' + ciphertext[end:]
        else:
            test = ciphertext[:start] + 'ff' + ciphertext[end:]
        pad_oracle = webserver_msgs.post_dictionary_guess('', test)
        pad_oracle = pad_oracle[0:5]
        if (pad_oracle == error_message):
            break
        else:
            length = length - 1
            start = end
            end = end + 2
    return length #integer 0-7


def last_nonpad_byte(ciphertext):
    empty = '0000000000000000'
    wrong = '<html'  #gives wrong padding
    if (len(ciphertext) > 48):
        start = 32
        end = 48
        c1 = ciphertext[start:end]
    else:
        start = 16
        end = 32
        c1 = ciphertext[start:end]
    as_c1 = conversions.hex_to_as(c1)
    length = pad_length(ciphertext)
    xor_c1 = conversions.xor(chr(length), chr(length + 1))
    hex_xor_c1 = conversions.as_to_hex(xor_c1)
    xor_c1_final = empty[:-(length * 2)] + (hex_xor_c1 * length)
    as_xor_c1 = conversions.hex_to_as(xor_c1_final)
    c2 = conversions.xor(as_c1, as_xor_c1)
    hex_c2 = conversions.as_to_hex(c2)
    oracle = webserver_msgs.post_dictionary_guess('', (ciphertext[:start] + hex_c2 + ciphertext[end:]))
    if (oracle == wrong):
        last_byte = conversions.as_to_hex(chr(length + 1))
    else:
        for i in range(255):
              test_byte = conversions.as_to_hex(chr(i))
              test_byte_as = chr(i)
              xor_c1 = empty[:-((length + 1) * 2)] + test_byte + (hex_xor_c1 * length)
              as_xor_c1 = conversions.hex_to_as(xor_c1)              
              c2 = conversions.xor(as_c1, as_xor_c1)
              hex_c2 = conversions.as_to_hex(c2)
              oracle = webserver_msgs.post_dictionary_guess('', (ciphertext[:start] + hex_c2 + ciphertext[end:]))
              oracle = oracle[0:5]
              if (oracle == wrong):
                  last = conversions.xor(test_byte_as, chr(length + 1))
                  last = conversions.as_to_hex(last)
    return last
