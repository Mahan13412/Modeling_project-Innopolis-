maxx = 0
for i in range(4, 10000):
    sum = 0
    N = int('5' + '2' * i)
    while '52' in str(N) == True or "2222" in str(N) == True or '1122' in str(N) == True:
        if 52 in N == True:
            N = int(str(N).replace(52, 11))
        if 2222 in N == True:
            N = int(str(N).replace(2222, 5))
        if 1122 in N == True:
            N = int(str(N).replace(1122, 25))
        for x in range(len(str(N))):
            sum += int(str(N)[x])
        if sum == 64 and N > maxx:
            maxx = N
print(maxx)
        
