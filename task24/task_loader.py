import os
import requests

with open("tasks.txt", "r") as f:
    links = list(map(str.strip, f.readlines()))

    for i, link in enumerate(links, start=10):
        data = requests.get(link)
        with open(f"{i}/data.txt", "w") as r:
            r.write(data.text)
