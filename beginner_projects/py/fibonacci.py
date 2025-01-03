#0 1 1 2 3 5 8 13 21 ....
def fibo(n):
    a=0
    b=1
    while a<n:
        print(a,end='  ')
        a,b=b,a+b

n=int(input('Enter number : '))
print('fibonacci : ',end='')
fibo(n)    

    