import requests

url= 'http://greenteapress.com/thinkpython2/code/words.txt'
data = requests.get(url)
print(data)
file = open('string.txt', 'r')