import re
import pytube

def youtube_url_validation(url):
    youtube_regex = (
        r'(https?://)?(www\.)?'
        '(youtube|youtu|youtube-nocookie)\.(com|be)/'
        '(watch\?v=|embed/|v/|.+\?v=)?([^&=%\?]{11})')

    youtube_regex_match = re.match(youtube_regex, url)
    if youtube_regex_match:
        return youtube_regex_match

    return youtube_regex_match

print("Enter link: ")

url=input()
m = youtube_url_validation(url)
if m:
    yt = pytube.YouTube(url)
    stream = yt.streams.first()
    stream.download()
else:
    print("Enter correct link")

