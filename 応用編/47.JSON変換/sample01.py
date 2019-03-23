import json

json_data = {'Python':'python-izm.com',
             'SearchEngin':('google.co.jp', 'yahoo,co.jp')}

print(type(json_data))

encode_json_data = json.dumps(json_data, indent=4)

print(encode_json_data)
print(type(encode_json_data))
