

import string

def decode(coded,shift):
    alphabet=string.ascii_lowercase
    res=''
    for i in coded:
        index=alphabet.index(i)
        old_index=index-shift
        if old_index<0:
            rest=shift-index
            old_index=len(alphabet)-1-rest
            res = res + alphabet[old_index]
        else:
            res = res + alphabet[old_index]
    return res
a = decode('wepsq',4)
print(a)