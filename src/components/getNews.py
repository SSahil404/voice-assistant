from GoogleNews import GoogleNews
import random

googlenews = GoogleNews()
googlenews.search("INDIA")
result = googlenews.result()

newsTitle = []
for x in result:
    newsTitle.append(x['title'])


def news():
    return random.choice(newsTitle)
