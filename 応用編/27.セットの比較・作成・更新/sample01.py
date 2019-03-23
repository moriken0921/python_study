test_set_1 = set(['python', '-', 'izm', '.', 'com'])

print(test_set_1.isdisjoint({'python', 'izm'}))
print(test_set_1.isdisjoint({1, 2, 3}))

print('----------------------------')

print(test_set_1.issubset({'python', 'izm'}))
print(test_set_1.issubset({'www', 'python', '-', 'izm', '.', 'com'}))

print('----------------------------')

print(test_set_1.issuperset({'python', 'izm'}))
print(test_set_1.issuperset({'www', 'python', '-', 'izm', '.', 'com'}))
