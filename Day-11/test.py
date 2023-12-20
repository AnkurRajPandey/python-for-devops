my_list = {'name': 'Ankur', 'Age': 34, 'Sex': 'Male'}
print(my_list['Sex'])

student_data = [
    {
        "name": "Ankur",
        "Age":34,
        "Sex":"Male"

    },
    {
        "name":"Shalu",
        "Age":30,
        "Sex":"Female"
    },
    {
        "name":"Aalu",
        "Age":3,
        "Sex":"Male"
    }
]
print(student_data[2]["name"])



print("-------------------------------")

import requests
url= "https://api.github.com/repos/kubernetes/kubernetes/pulls"
response = requests.get(url)

pull_request =  response.json()

pr_creators = {}

for pull in pull_request:
    creator = pull['user']['login']
    if creator in pr_creators:
        pr_creators[creator] += 1
    else:
        pr_creators[creator] = 1

print("PR creators and counts")
for creator, count in pr_creators.items():
    print(f"{creator}: {count}")








