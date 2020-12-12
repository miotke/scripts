import json
import requests

"""
A quick and simple script to read some data from
a web API and parse json.
"""

def main():
    response = requests.get('https://jsonplaceholder.typicode.com/posts')
    posts = json.loads(response.text)

    for i in posts:
        user = "userId"
        title = i["title"]
        body = i["body"]

        if i[user] == 2:
            print(f"{user}\n")
            print(f"Title:{title}\nBody:{body}\n")



if __name__ == '__main__':
    main()
