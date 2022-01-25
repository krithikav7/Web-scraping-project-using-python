import requests
from bs4 import BeautifulSoup
import pprint

res = requests.get('https://news.ycombinator.com/')
res2 = requests.get('https://news.ycombinator.com/news?p=2')
soup = BeautifulSoup(res.text, 'html.parser')
soup2 = BeautifulSoup(res2.text, 'html.parser')


links = soup.select('.titlelink')
subtext = soup.select('.subtext')
links2 = soup2.select('.titlelink')
subtext2 = soup2.select('.subtext')

mega_links = links + links2
mega_subtext = subtext + subtext2


def sorted_votes_hnlist(hnlist):
    return sorted(hnlist, key=lambda k: k['votes'], reverse=True)


def custom_hn(link, text):
    hn = []
    for idx, item in enumerate(link):
        title = item.getText()
        href = item.get('href', None)
        vote = text[idx].select('.score')
        if len(vote):
            points = int(vote[0].getText().replace(' points', ''))
            if points > 99:
                hn.append({'title': title, 'link': href, 'votes': points})
    return sorted_votes_hnlist(hn)


pprint.pprint(custom_hn(mega_links, mega_subtext))
