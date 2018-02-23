import sys
import requests, json
from pprint import pprint

class Weather():

	def ShowMeTheWeather(self, city, country):
		baseurl = "https://query.yahooapis.com/v1/public/yql?"
		url = baseurl+'q=select%20*%20from%20weather.forecast%20where%20woeid%20in%20(select%20woeid%20from%20geo.places(1)%20where%20text%3D%22{0}%2C%20{1}%22)&format=json'.format(city, country)
		hardcoded_response = requests.get(url)
		data3 = json.loads(hardcoded_response.text)
		return (data3["query"])

	def fToC(self, temp):
		return temp-32*(0.5556)

	def cToF(self, temp):
		return temp+32*(0.5556)