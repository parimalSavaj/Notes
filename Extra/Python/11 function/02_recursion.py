# factorial example

def fact(number):
    if(number <= 1):
        return 1   
    ans = number * fact(number - 1) 
    return ans

a = fact(5)
print(a)
b = fact(0)
print(b)
c = fact(1)
print(b)