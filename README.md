# DM - simple script for music and video install

## requsted :
- [yt-dlp](https://github.com/yt-dlp/yt-dlp) (install bin file and add in path)
- [python](https://www.python.org/) (for running script)

DM - without installing the file on the computer, [yt-dlp](https://github.com/yt-dlp/yt-dlp) DM in turn allows you not to write prefexes every time, and contains prefexes,
by default they are in the configuration file 'config.json' which is generated automatically in the directory of the executable file

## Config tutorial
DM uses a JSON file to describe methods and flags, and your can's creat own your's custom methods and flags, it's not so hard.

In base config have a two masse: "music" and "video", this masse have's a flag varibale, in this varibale descripted, a flag for called a custom prefix
example :
  "flag" : "m"
  dm m # runing dm an m flag
on DM running, script run a masse "music", and use a "prefix" in masse "music"
example :
  "prefix" : "-x --audio-format mp3 --embed-thumbnail --embed-metadata"
You can's read all [yt-dlp prefix list](https://github.com/yt-dlp/yt-dlp)
