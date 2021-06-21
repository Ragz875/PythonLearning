def reverse(self, x: int) -> int:
    org = x
    if x < 0:
        x = abs(x)
    if x == 0:
        return 0
    res = 0
    while x > 0:
        res = 10 * res + x % 10
        x = x // 10
    print(res)

    if org < 0 and res * -1 > -(2 ** 31):
        return res * -1
    if org > 0 and res < (2 ** 31):
        return res
    return 0
