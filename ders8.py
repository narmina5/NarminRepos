# TASKS (DAY 9):
# 01
import requests

url = "https://api.publicapis.org/entries"

r = requests.get(url)

if r.status_code == 200:
    response = r.json()
    print(response)
else:
    print(f"Error: Failed to fetch data. Status code: {r.status_code}")

# 02
url = "https://api.coindesk.com/v1/bpi/currentprice.json"
output_file = "test.txt"

try:
    r = requests.get(url)

    if r.status_code == 200:
        response = r.text

        with open(output_file, "w") as file:
            file.write(response)

        print(f"Data saved to {output_file}")
    else:
        print(f"Error: Failed to fetch data. Status code: {r.status_code}")
except Exception as e:
    print(f"An error occurred: {e}")

# 03
# ?

# 04
# ?

# 05
country = input("Enter the country name: ")

url = f"http://universities.hipolabs.com/search?country={country}"
r = requests.get(url)


if r.status_code == 200:
    universities_data = r.json()

    if len(universities_data) > 0:
        file_name = f"{country.lower()}_uni.txt"
        with open(file_name, "w", encoding="utf-8") as file:
            for university in universities_data:
                file.write(f"Name: {university['name']}\n")
                file.write(f"Country: {university['country']}\n")
                file.write(f"Web Page: {university['web_pages'][0]}\n")
                file.write("\n")

        print(f"University information saved to {file_name}")
    else:
        print(f"There are no universities in {country}.")
else:
    print(f"Error: There is no country with the name '{country}' or no universities found in that country.")

