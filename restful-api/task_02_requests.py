import requests
import csv


def fetch_and_print_posts():
    """
    Fetch posts from JSONPlaceholder API and print their titles.
    """
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)

    print(f"Status Code: {response.status_code}")

    if response.status_code == 200:
        posts = response.json()
        for post in posts:
            print(post['title'])


def fetch_and_save_posts():
    """
    Fetch posts from JSONPlaceholder API and save them to a CSV file.
    """
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)

    if response.status_code == 200:
        posts = response.json()
        post_list = [
            {
                'id': post['id'],
                'title': post['title'],
                'body': post['body']
            }
            for post in posts
        ]

        with open("posts.csv", mode='w', newline='', encoding='utf-8') as file:
            writer = csv.DictWriter(file, fieldnames=["id", "title", "body"])
            writer.writeheader()
            writer.writerows(post_list)
