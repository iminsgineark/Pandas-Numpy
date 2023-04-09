def Max(n1, n2, n3):
    if n1 > n2 and n1 > n3:
        print("N1 Is Greatest Among Three")
    elif n2 > n1 and n2 > n3:
        print("N2 Is Greatest Among Three")
    else:
        print("N3 Is Greatest Among Three")


Number1 = int(input("Enter Number 1\n"))
Number2 = int(input("Enter Number 2\n"))
Number3 = int(input("Enter Number 3\n"))
Max(Number1, Number2, Number3)