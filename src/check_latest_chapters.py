import sys
import time

from dotenv import load_dotenv
load_dotenv()

from manga import check_latest_chapter


def main():
    if len(sys.argv) != 2:
        print('No manga provided')
        quit()

    manga_name = sys.argv[1]
    starttime = time.time()
    latest_chapters = check_latest_chapter(manga_name)
    print('Latest chapters:', '\n'.join(latest_chapters))
    endtime = time.time()
    print('Total Time:', endtime-starttime)

if __name__ == "__main__":
    main()