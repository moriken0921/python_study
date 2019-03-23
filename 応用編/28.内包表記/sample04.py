comp_list = [i * ii for i in range(1, 10) for ii in range(1,10)]

print(comp_list)

print('--------------------------------------')

comp_list = []
for i in range(1, 10):
    for ii in range(1, 10):
        comp_list.append(i * ii)

print(comp_list)
