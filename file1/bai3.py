def doc_du_lieu():
    with open('XOANOC.INP', 'r') as f:
        n, m = map(int, f.readline().split())
        a = []
        for i in range(n):
            row = list(map(int, f.readline().split()))
            a.append(row)
    return n, m, a


def sap_xep_mang_2_chieu(n, m, a):
    flatten = [x for row in a for x in row]
    flatten.sort()
    idx = 0
    for i in range(n):
        for j in range(m):
            a[i][j] = flatten[idx]
            idx += 1
    return a


def tao_ma_tran_xoan_oc(n, m, a):
    res = [[0] * m for i in range(n)]
    left, right, top, bottom = 0, m-1, 0, n-1
    cnt = 0
    while left <= right and top <= bottom:
        for j in range(left, right+1):
            res[top][j] = a[cnt // m][cnt % m]
            cnt += 1
        top += 1

        for i in range(top, bottom+1):
            res[i][right] = a[cnt // m][cnt % m]
            cnt += 1
        right -= 1

        if top <= bottom:
            for j in range(right, left-1, -1):
                res[bottom][j] = a[cnt // m][cnt % m]
                cnt += 1
            bottom -= 1

        if left <= right:
            for i in range(bottom, top-1, -1):
                res[i][left] = a[cnt // m][cnt % m]
                cnt += 1
            left += 1
    return res


def ghi_ket_qua(n, m, res):
    with open('XOANOC.OUT', 'w') as f:
        for i in range(n):
            line = ' '.join(map(str, res[i]))
            f.write(line + '\n')


if __name__ == '__main__':
    n, m, a = doc_du_lieu()
    a = sap_xep_mang_2_chieu(n, m, a)
    res = tao_ma_tran_xoan_oc(n, m, a)
    ghi_ket_qua(n, m, res)
