# sentence=input("enter the sentence")
# words=upper=lower=digits=0
# split_sentence=sentence.split()
# print("after applying split sentence:"+str(split_sentence))
# words=len(split_sentence)

# for c in sentence:
#     if c.isupper():
#         upper+=1
#     if c.islower():
#         lower+=1
#     if c.isdigit():
#         digits+=1        
 
# print("words=",words)        
# print("uppercase=",upper)        
# print("lowercase=",lower)        
# print("digits=",digits)



sentence=input("enter the sentence")
word=upper=lower=digits=0
split_sentence=sentence.split()
print("after appling this method",str(split_sentence))
words=len(split_sentence)

for c in sentence:
    if c.isdigit():
        digits+=1
    if c.isupper():
        upper+=1
    if c.islower():
        lower+=1

print("number pf words=",words)
print("number of uppercase letter=",upper)
print("number of uppercase letter=",lower)
print("digits=",digits)
                