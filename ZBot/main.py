# Youtube video downloader...

from sre_constants import REPEAT
from pytube import YouTube


def main():
    print("""  ========================Youtube Audio and Video Downloader ==============================================
    **************************You can download the videos and audio in all Quality********************************
    Rules to Be follow:::::
    *******Choose the Number to work the Program=========
    1) Video Title 
    2) Thumbnail 
    3) Video ( To download Video )
    4) Audio ( To download Audio )
    =================================To re Run Program TYPE (yes)=======================================================

  """)
    a = int(input("Enter the number for using process===="))
    link = input("Give the link::")

    youtube_1 = YouTube(link)

    def my_fun():
        if a==3:
         videos = youtube_1.streams
        elif a==4:
            videos = youtube_1.streams.filter(only_audio=True)
        vido = list(enumerate(videos))
        for i in vido:
            print(i)
        print()
        srm = int(input("Enter the number to download videos=="))
        videos[srm].download()
        if a==3:
         print("Successfully Downloaded video...")
        elif a==4:
         print("Successfully Downloaded audio..")


    
    if a == 1:
        print(youtube_1.title)
    elif a == 2:
        print(youtube_1.thumbnail_url)
    elif a == 3:
        my_fun()
    elif a == 4:
        my_fun()
    else:
        print("failed")
    REPEAT = input("Would you like to run again==").lower()
    if REPEAT == 'yes':
        main()
    else:
        print("bye")
        exit()


main()
