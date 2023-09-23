def prime(x):
    flag = 0
    if x>1:
     for i in range(2, x):
            if (x % i) == 0:
                flag = 1
                break
    if flag == 1:
        return 0
    else:
        return 1

        m= int(input("enter first number:"))
        n = int(input("enter second number:"))
    if prime(m) and prime(n):
        diff = abs(m-n)
    if diff == 2:

            print(m, "and", n, "are twin prime number")
    else:
            print(m, "and", n, "is not twin prime number")
