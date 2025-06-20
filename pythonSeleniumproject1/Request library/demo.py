import json

data = {"name": "John Doe","age": 30,"email": "johndoe@example.com", "isEmployed": "true", "skills": ["Python", "Selenium", "Robot Framework"],
        "address": {"street": "123 Main St","city": "New York","zip": "10001"}}
print(data)
print(type(data))
print(data['name'])
print(data['skills'])
print(data['skills'][0])
print(data['skills'][2])
print(data['address'])

# opening the files
with open("C:\\Users\\SONY\\Documents\\new 15.json") as f:
    data3 = json.load(f)
    print(data3 == data)
