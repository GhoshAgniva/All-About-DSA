def reverse(s):
    res=""
    for char in s:
        res=chr(ord(char)+1)+res
    return res
s="ABDEF"
result=reverse(s)
print(result)

