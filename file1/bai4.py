def sinh_day_nhi_phan(n):
    if n == 0:
        return [""]

    day_nhi_phan_ngan_hon = sinh_day_nhi_phan(n - 1)

    return ["0" + s for s in day_nhi_phan_ngan_hon] + ["1" + s for s in day_nhi_phan_ngan_hon]


def main():
    with open("BAI42QL.INP", "r") as f:
        n = int(f.readline())

    day_nhi_phan = sinh_day_nhi_phan(n)

    with open("BAI42QL.OUT", "w") as f:
        for nhi_phan in day_nhi_phan:
            f.write(nhi_phan + "\n")


if __name__ == "__main__":
    main()
