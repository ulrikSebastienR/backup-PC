import json

def install_sort(package):
    return package["analytics"]["30d"]

with open("output.json", "r") as f:
    data = json.load(f)
    print(data)

data.sort(key=install_sort,reverse=True)
print(data)

data_str = json.dumps(data, indent=2)
print(data_str)