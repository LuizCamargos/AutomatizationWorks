import pyautogui
import time
import os
from pytube import Playlist, YouTube
"""
while True:
    print(pyautogui.position())
    time.sleep(5)

#Point(x=584, y=622)
#Point(x=594, y=548)

"""


playlist = Playlist(
    'https://www.youtube.com/watch?v=pUMFrEJJlMQ&list=PLQopidRc3kQ-3eQ88GR0_wlUeELwyI8J7')
diretorio = "KARAOKE"
var = []
print('Number of videos in playlist: %s' % len(playlist.video_urls))
var = playlist.video_urls
a = 0
for i in var:
    a += 1
    try:
        YouTube(i).streams.first().download('C:\\videos\\'+diretorio)
        print(a)
    except:
        pass
# playlist.download_all('C:\\videos\\'+diretorio)
