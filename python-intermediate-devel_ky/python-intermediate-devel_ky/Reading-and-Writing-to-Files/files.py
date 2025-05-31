import json

name = input("Enter your name: ")

with open("message.json", "r") as file:
    data = json.load(file)
    print(data['Hobby'])



