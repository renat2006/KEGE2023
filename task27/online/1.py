with open("27A.txt") as f:
    N = int(f.readline().strip())
    nums = list(map(lambda x: int(x.strip()), f.readlines()))
    max_pair_sum = -2000    
    for i in range(N):
        for j in range(i + 1, N):
            if ((nums[i] + nums[j]) % 22 == 0) and (nums[i] > nums[j]):
                max_pair_sum = max(max_pair_sum, nums[i] + nums[j])
    print(max_pair_sum)
