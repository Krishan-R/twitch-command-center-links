from bs4 import BeautifulSoup

if __name__ == '__main__':

    file = open('parse.html', 'r')
    soup = BeautifulSoup(file.read(), features="html.parser")

    streams = {"NiceWigg": 'nicewigg'}
    ignoreList = ['playapex', 'bbl spanish', 'bbl portuguese',
                  'nicewigg b stream', 'rage japanese',
                  'maincast', 'fps thai', '4gamers mandarin ']

    buttons = soup.find_all("button", attrs={'data-target': True})
    for button in buttons:
        children = button.findChildren("img", attrs={'alt': True})
        url = button['data-target']
        streamName = children[0]['alt'][3::]
        if streamName.lower() not in ignoreList and url != 'playapex':
            streams[streamName] = url

    # print('| Stream | URL |')
    # print('|-----|-----|')
    for name in streams:
        url = streams[name]
        # print(f'| {name} | https://www.twitch.tv/{url} |')

        print(f'streamlink https://www.twitch.tv/{url} best --output "/mnt/pool/aDownloads/vods/ALGS Championships/tosort/ALGS Championships Raleigh - {name} Finals - ' + '{time:%Y-%m-%d}.mkv" &>/dev/null &')

    print(len(streams))
