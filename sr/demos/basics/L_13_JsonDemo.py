import json

# TODO check dumping classes

# Object to Json
print(json.dumps(True))
print(json.dumps(["A", "b", "C"]))
json_string = json.dumps({'name': 'sr', 'address': {'line1': 'a', 'pin': 411045}, 'phones': [3241231, 67656435]},
                         indent=True, sort_keys=True)

print(json_string)
object = json.loads(json_string)

# Json to object
print("pin", object['address']['pin'])
