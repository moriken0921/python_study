test_set_1  = {'python', '-', 'izm', '.', 'com'}

# issubsetと同じ
print(test_set_1 <= {'python', 'izm'})
print(test_set_1 <= {'www', 'python', '-', 'izm', '.', 'com'})

print('----------------------------')

# issupersetと同じ
print(test_set_1 >= {'python', 'izm'})
print(test_set_1 >= {'www', 'python', '-', 'izm', '.', 'com'})
