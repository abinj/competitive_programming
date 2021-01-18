import requests

r = requests.get('https://coderbyte.com/api/challenges/json/age-counting')
print(len(r.json()['data']))

data = r.json()['data']
count =0
for item in data.split(','):
    if 'age' in item:
        if(int(item.replace('age=', '')) >= 50):
            count += 1

print(count)
