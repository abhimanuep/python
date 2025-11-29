n = 11
if n == 1:
    print('prime')

else:
    for i in range(2,n):
        if n%i == 0:
            print('note a prime')
            break
    else:
        print('prime')