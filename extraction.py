import requests
from bs4 import BeautifulSoup
import pandas as pd
import os

URL = "https://www.project-a.com/en/portfolio"
DATA_DIR = "./data"
SAMPLED_DATA = os.path.join(DATA_DIR, "base_data/sampled_data.csv")

def extract_meta(meta_section):
    """Extracts info like name and title fact about the startup
    """
    headline = meta_section.find(class_="Headline").text
    print("Extracting Startup -> {}".format(headline))
    subline = meta_section.find(class_="Subhead").text
    return {"startup": headline, "title": subline}

def extract_facts(facts_section):
    """Extracts info like year of foundation, type of investment 
    """
    facts = dict()
    content_sections = facts_section.find_all("div", class_="KeyValue")
    for section in content_sections:
        key = section.find("div", class_="KeyValue__key").text.strip()
        value = section.find("p").text
        facts.update({key: value})

    return facts

def extract_description(description_section):
    """Extracts the detailed  description of the startup
    """
    description = description_section.find("p").text
    return {"description": description}

def get_portfolio_info(portfolio_section):
    """Extracts Portfolio info the startup which contains its information like Founded
        Type of Investement etc
    
    Arguments:
        portfolio_section {HTML_TAG} -- Div containing the portfolio_info of startup
    
    Returns:
        portfolio_info[dict] -- Returns dict with following info
                                1) Startup Meta 
                                2) Startup Facts
                                3) Startup Description

    """
    meta_section = portfolio_section.find(
        "div", class_="PortfolioDetailTemplate__header"
    )
    facts_section = portfolio_section.find(
        "div", class_="PortfolioDetailTemplate__facts"
    )
    description_section = portfolio_section.find("div", class_="Wysiwyg")

    meta = extract_meta(meta_section)
    facts = extract_facts(facts_section)
    description = extract_description(description_section)

    return {**meta, **facts, **description}

def get_social_media_info(social_media_section):
    """Extracts social media info of the startup
    
    Arguments:
        social_media_section {HTML_TAG} -- Div containing the social media info of startup
    
    Returns:
        social_media_info [dict] -- Returns dict with two keys 
                                    1) url - of the startup social
                                    2) media -  platform type (ex: twitter)
    """
    social_medias = social_media_section.find_all("a", class_="Social__link")
    social_media_info = dict()
    for social_media in social_medias:
        url = social_media["href"]
        media = social_media["aria-label"]
        social_media_info.update({media: url})

    return social_media_info

print("Extraction Starts ->")
with requests.Session() as session:  # maintaining a web-scraping session
    page = session.get(URL)
    soup = BeautifulSoup(page.content, "html.parser")
    content_section = soup.find("div", class_="Group js-Group")
    startup_links = content_section.select("div a")

    startup_data = list()
    for link in startup_links:
        href = link["href"]
        # Parsing startup_portfolis
        soup_ = BeautifulSoup(session.get(href).content, "html.parser")

        # Intrested Sections in the page
        portfolio_section = soup_.find("div", class_="PortfolioDetailTemplate__section")
        social_media_section = soup_.find("div", class_="Footer__social")
        # Extractors
        portfolio_info = get_portfolio_info(portfolio_section)
        social_media_info = get_social_media_info(social_media_section)
        
        startup_data.append({**portfolio_info, **social_media_info})

    print("Extraction Ends")
    startup_data_df = pd.DataFrame(startup_data)
    print("Saving Data to Disk")
    startup_data_df.to_csv(SAMPLED_DATA, index=False)
    print("Data Saved")
