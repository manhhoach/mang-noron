import math

# s=int(input("Nhap n="))
# multi=1
# for i in range(1,s+1):
#   multi*=i

# print('giai thua cua %d la %d' %(s, multi))

# def recursive(n):
#   if n==1: return 1
#   else: return n*recursive(n-1)

# print(recursive(s))

a = int(input('Nhap a='))
b = int(input('Nhap b='))
c = int(input('Nhap c='))
if (a > 0 and b > 0 and c > 0 and a+b > c and c+b > a and a+c > b):
    chuvi = a+b+c
    p = chuvi/2
    dientich = math.sqrt(p*(p-a)*(p-b)*(p-c))
    print('chu vi = %d, dien tich = %d' % (chuvi, dientich))
else:
    print('Do dai khong hop le')

# x, y = input("Enter a two value: ").split()

# print("Number of boys: ", x) 

# print("Number of girls: ", y)

# print()
