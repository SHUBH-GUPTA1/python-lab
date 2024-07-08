# str1=input("enter string 1")
# str2=input("enter string 2")
# if len(str1)<len(str2):
#     short=len(str1)
#     long=len(str2)
# else:
#     short=len(str2)    
#     long=len(str1)
    
# matchCnt=0

# for i in range(short):
#     if str1[i]==str2[i]:
#         matchCnt+=1    
        
# print("similarity between 2 strings are")
# print(matchCnt/long)                



str1=input("enter the string 1")
str2=input("enter the string 2")
if len(str1)<len(str2):
    short=len(str1)
    long=len(str2)
else:
    short=len(str2)
    long=len(str1)

matchCnt=0
for i in range(short):
    if str1[i]==str2[i]:
        matchCnt+=1

print("similarirty between 2 strings is ")                
print(matchCnt/long)