import requests
from bs4 import BeautifulSoup

# Send request to website and retrieve html

# Set the base URL for the forum
baseUrl = "https://forum.ucdcanoeclub.com/"

response = requests.get(baseUrl)
htmlContent = response.text

soup = BeautifulSoup(htmlContent, 'html.parser')

# Find all links on the page
links = soup.find_all('a')

# Loop through each link and follow it to other pages on the forum
for link in links:
    # Get the URL for the link
    href = link.get('href')

    if 'forum.ucdcanoeclub.com/' in href:
        print(href)

#https://forum.ucdcanoeclub.com/index.php/topic,13001.0.html


def ReadPage():
    soup = BeautifulSoup(html_content, "html.parser")

    # Get title
    forumTopic = soup.find("title").text

    # Extract information
    posts = soup.find_all("div", class_="postarea")
    posters = soup.find_all("div", class_="poster")


    print(f"Topic: {forumTopic}\n")

    for post, poster in zip(posts, posters):

        author = poster.find("a").text
        authorTitle = poster.find("li", class_="title").text
        
        date = post.find(class_="smalltext").text

        body = post.find(class_="inner").text

        print(f"Post by {author}, {authorTitle}, {date}:\n{body}\n")