import requests
from bs4 import BeautifulSoup

# Send request to website and retrieve html

# Set the base URL for the forum
baseUrl = "https://forum.ucdcanoeclub.com/"

response = requests.get(baseUrl)
htmlContent = response.text

soup = BeautifulSoup(htmlContent, 'html.parser')

linkContainers = soup.find_all("tbody", class_="content")

for linkGroup in linkContainers:
    links = linkGroup.find_all("a", class_="subject")

    for link in links:
        href = link.get("href")
        print(href)

#https://forum.ucdcanoeclub.com/index.php/topic,13001.0.html


def ReadPage(url):

    response = requests.get(url)
    thisHtmlContent = response.text

    soup = BeautifulSoup(thisHtmlContent, "html.parser")

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

#ReadPage("https://forum.ucdcanoeclub.com/index.php/topic,13001.0.html")