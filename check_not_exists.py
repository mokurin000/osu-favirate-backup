import os

with open("id.txt", "r", encoding="utf-8") as f:
    id_list = f.read().strip().splitlines()
    id_list = [id_ for id_ in id_list if id_]

files = [f for f in os.listdir("tmp") if f.endswith(".osz")]
print(*(id for id in id_list if f"{id}.osz" not in files))
