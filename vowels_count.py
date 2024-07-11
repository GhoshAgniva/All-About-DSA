#write a code to count the number of vowels in a string
vowels="aioueAIOUE"
s="hello"
count=0
for i in s:
    if i in vowels:
        count+=1
print(count)



#write a code to count the number of vowels, consonant and white spaces in a string

vowels="aioueAIOUE"

s="hel l o"
vo_count=0
con_count=0
whiteSpace_count=0
for char in s:
    if char in vowels:
        vo_count+=1
    elif char in " ":
        whiteSpace_count+=1

    else:
        con_count+=1



print("Number of vowels: ",vo_count)
print("Number of consonant: ",con_count)
print("Number of white spaces: ",whiteSpace_count)

