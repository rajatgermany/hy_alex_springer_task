# hy_alex_springer_task
Scrapper to scrap startup data from https://www.project-a.com/en/portfolio. 
It extracts info like startup founded year , its category , investement type etc


## Task1

## Requirements
- python >=3.5
- pip = python package manager

## Setup
- git clone git@github.com:rajatgermany/hy_alex_springer_task.git
- cd hy_alex_springer_task
- pip install -r requirements.txt
- Run in order
  -  python extraction.py -  Web extraction script
  -  python transformer.py -  Transformers the extracted data
  -  python analysis.py - Generates the statistics of number of startups founded in each year



## Technical Details
 - extraction.py 
   - It uses python request libary to made a http request. 
   - Uses Beautiful soup to parse the html
   
 - transformer.py 
   - It has two processing .
      - Formatted Founded year column
      - Reorded the columns
 - analysis.py
    - it has function to generate the statistics of number of startups founded  each year
    
## Task2
  - Designed the solution for scalable web scraper
 
## Task3 
  - Performed the naive analysis of investor startup-matching

