def main():
    m = 1
    f = 1
    n = int(input())
    while 1:
        if n == m:
            break
        f = m*f
        m += 1
    print(f)
main()