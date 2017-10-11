
import urllib
import urllib2
#routines for grabbing the encrypted tag from the
#dictionary server
#and posting a request
#back to the server.
import urllib
import urllib2

#This grabs the page and extracts the encrypted tag,
#which is a hex string encrypting a long word from the
#dictionary.

def grab_encrypted_tag():
    f=urllib.urlopen('http://cscicrypto.bc.edu:8080/dictionary')
    s=f.read()
    f.close()
    t=s.index('"',265)
    return s[265:t]


#This makes a post request to the server with
#parameters the guessed captcha text and the
#encrypted tag in hex.

def post_dictionary_guess(guess,encrypted):
    url_2='http://cscicrypto.bc.edu:8080/dictionary'
    values=[('encrypted text',encrypted),('Entry',guess)]
    data = urllib.urlencode(values)
    req = urllib2.Request(url_2, data)
    rsp=urllib2.urlopen(req)
    #print rsp.code
        
    print rsp.read()
