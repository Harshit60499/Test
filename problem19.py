N = int(input("Define the limit of natural number : "))

def pyt():
    for a in range(1,N):
        for b in range(1,N):
            for c in range(1,N):
                if (a**2) + (b**2) -(c**2) == 0:
                    print(a,b,c)
pyt()