import requests
import os
import json

# val = []
# path = os.path.join(os.getcwd(), 'data', 'person.json')
# with open(path, 'r') as file:
#     val.extend(json.load(file))

# print(val)
val = {"last_name": "asdf", "first_name": "asdf", "birth_date": 23, "contact": [{"_contact_type": "phone", "value": 4567},
                                                                                 {"_contact_type": "phone", "value": 78900987}],
        "skills": [{"_category": "technologies", "name": "asdfg", "experience": 1, "_level": "junior", "id": 1},
                   {"_category": "technologies", "name": "vbnm", "experience": 2, "_level": "junior", "id": 2}],
        "experience": [{"start_data": 23, "end_data": 34, "company": "asd", "position": "jun"},
                       {"start_data": 23, "end_data": 34, "company": "fgh", "position": "jun"},
                       {"start_data": 23, "end_data": 34, "company": "jhk", "position": "jun"},
                       {"start_data": 23, "end_data": 34, "company": "cvb", "position": "jun"}]}
# req = requests.post('http://127.0.0.1:5000/', json=val)
#
# print(req.text)
# print(req)

request = requests.patch('http://127.0.0.1:5000/test', json={'id': '3', 'last_name': 'QQQQQQQQ'})
print(request.text)
print(request)