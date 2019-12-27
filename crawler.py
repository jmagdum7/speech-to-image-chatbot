import numpy as np
import pandas as pd
import requests
from collections import defaultdict
import random
import regex
import pickle
from bs4 import BeautifulSoup

#crawler logic
def all_pages(base_url,data_dict):

    response = requests.get(base_url)
    print("url:"+base_url+"\n")
    soup = BeautifulSoup(response.text, "html.parser")
    try:
    	div_data = soup.find(id = "container")
    	data_dict[0] = {'url' : base_url,'title':soup.title.get_text(),'data' : div_data.get_text()} 
    except Exception as e:
    	pass
    unique_urls = {base_url}
    visited_urls = set()
    cnt = 0
    
    while len(unique_urls) > len(visited_urls):
    	cnt=cnt+1
    	print("total:"+str(len(unique_urls))+"\n")
    	print("visited:"+str(len(visited_urls))+"\n")
    	for link in soup.find_all("a"):
            try:
            	if "https://pict.edu/" in str(link["href"]) and "https://pict.edu/wp-content/" not in str(link["href"]) and "https://pict.edu/events/" not in str(link["href"]):
            		url = link["href"]
            		unique_urls.add(url)
            except:
                continue
            #absolute_url = base_url + url
            # unique_urls.add(url)

    	unvisited_url = (unique_urls - visited_urls).pop()
    	unique_urls.add(unvisited_url)
    	visited_urls.add(unvisited_url)
    	try:
    		response = requests.get(unvisited_url)
    	except Exception as e:
    		pass
    	print("url:"+unvisited_url+"\n")
    	soup = BeautifulSoup(response.text, "html.parser")
    	print("title:"+soup.title.get_text()+"\n")

    	try:
    		div_data = soup.find(id = "container")
    		div_title = soup.title.get_text()
    		data_dict[cnt] = {'url' : unvisited_url,'title' : div_title,'data' : div_data.get_text()}
    	except Exception as e:
    		pass
    return unique_urls



# base_url = "https://pict.edu/"
# data_dict = {}
# all_urls=all_pages(base_url,data_dict)

# print(data_dict)

# with open("data.pickle","wb") as f:
# 	pickle.dump(data_dict,f,protocol=pickle.HIGHEST_PROTOCOL)

with open("data.pickle","rb") as f:
	new_dict=pickle.load(f)

# print(new_dict)

for key,value in new_dict.items():
	print("url = "+value['url']+"\n")
	# print("data = "+value['data']+"\n")
	print("title = "+value['title']+"\n")

#parser output
with open("parser.pickle","rb") as f1:
	parse_string=pickle.load(f1)
print(parse_string)