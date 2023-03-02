import requests, re, json
from bs4 import BeautifulSoup


# specify the url of the website to scrape
url = 'https://www.sitytrail.com/fr/'

# send a GET request to the website
response = requests.get(url)

# parse the html content of the website using Beautiful Soup
soup = BeautifulSoup(response.content, 'html.parser')
# find all meta tags in the html content
meta_tags = soup.find_all('meta')

# create an empty list to store the metadata
metadata_list = []

# loop through each meta tag and store its content in the metadata list
for meta_tag in meta_tags:
    # check if the meta tag has a 'name' attribute
    if meta_tag.has_attr('name'):
        metadata_list.append((meta_tag['name'], meta_tag.get('content')))
    # check if the meta tag has a 'property' attribute
    if meta_tag.has_attr('twitter*'):
        metadata_list.append((meta_tag['property'], meta_tag.get('content')))

# print the metadata list
print(metadata_list)
print("-----")

# for each row in metadata_list we get the tuple in result
for i in range(len(metadata_list)):
    result=metadata_list[i]
    j=""
    #if result contains the substring then create a JSON object
    if "twitter" in result[0].lower():
        print(metadata_list[i])
        j=json.dumps({result[0] : result[1]},sort_keys=True,indent=4)



