# Gray code, https://oeis.org/A003188

n = 32

for i in range(n):
    a = i ^ (i // 2)
    print(f"{a:08b} {a:03d}")
