#program to find prime no in interval.
start = 11
end = 25
for i in range (start,end):
    for j in range (2,i):
        if i%j==0:
            break
    else:
        print(i)