from asouler import Asouler
from comments import CommentsFetcher
import os
from config import Config

# Config
HOME = Config.DIANA
DIR = "Diana"

def download_all():
    index = 1
    for link in waifu.video_links:
        video = CommentsFetcher(video_url=link)
        with open("./comments/" + DIR + "/" + index + ".txt", "w") as f:
            f.write(video.get_full_html())
        index += 1

def get_max_key(result: dict):
    return max(result, key=result.get)

def print_ten_most_frequent(result: dict):
    i = 0
    while i < 10:
        max_key = get_max_key(result)
        print(max_key + ": " + result.pop(max_key))
        i += 1

if __name__ == "__main__":
    waifu = Asouler(home_page=HOME)
    waifu.get_videos()

    # Download all html source codes (fully loaded)
    download_all()

    # Count the number of each emoji found in files
    result = dict()
    for root, dirs, files in os.walk("./comments/" + DIR):
        for name in files:
            with open(os.path.join(root, name), "r") as f:
                content = f.read()
                for key, value in Config.EmojiCharac:
                    if key in result:
                        result[key] += content.count(value)
                    else:
                        result[key] = content.count(value)
    
    print_ten_most_frequent(result)
    