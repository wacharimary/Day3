from urllib.request import urlopen
import json


def get_data():

	api_url='http://api.timezonedb.com/v2/get-time-zone?key=SYSFPHBAB0VJ&format=json&by=zone&zone=Africa/Dar_es_salaam'

	request=urlopen(api_url)

	figure=request.read().decode('utf')

	json_object=json.loads(figure)

	print(json.dumps(json_object))

	get_data()
