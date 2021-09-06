def zoc(m, n):
    if (m == 0) or (n == 0):
        return m+n
    x = zoc(m-1, n)
    y = zoc(m, n-1)
    print(f"x={x}, y={y}")
    return x+y

if __name__ == '__main__':
    print(zoc(3, 2))
