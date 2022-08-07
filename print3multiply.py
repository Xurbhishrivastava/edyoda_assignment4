def triple(n):
    return n + n + n
lst=[]
num=int(input("Enter the number of digits in the series: "))
for n in range(num):
        series= int(input("Enter the numbers of the series:"))
        lst.append(series)

result = map(triple, lst)
print(list(result))
