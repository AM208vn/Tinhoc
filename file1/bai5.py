def kiem_tra_sieu_nguyen_to(n):
    while n > 0:
        if not kiem_tra_nguyen_to(n):
            return False
        n //= 10

    return True


def kiem_tra_nguyen_to(n):
    if n <= 1:
        return False

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False

    return True


def sinh_sieu_nguyen_to(n):
    sieu_nguyen_to = []

    for i in range(10 ** (n - 1), 10 ** n):
        if kiem_tra_sieu_nguyen_to(i):
            sieu_nguyen_to.append(i)

    return sieu_nguyen_to


def main():
    with open("BAI40QL.INP", "r") as f:
        n = int(f.readline())

    sieu_nguyen_to = sinh_sieu_nguyen_to(n)

    if len(sieu_nguyen_to) == 0:
        with open("BAI40QL.OUT", "w") as f:
            f.write("-1")
    else:
        with open("BAI40QL.OUT", "w") as f:
            for sieu_nguyen_to in sieu_nguyen_to:
                f.write(str(sieu_nguyen_to) + "\n")


if __name__ == "__main__":
    main()
