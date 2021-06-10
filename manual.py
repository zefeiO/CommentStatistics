from comments import CommentsFetcher

if __name__ == "__main__":
    link = input("Enter the url: ")
    index = str(input("Enter the index for the file: "))
    video = CommentsFetcher(video_url=link)
    with open("./comments/Diana/" + index + ".txt", "w", encoding="utf-8") as f:
        f.write(video.get_full_html())