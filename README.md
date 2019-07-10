# Manga Downloader

This is directory for scripts to download latest of my favourite manga.  

The ultimate goal for this app will be flask-based service that can check and download latest manga.  

However it will start as script for now with 3 functionality:  
- check latest manga
- download single chapter
- download multiple chapter

## Installation
0. Get python3 installed in your system. Please google how or check my `tech-how-to` repo.
1. clone this repository and go inside the repo directory (`cd manga-downloader`)
2. create virtualenv (*install virtualenv if you have not installed it*): `virtualenv venv`
3. install all required packages: `pip3 install -r requirements.txt`  

## Usage  
- Checking latest manga chapters:  
    `python3 check_latest_chapters.py <manga_name>`
    - Example: `python3 check_latest_chapters.py Boruto`
- Download a single manga chapter:  
    - `python3 download_chapter.py <manga_name> <chapter_no>`
    - Example: `python3 download_chapter.py Boruto 10`
- Download multiple manga chapter:
    - `python3 download_multichapters.py <manga_name> <chapter_no>`
    - Example: `python3 download_multichapters.py Boruto 10-12`
  
## Note
- I am using `.env` to store all my related environment variables (like `MANGADIR` for example). You can setup your own by creating a `.env` file and storing where you want to put your manga directory in `MANGADIR` variable.
- Same goes for my manga website. (I might disclose soon the website since my script possibly dependant on this website)