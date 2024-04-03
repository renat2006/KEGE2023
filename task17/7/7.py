with open("data.txt") as f:
    nums = list(map(lambda x: int(x.strip()), f.readlines()))


    def is_num_simple(a: int):
        is_simple = True
        for d in range(2, round(a ** 0.5) + 1):
            if a % d == 0:
                is_simple = False
                break
        return is_simple


    mx = 0
    count = 0
    s_count = 0

    for i in range(len(nums)):
        if nums[i] % 3 == 0 and nums[i] % 27 != 0:
            if nums[i] > mx:
                mx = nums[i]
    print(mx)
    indx = []
    for j in range(len(nums) - 2):
        c1 = nums[j]
        c2 = nums[j + 1]
        c3 = nums[j + 2]
        if ((is_num_simple(c1) and is_num_simple(c2) and not is_num_simple(c3)) or (
                is_num_simple(c1) and not is_num_simple(c2) and is_num_simple(c3)) or (
                    not is_num_simple(c1) and is_num_simple(c2) and is_num_simple(c3))) or (
                c1 > mx or c2 > mx or c3 > mx):
            count += 1
            if is_num_simple(c1) and j not in indx:
                s_count += 1
                indx.append(j)
            if is_num_simple(c2) and (j + 1) not in indx:
                s_count += 1
                indx.append(j + 1)
            if is_num_simple(c3) and (j + 2) not in indx:
                s_count += 1
                indx.append(j + 2)
    print(f'{count}*{s_count}')
