import os
import math
import random
import datetime

#OS - file system operations
print("Current working directory:", os.getcwd())
files=os.listdir('.')
print("Files in current directory:", files)
os.makedirs('test_dir', exist_ok=True)

#Math - mathematical functions
print("Square root of 16:", math.sqrt(16))
print("Value of pi:", math.pi)
print("Cosine of 0:", math.cos(0))

#Random - random number generation
print("Random integer between 1 and 10:", random.randint(1, 10))
print("Random choice from list:", random.choice(['apple', 'banana', 'cherry']))

#Datetime - date and time manipulation
now = datetime.datetime.now()
print("Current date and time:", now)
print("Current year:", now.year)
print("Current month:", now.month)
print("Current day:", now.day)
print("Current hour:", now.hour)
print("Current minute:", now.minute)
print("Current second:", now.second)
print("Current date:", now.date())
print("Current time:", now.time())
print("Current weekday:", now.strftime("%A"))
print("Current month name:", now.strftime("%B"))
print("Current day name:", now.strftime("%A"))
print("Current date and time in ISO format:", now.isoformat())
print("Current date and time in custom format:", now.strftime("%Y-%m-%d %H:%M:%S"))
print("Current date and time in UTC:", datetime.datetime.utcnow())

#json - JSON serialization and deserialization
import json
data = {'name': 'Alice', 'age': 30, 'city': 'New York'}
json_string = json.dumps(data)
print("JSON string:", json_string)
parsed_data = json.loads(json_string)
print("Parsed data:", parsed_data)
print("Name:", parsed_data['name'])
print("Age:", parsed_data['age'])
print("City:", parsed_data['city'])