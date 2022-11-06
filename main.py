from bs4 import BeautifulSoup
import re
from selenium import webdriver
import time

if __name__ == '__main__':
    url = "https://www.twitch.tv/playapex/commandcenter"

    driver = webdriver.Chrome()
    driver.get(url)
    time.sleep(10)
    data = driver.page_source
    driver.close()

    soup = BeautifulSoup(data, features="html.parser")

    streams = {"NiceWigg": 'nicewigg'}
    ignoreList = ['playapex', 'bbl spanish', 'bbl portuguese',
                  'nicewigg b stream', 'rage japanese',
                  'maincast', 'fps thai', '4gamers mandarin ']

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

    # print('| Stream | URL |')
    # print('|-----|-----|')
    for name in streams:
        url = streams[name]
        # print(f'| {name} | https://www.twitch.tv/{url} |')

        print(f'streamlink https://www.twitch.tv/{url} best --output "/mnt/pool/tempdownloads/vods/ALGS PL2 Week 1/tosort/ALGS PL2 Week 1 - {name} - ' + '{time:%Y-%m-%d}.mkv" &>/dev/null &')

    print(len(streams))
