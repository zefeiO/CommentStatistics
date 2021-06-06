from asouler import Asouler
from comments import CommentsFetcher
import os

EmojiCharac = {
    "流汗黄豆": "😅",
    "愤怒黄豆": "😡",
    "笑哭黄豆": "🤣",
    "黄拳头": "👊",
    "白拳头": "👊🏻",
    "大哭黄豆": "😭",
    "给心心": "[给心心]",
    "愤怒恶魔": "👿",
    "口水黄豆": "🤤",
    "鲨鲨鲨": "🦈",
    "大哭": "[大哭]",
    "眼睛": "👀",
    "三心黄豆": "🥰",
    "双心黄豆": "😍",
    "单心黄豆": "😘",
    "摆手黄豆": "🤗",
    "润": "🏃",
    "害怕黄豆": "😰",
    "大笑": "😄",
    "寄吧": "🎤",
    "天使黄豆": "😇",
    "惊恐黄豆": "😱",
    "开香槟": "🍾",
    "奶瓶": "🍼",
    "生气": "[生气]",
    "舔爆": "👅",
    "失望黄豆": "😧",
    "我不好说卧槽": "🤭",
    "烧": "🥵",
    "跳舞": "💃",
    "高跟鞋": "👠",
    "击剑": "🤺",
    "哦呼": "[哦呼]",
    "狗头": "[doge]",
    "嘴硬": "[傲娇]",
    "笑哭": "[笑哭]",
    "抱拳": "[抱拳]",
    "无语": "[无语]",
    "嘉门": "[保佑]"
}


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
                for key, value in EmojiCharac:
                    if key in result:
                        result[key] += content.count()
                    else:
                        result[key] = content.count(value)
    
    print_ten_most_frequent(result)
    