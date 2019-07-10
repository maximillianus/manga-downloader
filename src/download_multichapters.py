import sys
import time
from dotenv import load_dotenv
load_dotenv()

from manga import *

def main():
    if len(sys.argv) != 3:
        print('No manga or chapter provided')
        quit()

    manga_name = sys.argv[1]
    chapters = sys.argv[2]
    start_chapter = chapters.split('-')[0].strip()
    end_chapter = chapters.split('-')[1].strip()
    starttime = time.time()
    for chapter_no in range(int(start_chapter), int(end_chapter)+1):
        download_chapter(manga_name, chapter_no)
    endtime = time.time()
    print('Total Time:', endtime-starttime)

if __name__ == "__main__":
    main()