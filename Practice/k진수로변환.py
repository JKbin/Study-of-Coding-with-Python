import string

tmp = string.digits+string.ascii_lowercase
# '0123456789ABCDEF'

def convert(num, base) :
    q, r = divmod(num, base)
    if q == 0 :
        return tmp[r] 
    else :
        return convert(q, base) + tmp[r]
    
    
print(convert(15,16))

