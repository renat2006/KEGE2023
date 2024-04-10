import fnmatch
cands = []
for i in range(131, 10**8, 131):
    if fnmatch.fnmatch(str(i), "*13?*?1*"):
        cands.append(i)
for cand in cands[1130::1131]:
    print(f'{cand}*{cand // 131}', end='-')