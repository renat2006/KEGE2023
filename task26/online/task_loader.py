import os
import requests

with open("tasks.txt", "r") as f:
    links = list(map(str.strip, f.readlines()))

    for i, link in enumerate(links, start=1):
        os.makedirs(str(i))
        data = requests.get(link)
        print(f'{data.text=}')
        with open(f"{i}/data.txt", "w", encoding="utf-8" ) as r:
            r.writelines(data.text.strip().replace("\n", ""))
