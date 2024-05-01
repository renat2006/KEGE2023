import os
import requests

START = 2
with open("tasks.txt", "r") as f:
    links = list(map(str.strip, f.readlines()))

    for i, link in enumerate(links, start=START):
        # data = requests.get(link)
        os.mkdir(str(i))
        with open(f"{i}/{i}.py", "w") as r:
            r.write("")
        # with open(f"{i}/data.txt", "w") as r:
        #     r.write(data.text.strip())
