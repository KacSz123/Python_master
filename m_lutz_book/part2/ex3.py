r=11
for i in range(r):
    for j in range(r):
        if i==j:
            print('-', end = ' ')
        elif i+j==r-1:
            print('-', end = ' ')
        else:
            print('o', end = ' ')
    print()