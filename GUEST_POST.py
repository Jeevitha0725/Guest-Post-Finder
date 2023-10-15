import re
from bs4 import BeautifulSoup
import requests



def find_guest_post_sites():

    Details={"Website_Url":[],"GuestPost_URL":[]}
    urls = ['https://www.example.com/submit-a-guest-post','https://startup.info/top-niche-sites-to-submit-a-guest-post-for-free-now/','https://bloggerspassion.com/guest-posting-sites-list/','https://www.allbusiness.com/guest-post-overview','https://www.allbusiness.com/guest-post-overview']

    for url in urls:
        try:
            response = requests.get(url)
            soup = BeautifulSoup(response.content, 'html.parser')
            # Look for any anchor tags with text that matches a regular expression
            #print(soup.prettify())
            link=soup.find("a").get("href")
            Web=str(link).split("/")
            # print(Web[2])
            # print(link)
            Details["Website_Url"].append(Web[2])
            Details["GuestPost_URL"].append(link)
        except Exception as e:
            print("Error occurred while processing " + url + ": " + str(e))
    print(Details)

find_guest_post_sites()