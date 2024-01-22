def ucln(a, b):
    while b:
        a, b = b, a % b
    return a

def tim_uoc_chung(arr):
    uoc_chung = arr[0]
    for i in range(1, len(arr)):
        uoc_chung = ucln(uoc_chung, arr[i])
    return uoc_chung

def tim_uoc_chung_lon_nhat(arr):
    uoc_chung_lon_nhat = 0
    for i in range(len(arr)):
        dem = 0
        for j in range(len(arr)):
            if arr[j] % arr[i] == 0:
                dem += 1
        if dem == len(arr) - 1 and arr[i] > uoc_chung_lon_nhat:
            uoc_chung_lon_nhat = arr[i]
    return uoc_chung_lon_nhat

def main():
    with open("TCONE.INP", "r") as f:
        n = int(f.readline())
        arr = list(map(int, f.readline().split()))

    uoc_chung = tim_uoc_chung(arr)
    uoc_chung_lon_nhat = tim_uoc_chung_lon_nhat(arr)

    with open("TCONE.OUT", "w") as f:
        if uoc_chung_lon_nhat > uoc_chung:
            f.write(str(uoc_chung_lon_nhat))
        else:
            f.write(str(uoc_chung))

if __name__ == "__main__":
    main()
