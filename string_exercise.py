# In the given string we have to print the following
# 1.running is virat
# 2.
# 3.Virat Is Running
# 4.gninnur si tariv

# for question no 4
def reverse(s):
    res=""
    for word in s:
        res = word + res
    return res


def word_reverse(s):
    res=""
    split_word=s.split(" ")
    for word in split_word:
        res=word +" "+ res
    return res



s = "virat is running"
result = reverse(s)
result1=word_reverse(s)
print(result)
print(result1)