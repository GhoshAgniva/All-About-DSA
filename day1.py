#what is the output for this code
def print_num(num):
    if num==0:
        print(num)
        return
    print_num(num-1)
    print(num)
num = 5
res=print_num(num)
print(res)