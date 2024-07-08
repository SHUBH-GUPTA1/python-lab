# num=input("enter the number to check")

# if num==num[::-1] :
#     print("the number is a palindrome")
# else:
#     print("the number is not a plaindrome")    
# digit_counts={}

# for digit in num:
#     if digit in digit_counts:
#         digit_counts[digit]+=1
#     else:
#         digit_counts[digit]=1
# print("digit counts:",digit_counts)                



# num=input("enter the number to check")
# if num==num[::-1]:
#     print("the number is a plaindrome")
# else:
#     print("not a plaindrome")
# digitcounts={}
# for digit in num:
#     if digit in digitcounts:
#         digitcounts[digit]+=1        
#     else:
#         digitcounts[digit]=1    

# print("digit counts:",digitcounts)    


num=input("enter the string to check")    
if num==num[::-1]:
    print("the number is a palindrome")
else:
    print("not a palindrome")
digit_counts={}
for digit in num:
    if digit in digit_counts:
        digit_counts[digit]+=1
    else:
        digit_counts[digit]=1            

print("digit counts:",digit_counts)
