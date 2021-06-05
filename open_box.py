from asouler import Asouler
from comments import CommentsFetcher

DIANA = "https://space.bilibili.com/672328094"
CAROL = "https://space.bilibili.com/351609538"
EILEEN = "https://space.bilibili.com/672342685"
BELLA = "https://space.bilibili.com/672353429"
AVA = "https://space.bilibili.com/672346917"

# Config
HOME = DIANA
DIR = "Diana"

def download_all():
    index = 1
    for link in waifu.video_links:
        video = CommentsFetcher(video_url=link)
        with open("./comments/" + DIR + "/" + index + ".txt", "wb") as f:
            f.write(video.get_full_html())
        index += 1

if __name__ == "__main__":
    waifu = Asouler(home_page=HOME)
    waifu.get_videos()

    # Download all html source codes (fully loaded)
    download_all()