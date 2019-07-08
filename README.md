# Manga Downloader

This is directory for scripts to download latest of my favourite manga.  

The ultimate goal for this app will be flask-based service that can check and download latest manga.  

However it will start as script for now with 3 functionality:  
- check latest manga
- download single chapter
- download multiple chapter

## Installation
1. clone this repository and go inside the repo directory (`cd manga-downloader`)
2. create virtualenv (*install virtualenv if you have not installed it*): `virtualenv venv`
3. install all required packages: `pip3 install -r requirements.txt`  

## Usage  
- Checking latest manga chapters:  
    `python3 check_latest_chapters.py <manga_name>`
- Download a single manga chapter:  
    `python3 download_chapter.py <manga_name> <chapter_no>`

##
