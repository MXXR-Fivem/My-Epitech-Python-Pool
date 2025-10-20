def multiplesStriclySmaller(n: int) -> None:
    for i in range(2, int(n/2)+1):
        for j in range(n, 0, -1):
            if i*j < n:
                print(i*j, end=" ")
        print("")

multiplesStriclySmaller(14)