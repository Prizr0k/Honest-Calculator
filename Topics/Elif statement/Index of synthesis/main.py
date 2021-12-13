index_n = float(input())
if index_n < 2:
    print("Analytic")
elif 2 <= index_n <= 3:
    print("Synthetic")
else:
    print("Polysynthetic")
