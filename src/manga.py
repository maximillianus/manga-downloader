import time
import re
import os, sys
from pprint import pprint
import requests
from bs4 import BeautifulSoup
from dotenv import load_dotenv
load_dotenv()

# webpage = os.getenv('MANGASEE_MANGALIST')
# # manga = 'Tekken-Chinmi-Legends'
# manga = 'Shingeki-No-Kyojin'
# # manga = 'Nanatsu-No-Taizai'
# # manga = 'Hunter-X-Hunter'
# # manga = 'One-Piece'
# # manga = 'Boruto'

def check_latest_chapter(manga_name):
    """
    Input manga_name
    Get back 5 latest chapters of that manga
    """
    manga_webpage = os.getenv('MANGASEE_MANGALIST')
    uri = os.path.join(manga_webpage + manga_name)
    print(uri)
    response = requests.get(uri)
    if response.status_code != 200:
        print("Error during connection. Status code:", response.status_code)
        return []
    soup = BeautifulSoup(response.text, 'html.parser')
    latest_chapters_tags = soup.findAll('span',{'class':'chapterLabel'})
    latest_chapters = []
    for el in latest_chapters_tags[:5]:
        # print(el.text)
        latest_chapters.append(el.text)
    return latest_chapters

def download_chapter(manga_name, chapter):
    """
    Input manga and chapter
    Get that chapter saved in ~/Downloads/manga
    """
    chapter = str(chapter)
    manga_webpage = os.getenv('MANGASEE_MANGAREAD')
    uri = manga_webpage + manga_name + '-chapter-' + chapter + '.html'
    print(uri)
    response = requests.get(uri)
    if response.status_code != 200:
        return False
    soup = BeautifulSoup(response.text, 'html.parser')
    img_tags = soup.find_all('img')
    urls = [img['src'] for img in img_tags if 'src' in img.attrs.keys()]

    if not os.path.isdir('/Users/adityap/Downloads/manga/'+manga_name+'/'+chapter):
        os.makedirs('/Users/adityap/Downloads/manga/'+manga_name+'/'+chapter)
    os.chdir('/Users/adityap/Downloads/manga/'+manga_name+'/'+chapter)
    for url in urls:
        x = re.search('[0-9]*-[0-9]*\.(png|jpg)$', url)
        print(x)
        if x:
            chapter_page = x.group()
            with open(chapter_page, 'wb') as f:
                response = requests.get(url)
                f.write(response.content)
        else:
            print('chapter page image not found')



if __name__ == "__main__":
    # manga_name = 'Shingeki-No-Kyojin'
    if len(sys.argv) != 3:
        print('No manga or chapter provided')
        quit()

    manga_name = sys.argv[1]
    chapter_no = sys.argv[2]
    starttime = time.time()
    # latest_chapters = check_latest_chapter(manga_name=manga_name)
    # print('\n'.join(latest_chapters))
    download_chapter(manga_name, chapter_no)
    endtime = time.time()
    print('Total Time:', endtime-starttime)
