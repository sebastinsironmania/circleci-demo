# def Palindrome(strParam):
#       strParam=strParam.replace(" ","")
#   l = len(strParam)
#   # code goes here
#   for i in range(l//2):
#     if strParam[i] != strParam[l-i-1]:
#       return False
#   return True
#   #return strParam == strParam[::-1] 
# # keep this function call here 
# print Palindrome(raw_input())

# a="listen"
# b="silent"
# # a=str(a)
# # b=str(b)
# count=0
# for i in a:
#     for j in b:
#         if i==j:
#             count=count+1
# if count==len(a):
#     print("Anagram")
# else:
#     print("Not an Anagram")


# a=828
# b=224
# # print(sorted(a))
# a=str(a)
# b=str(b)
# # print(sorted(a))
# # print(type(a))
# if(sorted(a)==sorted(b)):
#     print("Anagram")
# else:
#     print("Not an anagram")

a=224
b=a%10
a=a//10
print(a)
print(b)



