def triple(n):
    return n + n + n
numbers = [1,2,3,4,5,6,7]
result = map(triple, numbers)
print(list(result))

