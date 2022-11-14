from bs4 import BeautifulSoup
import re
from selenium import webdriver
import time

def getHTML(url):
    driver = webdriver.Chrome()
    driver.get(url)
    time.sleep(10)
    data = driver.page_source
    driver.close()

    return data

def getStreamUrls(soup, streams, ignoreList):
    buttons = soup.find_all("button", attrs={'data-target': True})
    for button in buttons:
        url = button['data-target']

        parent = button.parent
        name = parent.findChildren('div', recursive=False)[0]
        streamName = name.getText()

        streamName = re.sub("[\(\[].*?[\)\]]", "", streamName)
        streamName = streamName.replace("\n", "").strip()
        streamName = streamName[3::]

        if streamName.lower() not in ignoreList and url != 'playapex':
            streams[streamName] = url

    return streams

def printData(streams, table=False):

    if table:
        print('| Stream | URL |')
        print('|-----|-----|')

    for name in streams:

        url = streams[name]

        if table:
            print(f'| {name} | https://www.twitch.tv/{url} |')
        else:
            print(
                f'streamlink https://www.twitch.tv/{url} best --output "/mnt/pool/tempdownloads/vods/ALGS PL2 Week 1/tosort/ALGS PL2 Week 1 - {name} - ' + '{time:%Y-%m-%d}.mkv" &>/dev/null &')

    print(len(streams))

if __name__ == '__main__':
    url = "https://www.twitch.tv/playapex/commandcenter"
    streams = {"NiceWigg": 'nicewigg'}
    ignoreList = ['playapex', 'bbl spanish', 'bbl portuguese',
                  'nicewigg b stream', 'rage japanese',
                  'maincast', 'fps thai', '4gamers mandarin ']

    data = getHTML(url)

    soup = BeautifulSoup(data, features="html.parser")

    streams = getStreamUrls(soup, streams, ignoreList)

    printData(streams, False)
