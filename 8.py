# class PaliStr:
#     def __init__(self):
#         self.isPali=False
#     def chkPalindrome(self,str):
#         if str==str[::-1]:
#             self.isPali=True
#         else:
#             self.isPali=False
#         return self.isPali
   
# class Paliint(PaliStr):
#     def __init__(self):
#         self.isPali=False
#     def chkPalindrome(self,val):
#         temp=val
#         rev=0
        
#         while temp!=0:
#             dig=temp%10
#             rev=(rev*10)+dig                    
#             temp=temp//10
#         if val==rev:
#             self.isPali=True
#         else:
#             self.isPali=False
#         return self.isPali
    
# st=input("enter the string to check palindrome")
# stobj=PaliStr()  
# if stobj.chkPalindrome(st):
#     print("the given string is a palindrome")              
# else:
#     print("not a plaindrome")

# ans=int(input("enter the value"))        
# stint=Paliint()
# if stint.chkPalindrome(ans):
#     print("the given number is a plaindrome")
# else:
#     print("not a palindrome")








class PaliStr:
    def __init__(self):
        self.isPali=False
    def chkPalindrome(self,str):
        print('parent')
        if str==str[::-1]:
            self.isPali=True
        else:
            self.isPali=False
        return self.isPali        

class PaliInt(PaliStr):
    def __init__(self):
        self.isPali=False
    def chkPalindrome(self,val):
        print('child')    
        temp=val
        rev=0
        while temp!=0:
            dig=temp%10
            rev=(rev*10)+dig
            temp=temp//10
        if val==rev:
            self.isPali=True
        else:
            self.isPali=False
        return self.isPali

st=input("enter the string")
stobj=PaliStr()
if stobj.chkPalindrome(st):
    print("the string is a plaindrome")
else:
    print("Not a palindrome")

ans=int(input("enter the value"))
intobj=PaliInt()
if intobj.chkPalindrome(ans):
    print("the string is a plaindrome")
else:
    print("Not a palindrome")
        