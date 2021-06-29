#corey schafer's 
#https://www.youtube.com/watch?v=1lxrb_ezP-g&t=6s
import json
import requests
import time

r = requests.get("https://formulae.brew.sh/api/formula.json")
packages_json = r.json()

results = []
i=0

for package in packages_json:
  package_name = package["name"]
  package_desc = package["desc"]

  package_url = f"https://formulae.brew.sh/api/formula/{package_name}.json"

  r = requests.get(package_url)
  package_json = r.json() 
  print(package_json)
  
  installs_30 = package_json["analytics"]["install"]["30d"][package_name]
  installs_90 = package_json["analytics"]["install"]["90d"][package_name]
  installs_365 = package_json["analytics"]["install"]["365d"][package_name]
 
  data = {
    "name": package_name,
    "desc" : package_desc,
    "analytics" : {
      "30d" : installs_30,
      "90d" : installs_90,
      "365d": installs_365
      }
  }

  results.append(data)

  time.sleep(r.elapsed.total_seconds())

  print(package_name, package_desc, installs_30, installs_90, installs_365)

  i += 1

  if i == 4:
    break
  
print(results)

with open("output.json", "w") as f:
  json.dump(results, f, indent=2)




