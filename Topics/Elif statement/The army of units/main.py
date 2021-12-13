n = int(input())
if n == 0:
    print("no army")
elif 0 < n < 10:
    print("few")
elif 9 < n < 50:
    print("pack")
elif 49 < n < 500:
    print("horde")
elif 499 < n < 1000:
    print("swarm")
else:
    print("legion")
