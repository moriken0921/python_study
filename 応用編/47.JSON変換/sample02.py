import json

json_data = {'Python':'python-izm.com',
             'SearchEngin':('google.co.jp', 'yahoo,co.jp')}

encode_json_data = json.dumps(json_data)
print(type(encode_json_data))

decode_json_data = json.loads(encode_json_data)
print(encode_json_data)
print(type(encode_json_data))
