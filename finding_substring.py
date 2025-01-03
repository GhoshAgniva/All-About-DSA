#write a code that will print all substring of a string(importent)
str=input()
for i in range(0,len(str)):
    for j in range(i,len(str)):
        print(str[i:j+1])

#-----------------------------------------------------------------------------------------

#Write a program that will print the substring only if substring is palimdrome
def reverse(s):
    res=""
    for i in s:
        res=i+res
    return res

def print_substring(s):
    for i in range(0,len(s)):
        for j in range(i,len(s)):
            answer=(s[i:j + 1])
            if reverse(answer) == answer:
                print(answer)

s="abcbc"
print_substring(s)

#--------------------------------------------------------------------------------------------------------

#write a code that will print longest palimdrome substring
def reverse(s):
    res=""
    for i in s:
        res=i+res
    return res

def print_substring(s):
    longest=0
    longest_str=""
    for i in range(0,len(s)):
        for j in range(i,len(s)):
            answer=s[i: j+1]
            if reverse(answer) == answer and len(answer)>longest:
                longest_str=answer
                longest = len(answer)
    print(longest_str)

s="abcbab"
print_substring(s)
