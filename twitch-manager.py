#!/usr/bin python3
import subprocess
import sys

downloadList = [
    'streamlink https://www.twitch.tv/nicewigg best --output "/mnt/MX5001TB/ALGS Year 2 Playoff 2 London/Day 4/Finals/ALGS London Playoff 2 Finals - NiceWigg - {time:%Y-%m-%d}.mkv" &>/dev/null &',
    'streamlink https://www.twitch.tv/telnach_febbcdehfjih best --output "/mnt/MX5001TB/ALGS Year 2 Playoff 2 London/Day 4/Finals/ALGS London Playoff 2 Finals - ACEND - {time:%Y-%m-%d}.mkv" &>/dev/null &',
    'streamlink https://www.twitch.tv/telnach_febbccfhdaaf best --output "/mnt/MX5001TB/ALGS Year 2 Playoff 2 London/Day 4/Finals/ALGS London Playoff 2 Finals - Alliance - {time:%Y-%m-%d}.mkv" &>/dev/null &',
    'streamlink https://www.twitch.tv/telnach_febbcdbfjabf best --output "/mnt/MX5001TB/ALGS Year 2 Playoff 2 London/Day 4/Finals/ALGS London Playoff 2 Finals - LG Chivas - {time:%Y-%m-%d}.mkv" &>/dev/null &',
    'streamlink https://www.twitch.tv/telnach_febbcdafdecf best --output "/mnt/MX5001TB/ALGS Year 2 Playoff 2 London/Day 4/Finals/ALGS London Playoff 2 Finals - PULVEREX - {time:%Y-%m-%d}.mkv" &>/dev/null &',
    'streamlink https://www.twitch.tv/telnach_febbcdhfedcd best --output "/mnt/MX5001TB/ALGS Year 2 Playoff 2 London/Day 4/Finals/ALGS London Playoff 2 Finals - FaZe - {time:%Y-%m-%d}.mkv" &>/dev/null &',
    'streamlink https://www.twitch.tv/telnach_febbcdbidbdb best --output "/mnt/MX5001TB/ALGS Year 2 Playoff 2 London/Day 4/Finals/ALGS London Playoff 2 Finals - NRG - {time:%Y-%m-%d}.mkv" &>/dev/null &',
    'streamlink https://www.twitch.tv/telnach_febbcddhcacf best --output "/mnt/MX5001TB/ALGS Year 2 Playoff 2 London/Day 4/Finals/ALGS London Playoff 2 Finals - RIDDLE ORDER - {time:%Y-%m-%d}.mkv" &>/dev/null &',
    'streamlink https://www.twitch.tv/telnach_febbcdecjgad best --output "/mnt/MX5001TB/ALGS Year 2 Playoff 2 London/Day 4/Finals/ALGS London Playoff 2 Finals - DarkZero - {time:%Y-%m-%d}.mkv" &>/dev/null &',
    'streamlink https://www.twitch.tv/telnach_febbciaedafc best --output "/mnt/MX5001TB/ALGS Year 2 Playoff 2 London/Day 4/Finals/ALGS London Playoff 2 Finals - MAP - {time:%Y-%m-%d}.mkv" &>/dev/null &',
    'streamlink https://www.twitch.tv/telnach_febbcdddefid best --output "/mnt/MX5001TB/ALGS Year 2 Playoff 2 London/Day 4/Finals/ALGS London Playoff 2 Finals - Moist Esports - {time:%Y-%m-%d}.mkv" &>/dev/null &',
    'streamlink https://www.twitch.tv/telnach_febbcdfegehd best --output "/mnt/MX5001TB/ALGS Year 2 Playoff 2 London/Day 4/Finals/ALGS London Playoff 2 Finals - Pioneers - {time:%Y-%m-%d}.mkv" &>/dev/null &',
    'streamlink https://www.twitch.tv/telnach_febbcefaebae best --output "/mnt/MX5001TB/ALGS Year 2 Playoff 2 London/Day 4/Finals/ALGS London Playoff 2 Finals - Fire Beavers - {time:%Y-%m-%d}.mkv" &>/dev/null &',
    'streamlink https://www.twitch.tv/telnach_febbccegfbfb best --output "/mnt/MX5001TB/ALGS Year 2 Playoff 2 London/Day 4/Finals/ALGS London Playoff 2 Finals - Oxygen Esports - {time:%Y-%m-%d}.mkv" &>/dev/null &',
    'streamlink https://www.twitch.tv/telnach_febbccdfecae best --output "/mnt/MX5001TB/ALGS Year 2 Playoff 2 London/Day 4/Finals/ALGS London Playoff 2 Finals - FNATIC - {time:%Y-%m-%d}.mkv" &>/dev/null &',
    'streamlink https://www.twitch.tv/telnach_febbcdciefjf best --output "/mnt/MX5001TB/ALGS Year 2 Playoff 2 London/Day 4/Finals/ALGS London Playoff 2 Finals - TSM - {time:%Y-%m-%d}.mkv" &>/dev/null &',
    'streamlink https://www.twitch.tv/telnach_febbcdjheajd best --output "/mnt/MX5001TB/ALGS Year 2 Playoff 2 London/Day 4/Finals/ALGS London Playoff 2 Finals - FC destroy - {time:%Y-%m-%d}.mkv" &>/dev/null &',
    'streamlink https://www.twitch.tv/telnach_febbcbadchaa best --output "/mnt/MX5001TB/ALGS Year 2 Playoff 2 London/Day 4/Finals/ALGS London Playoff 2 Finals - XSET - {time:%Y-%m-%d}.mkv" &>/dev/null &',
    'streamlink https://www.twitch.tv/telnach_febbccafebib best --output "/mnt/MX5001TB/ALGS Year 2 Playoff 2 London/Day 4/Finals/ALGS London Playoff 2 Finals - OpTic Gaming - {time:%Y-%m-%d}.mkv" &>/dev/null &',
    'streamlink https://www.twitch.tv/telnach_febbcccbgibb best --output "/mnt/MX5001TB/ALGS Year 2 Playoff 2 London/Day 4/Finals/ALGS London Playoff 2 Finals - BLVKHVND - {time:%Y-%m-%d}.mkv" &>/dev/null &',
    'streamlink https://www.twitch.tv/telnach_febbcdigjbac best --output "/mnt/MX5001TB/ALGS Year 2 Playoff 2 London/Day 4/Finals/ALGS London Playoff 2 Finals - 100 Thieves - {time:%Y-%m-%d}.mkv" &>/dev/null &',
]


def GetStreams():
    output = subprocess.run(['ps', 'aux'], stdout=subprocess.PIPE)
    processList = output.stdout.decode('utf-8').split('\n')

    twitchStreams = []
    for process in processList:
        if "streamlink" in process:
            twitchStreams.append(process)

    return twitchStreams


def CountStreams():
    print(len(GetStreams()))


def PrintStreams():
    for stream in GetStreams():
        print(stream)

    print(GetDownloadList())


def GetDownloadList():
    currentlyDownloading = []
    for stream in GetStreams():
        stream = stream.split("twitch.tv/")
        stream = stream[1].split(" ")
        streamName = stream[0]
        currentlyDownloading.append(streamName)

    currentlyDownloading.sort()

    return currentlyDownloading


def FindMissing():

    currentlyDownloading = GetDownloadList()

    missingList = []
    for stream in downloadList:
        stream = stream.split(" ")
        stream = stream[1].split("/")
        streamName = stream[-1]
        if streamName not in currentlyDownloading:
            missingList.append(streamName)

    print(f"Missing Streams: {missingList}")


if __name__ == '__main__':

    match sys.argv[1]:
        case "count":
            CountStreams()
        case "print":
            PrintStreams()
        case "missing":
            FindMissing()
        case other:
            print("unknown command")
            print("count, print, missing are available commands")
