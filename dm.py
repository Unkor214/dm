import os , json, re

from sys import argv
from pathlib import Path

#config read func (-_-)
def configRead() :
    try :
        #trying read config "config.json" in main file dir )
        with open(Path(__file__).resolve().parent/"config.json", "r") as json_config :
            config = json.load(json_config) #loding config.json in config
    except FileNotFoundError :
        #el file not found (
        print("error - config file not found\ncreat - new config file")

        #writing file
        with open(Path(__file__).resolve().parent/"config.json", "w") as json_config :
            json_config.write() #creat null json file
    
    return config

#main func ^^
def main() :
    config = configRead()

    for custom_obj in config :
        if config[custom_obj]["flag"] in argv :
            for flags in argv :
                if re.search(r"^http", flags) :
                    url = flags
                    break
            os.system(f"yt-dlp {config[custom_obj]["prefix"]} {url}")

if __name__ == "__main__" :
    main()