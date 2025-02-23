
shift = 4
#salom

#wepsq
import string
print(string.ascii_lowercase)


# word = 'python'
# shift = 5


def ceaser_ciph(word,shift):
    res = ''
    alphabet = string.ascii_lowercase
    for i in word:
        ind = alphabet.index(i)
        ind = ind + shift
        if ind +1 >= len(alphabet):
            rest_part = ind + 1 - len(alphabet)
            res = res + alphabet[rest_part -1]
        else:
            res = res + alphabet[ind]
    return res

a = ceaser_ciph('world',4)
print(a)
        
