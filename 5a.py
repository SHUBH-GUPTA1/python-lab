# import re
# def is_phonenumber(number):
#     if len(number)!=12:
#         return False
#     elif number[3]!='-' and number[7]!='-':
#         return False
    
#     for i in range(12):
#         if i==3 or i==7:
#             continue
#         if not number[i].isdigit():
#             return False
#     return True

# def isphonenumber_reg(number):
#     pattern=r'\d{3}-\d{3}-\d{4}'
#     match=re.fullmatch(pattern,number)
#     return match is not None

# ph_num=input("enter the number in ddd-ddd-dddd format")
# print("1.check witchout using regex exp")
# print("2.check witch using regex exp")
# ch=int(input("enter the choice"))
# if ch==1:
#     res=is_phonenumber(ph_num)
#     if res==True:
#         print("the"+ph_num+"is valid")
#     else:
#         print(ph_num+"is not valid")
# elif ch==2:
#     res=isphonenumber_reg(ph_num)
#     if res==True:
#         print("the"+ph_num+"is valid")
#     else:
#         print(ph_num+"is not valid")
# else:
#     print("enter the valid choice")














import re
def isphonenumber(number):
    if len(number)!=12:
        return False
    if number[3]!='-' and number[7]!='-':
        return False
    for i in range(12):
        if i==3 or i==7:
            continue
        if not number[i].isdigit():
            return False
    return True

def isphonenumber_reg(number):
    pattern=r"\d{3}-\d{3}-\d{4}"
    match=re.fullmatch(pattern,number)
    return match is not None

ph_num=input("enter the number in ddd-ddd-dddd format")    
print("1.without using reg operation")
print("2.using reg operation")
ch=int(input("enter the choice"))
if ch==1:
    res=isphonenumber(ph_num)
    if res==True:
        print(ph_num+"is valid")
    else:
        print(ph_num+"is not valid")    
elif ch==2:
    res=isphonenumber_reg(ph_num)
    if res==True:
        print(ph_num+"is valid")
    else:
        print(ph_num+"is not valid")  
else:
    print("invali choice")             