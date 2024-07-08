# def some2dec(n:str,base:int):
#     if len(n)==1:
#         return int(n)
#     return int (n[0])*base**(len(n)-1)+some2dec(n[1:],base)

# def mapper(n:int):
#     if n<=9:
#         return str(n)
#     s={10:"A",11:"B",12:"C",13:"D",14:"E",15:"F"}
#     return s[n]

# def dec2hex(x:int):
#     if x<16:
#         return mapper(x)
#     else:
#         return dec2hex(x//16)+mapper(x%16)

# print("1.binary to decimal")    
# print("2.octal to hexadecimal")    
# ch=int(input("enter the choice"))
# if ch==1:
#     num=input("enter the number")
#     print("decimal=",some2dec(num,2))
# elif ch==2:
#     num=input("enter the number")
#     print("hexadecimal=",dec2hex(some2dec(num,8)))
# else:
#     print("invalid choice")     


# def som2dec(n:str,base:int):
#     if len(n)==1:
#         return int(n)
#     return int (n[0])*base**(len(n)-1)+som2dec(n[1:],base)   

# def mapper(n:int):
#     if n<=9:
#         return str(n)
#     s={10:"A",11:"B",12:"C",13:"D",14:"E",15:"F"}
#     return s[n]

# def dec2hex(x:int):
#     if x<16:
#         return mapper(x)
#     else:
#         return dec2hex(x//16)+mapper(x%16)

# print("1.binary to decimal")    
# print("2.octal to hexadecimal")    
# ch=int(input("enter the choice"))
# if ch==1:
#     n=input("enter the binary number")
#     print("decimal=",som2dec(n,2))
# elif ch==2:
#     n=input("enter the octal number")
#     print("hexadicamal=",dec2hex(som2dec(n,8)))
# else:
#     print("invalid choice")    
        
        

def some2dec(n:str,base:int):
    if len(n)==1:
        return int(n)
    return int (n[0])*base**(len(n)-1)+some2dec(n[1:],base)

def mapper(n:int):
    if n<=9:
        return str(n)
    s={10:"A",11:"B",12:"C",13:"D",14:"E",15:"F"}
    return s[n]

def dec2hex(x:int):
    if x<16:
        return mapper(x)
    else:
        return dec2hex(x//16)+mapper(x%16)
    
print("1.binary to decimal")
print("2.octal to hexadecimal")
ch=int(input("enter the choice"))
if ch==1:
    n=input("enter the binary number")
    print("decimal=",some2dec(n,2))
elif ch==2:
    n=input("enter the binary number") 
    print("hexadecimal=",dec2hex(some2dec(n,8)))
else:
    print("invalid choice")