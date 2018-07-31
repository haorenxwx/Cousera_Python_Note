#week6_testjson.py
import json
data = '''{
	"name" : "Chuck",
	"phone" : {
	"type" : "int1",
	"number" : "+1 734 303 4456"
	},
	"email" : {
	"hide" : "yes"
	}
}'''

info = json.loads(data) #-------generate a dictionary from json
print(type(info))
print('Name:',info["name"])
print('Hide',info["email"]["hide"])