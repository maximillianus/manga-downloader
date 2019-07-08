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
    chapter_no = sys.argv[2]
    starttime = time.time()
    download_chapter(manga_name, chapter_no)
    endtime = time.time()
    print('Total Time:', endtime-starttime)

if __name__ == "__main__":
    main()