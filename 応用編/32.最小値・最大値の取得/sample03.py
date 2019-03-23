def key_func(n):
    return n[2]


# code / name / score
l = [(1, 'Python', 100), (2, 'Ruby', 80), (3, 'Perl', 40)]

print(min(l, key=key_func))
print(max(l, key=key_func))
