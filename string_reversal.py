def reverse(s):
    res=""
    for i in s:
        res=i+res

    return res
s="momo"
rev=reverse(s)
print(rev)
if s == rev:
    print("palimdrome")
else:
    print("not palimdrome")
