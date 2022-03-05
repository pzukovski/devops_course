import requests

result = requests.get("https://api.github.com/users/gitelmandanny/repos")


result_json=result.json()
print(result_json)


#resss=result_json[0].get("name")
#print(resss)

#keys=result_json[0].keys()
#print(keys)

for paul in result_json:
    print(paul.get('full_name'))






