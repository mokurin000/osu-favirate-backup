import os

with open("id.txt", "r", encoding="utf-8") as f:
    id_list = f.read().strip().splitlines()
    id_list = [id_ for id_ in id_list if id_]

urls = [
    f"https://cmcc.sayobot.cn:25225/beatmaps/{id_[:3]}/{id_[3:]}/full?filename={id_}"
    for id_ in id_list
]

os.makedirs("tmp", exist_ok=True)

with open("tmp/sayo.txt", "w", encoding="utf-8") as f:
    f.write("\n".join(urls))
