str1=input("enter the first string:")
str2=input("enter the second string:")
len1=len(str1)
len2=len(str2)
if len1 > len2:
    print("the string with maximum length is :\n",st1)
elif len2 > len1:
    print("the string with maximun length is :\n",str2)
else:
       print("both the string is equal.")
       print("the concatenated string is :",str1+str2)