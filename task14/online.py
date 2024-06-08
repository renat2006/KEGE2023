for x in range(12):
    r = int(f"2{x}1{x}7", 12) + int(f"3{x}A{x}21", 12)
    if r % 17 == 0:
        print(r // 17)