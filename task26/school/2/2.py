with open("data.txt") as f:
    P, N = map(int, f.readline().split())
    min_avg = 1e9
    max_delta = 0
    max_delta_id = 0
    print(P, N)
    rates = dict()
    for rate_str in f.readlines():
        rate_id, rate = map(int, rate_str.split())
        if rate_id in list(rates.keys()):
            rates[rate_id]["rate"].append(rate * 100)
        else:
            rates[rate_id] = {
                "rate": [],
                "med": 0,
                "avg": 0

            }

    for rate_id, rate_dict in list(rates.items()):
        rate_list = rate_dict["rate"]
        x = int(P / 100 * len(rate_list))

        rates[rate_id]["rate"] = sorted(rates[rate_id]["rate"])[x:-x]

    for rate_id, rate_dict in list(rates.items()):
        rate_list = rate_dict["rate"]
        rate_dict["avg"] = sum(rate_list) / len(rate_list)

        rate_dict["med"] = rate_list[len(rate_list) // 2] if len(rate_list) % 2 != 0 \
            else (rate_list[len(rate_list) // 2] + rate_list[len(rate_list) // 2 - 1]) / 2
        min_avg = min(rate_dict["avg"], min_avg)
        print(rate_dict["med"], rate_dict["avg"])
        delta = abs(rate_dict["med"] - rate_dict["avg"])
        if delta >= max_delta:
            if max_delta == delta:
                max_delta_id = max(rate_id, max_delta_id)
            else:
                max_delta_id = rate_id
            max_delta = delta
    print(int(min_avg), max_delta_id)
