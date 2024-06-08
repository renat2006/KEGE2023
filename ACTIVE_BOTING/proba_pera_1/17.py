with open("17.txt") as f:
    nums = list(map(int, f.readlines()))
    m5 = 1e9
    k = 0
    ms = 0
    for n in nums:
        if (100 <= n <= 999) and n % 10 == 5:
            m5 = min(m5, n)

    print(m5)
    for i in range(len(nums) - 1):
        c1 = nums[i]
        c2 = nums[i + 1]
        if (100 <= c1 <= 999 or 100 <= c2 <= 999) and (c1 + c2) % m5 == 0:
            k += 1
            ms = max(ms, c1 + c2)
    print(k, ms)
