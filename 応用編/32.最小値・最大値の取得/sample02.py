def key_func(n):
    return int(n)


l = [2, 3, 4, '111']

print(min(l, key=key_func))
print(max(l, key=key_func))


print('--------------------------')

def key_func(n):
    return str(n)


l = [2, 3, 4, '111']

print(min(l, key=key_func))
print(max(l, key=key_func))


print('--------------------------')

l = [2, 3, 4, '111']

print(min(l, key=int))
print(max(l, key=int))

print(min(l, key=str))
print(max(l, key=str))
