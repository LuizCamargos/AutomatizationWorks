import pyautogui
import time
import os
from pytube import Playlist, YouTube


def getMousePosition():
    while True:
        print(pyautogui.position())
        time.sleep(5)

    #Point(x=584, y=622)
    #Point(x=594, y=548)


listPlaylist = ['https://www.youtube.com/watch?v=s8lPbGlWd8A&list=PLqGkpApxFsX_jRp4sDFz9_gwztqqpDZ2U',
                'https://www.youtube.com/watch?v=an0JKXnnrAY&list=PL8D4Iby0Bmm9y57_K3vBvkZiaGjIXD_x5',
                'https://www.youtube.com/watch?v=hn-0iYnYVxE&list=PLegSxOLCWXO-WNcw-bN4CBXNoEJi3LhMy',
                'https://www.youtube.com/watch?v=AeSAPNnXlbE&list=PL1ABLQd6SasPzTrVmY2R-cuB5B3urz_h3',
                'https://www.youtube.com/watch?v=1sR0ol4IIPQ&list=PLyPCASkMblm5nn2FKsgK0uWwIhefp76m4',
                'https://www.youtube.com/watch?v=2-vUyRsOWFM&list=PL4vHRvN8o9BLxVImrigCE1UbFGbaEloGu',
                'https://www.youtube.com/watch?v=5vQ1IxKFN7M&list=PL_Q15fKxrBb6xsieff84zLNY012DKL6vP',
                'https://www.youtube.com/watch?v=oh14vu14Zzg&list=PLxENR_aD5W14AJUrOfT2aT5C2KINxta3l',
                'https://www.youtube.com/watch?v=uhiamj_I7II&list=PLdZzClTcgSlUnaDOeYrxtOF33CNYc6Iq4',
                'https://www.youtube.com/watch?v=9aspmIs2rzQ&list=PL-7NkxlnsDlWQuUmlNvVgjZVngpGoUal1',
                'https://www.youtube.com/watch?v=QwGasNuDXos&list=PLCwAHfhr-Gc8vQtjuZ7XU32B62yteWneO',
                'https://www.youtube.com/watch?v=qTPzUdKakSg&list=PLPGpGyS_bHMebbjZDrM2RxUjJDZGa3u1h',
                'https://www.youtube.com/watch?v=-xDniadTQsU&list=PLht7cktgZMlsTd5xp_jOfhyeDmnoECSSq',
                'https://www.youtube.com/watch?v=_pbW_eNGfj0&list=PLj5sti9SKXY7hGAGUyIUwrDtGYwudsMv9',
                'https://www.youtube.com/watch?v=d_jj_DNMNrk&list=PL9AqcOlfhzSxsFU2cByjWvSiz19N0incx',
                'https://www.youtube.com/watch?v=oKBiMU7Tbpo&list=PLZ2NmDB-REtG33PuZlA1EIU1oB6-Cceq-',
                'https://www.youtube.com/watch?v=MvnWXXmmxP4&list=PLXP07Q7Xyq-JuU4ylGlMZQZR8FH4QOWU9',
                'https://www.youtube.com/watch?v=cUe1ruryL-M&list=PLmdruITTb_26KWbvW1OhFVpao60sfErCk',
                'https://www.youtube.com/watch?v=5fHEcpO5IQQ&list=PL6SXrXPFRTivPkXcdHG3j70RFL8u5Qs2d',
                'https://www.youtube.com/watch?v=hn-0iYnYVxE&list=PLegSxOLCWXO-WNcw-bN4CBXNoEJi3LhMy',
                'https://www.youtube.com/watch?v=9aspmIs2rzQ&list=PL-7NkxlnsDlWQuUmlNvVgjZVngpGoUal1',
                'https://www.youtube.com/watch?v=qTPzUdKakSg&list=PLPGpGyS_bHMebbjZDrM2RxUjJDZGa3u1h',
                'https://www.youtube.com/watch?v=WDTksyMNEJ4&list=PLhw79wdYJhjY1yPulB2aGbL4VYijTBBtm',
                'https://www.youtube.com/watch?v=L49Jftq-VQk&list=PL173-xYCgMCp_xXaRBgVu4YjQCKR-aeCP',
                'https://www.youtube.com/watch?v=381Ikn82llg&list=PLjBECP3cDLBWkoJ3uloR4a4OHNsGMRddF',
                'https://www.youtube.com/watch?v=E2ZlcvsYBOM&list=PLD80GhQQHmK2ooNQlcfbSZtjSbUyPcMW8',
                'https://www.youtube.com/watch?v=4gJrtx-iuJk&list=PL9e-Hf6xO9DOGfgL3M8PgjLLcLcdXWwrM',
                'https://www.youtube.com/watch?v=exPFJVbIz0c&list=PLuKqxvDrOaoep8WV7qAzEootEMIg8uEr7',
                'https://www.youtube.com/watch?v=eXqBhDAlVCc&list=PL7tynfnzZQJBx8L1qtbiA0Fyv8tb5hD_y',
                'https://www.youtube.com/watch?v=IHgWjd_qL-o&list=PLb5RZZ4f08w85SVMPR8XoNGNXUHzJDOkm',
                'https://www.youtube.com/watch?v=_7tzXcXnclQ&list=PLgkJdTBnnFjOeDpdT7jEIUmwjRHGYp0C5',
                'https://www.youtube.com/watch?v=M7Cw7f6UMT8&list=PLFZ1H4GxYAaB6DEDULM4EUZxXfAHfNQiG',
                'https://www.youtube.com/watch?v=TGXkdU9S0OU&list=PL_DOYyKzBRhzH3kqjxJnEZ8WNDzyr-4pP',
                'https://www.youtube.com/watch?v=u7fUzLnA54I&list=PLcy1LU4PNItDSfgXK6I5cFJE3jQQ0iKDK',
                'https://www.youtube.com/watch?v=qTPzUdKakSg&list=PLPGpGyS_bHMebbjZDrM2RxUjJDZGa3u1h',
                'https://www.youtube.com/watch?v=hmwkRCFjs3Y&list=PL1B-dny5GoRCbtnGt6V6fJ5eJhXnaFVs3',
                'https://www.youtube.com/watch?v=s7kQCDSmalM&list=PLViJ5hcn5wMYr4FPQdvc5ITdy2gWxzR4U',
                'https://www.youtube.com/watch?v=GH1sbmoqXYQ&list=PLHeCj5b6VRfCYktwsLN5W886qa4QWkPlM',
                'https://www.youtube.com/watch?v=ArQA_uAVPac&list=PLB_03P59a2VrgCZFa53FLxSBUJ-286SBW',
                'https://www.youtube.com/watch?v=BfxYpj0Xo8w&list=PLDCFY7affEBS2UmSG4-Yg94cdsujXjpPG',
                'https://www.youtube.com/watch?v=T2ndwlq-x6g&list=PLObp3zV4FYJLv7RnCigW9XiJB2weVQl1_',
                'https://www.youtube.com/watch?v=KO-_h0gRWzc&list=PLYUGkfsByupW0jIabsaEe7c6RRl3z55VO',
                'https://www.youtube.com/watch?v=T1d_H875IXY&list=PLeyqPwWqnrfqmN4rCBbruLanYtbc9Q_7M',
                'https://www.youtube.com/watch?v=KO-_h0gRWzc&list=PLYUGkfsByupW0jIabsaEe7c6RRl3z55VO',
                'https://www.youtube.com/watch?v=XKcxmMx3hag&list=PL0VhexNGSwt5PHzqkBI_NULszE8Mt0zEh',
                'https://www.youtube.com/watch?v=pUMFrEJJlMQ&list=PLQopidRc3kQ-3eQ88GR0_wlUeELwyI8J7',
                'https://www.youtube.com/watch?v=QwGasNuDXos&list=PLCwAHfhr-Gc8vQtjuZ7XU32B62yteWneO',
                'https://www.youtube.com/watch?v=XsuA1Wa1dlc&list=PL6SLQSSfO-lYWnwQjCxzg-zf5r7xM1eq1',
                'https://www.youtube.com/watch?v=0LDGO6LX0D8&list=PLoyYoKEpKVGstiDWyuaks0T0zSEqJiFTw',
                'https://www.youtube.com/watch?v=7v4yjwZ9uPk&list=PLY-BfumRSziJGpy8Dpo7WY4nCQL0rAJE9',
                'https://www.youtube.com/watch?v=qG520Uw8lUA&list=PL8D4Iby0Bmm-uQIcbRfHeUMd_YDSZDA39',
                'https://www.youtube.com/watch?v=sPMA1tqWuf4&list=PL8D4Iby0Bmm94U_rwuJuocyC1xFoPTd5R']

for linkPlaylist in listPlaylist:
    print(linkPlaylist)
    playlist = Playlist(linkPlaylist)
    time.sleep(1)
    linkVideosDaPlaylist = []
    print('Number of videos in playlist: %s' % len(playlist.video_urls))
    var = playlist.video_urls
    indexBaixado = 0
    for linkVideo in linkVideosDaPlaylist:
        indexBaixado += 1
        try:
            YouTube(linkVideo).streams.first().download('C:\\VIDEOS\\KARAOKE')
            print(indexBaixado)
        except:
            print(indexBaixado*-1)
            pass
