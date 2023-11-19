import requests

user_name = input("Enter your name: ")
# user_name = "TalehIlqar"
# Making a GET request
r = requests.get(f'https://api.github.com/users/{user_name}')
if r.status_code == 200:
    # changing the format of response to json
    response = r.json()
    # print response of id
    print(response["avatar_url"])
elif r.status_code == 404:
    print("User not found")
else:
    print("Try again")
