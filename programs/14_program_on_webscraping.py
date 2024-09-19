"""
Write 8th program to get data directly from website
and write to json file
"""

print("Get data from website and print")
print("-"*20)
# --------------

import urllib.request as u

my_web_file_handle = u.urlopen("https://www.jafsoft.com/searchengines/log_sample.html")
web_content = my_web_file_handle.read()
my_web_file_handle.close()

print(web_content)

print("#"*40, end="\n\n")
################################

print("Create object of beautifulsoup class")
print("-"*20)
# --------------

from bs4 import BeautifulSoup
soup = BeautifulSoup(web_content, 'html.parser')
print(soup)

print("#"*40, end="\n\n")
################################

print("log data")
print("-"*20)
# --------------

log_data = soup.body.pre.text
print(log_data)

print("#"*40, end="\n\n")
################################

print("type of log data")
print("-"*20)
# --------------

print(type(log_data))

print("#"*40, end="\n\n")
################################

print("log data in raw format")
print("-"*20)
# --------------

print(repr(log_data))

print("#"*40, end="\n\n")
################################

print("data in list")
print("-"*20)
# --------------

data_in_list = log_data.splitlines()
print(data_in_list)

print("#"*40, end="\n\n")
################################

print("Extract Info: Dictionary")
print("-"*20)
# --------------

# {
# 0: (ip, dt, img, url),
# 1: (ip, dt, img, url),
# 2: (ip, dt, img, url),
# 3: (ip, dt, img, url),
# 4: (ip, dt, img, url),
# 5: (ip, dt, img, url),
# }

extracted_info_dictionary = {}
index_no = 0
for each_line in data_in_list:
    if each_line.startswith('123'):
        sp = each_line.split()

        ip = sp[0]

        raw_date = sp[3]
        raw_date = raw_date[1:]
        index_of_colon = raw_date.index(":")
        dt = raw_date[:index_of_colon]

        raw_img = sp[6]
        if raw_img.startswith("/pics/"):
            img = raw_img[6:]
        else:
            img = "No Image"

        raw_url = sp[10]
        url = raw_url[1:-1]

        each_line_tuple = (ip, dt, img, url)
        extracted_info_dictionary[index_no] = each_line_tuple
        index_no += 1

print(extracted_info_dictionary)

# Example:
# >>> D = {}
# >>> type(D)
# <class 'dict'>
# >>>
# >>> D["A"] = 10
# >>> D[0] = 20
# >>> D
# {'A': 10, 0: 20}

print("#"*40, end="\n\n")
################################

print("Write to web_scrape_report.json")
print("-"*20)
# --------------

my_json_file_handle = open("web_scrape_report.json", "w")

import json
json.dump(extracted_info_dictionary, my_json_file_handle)

my_json_file_handle.close()

print("""
File 'web_scrape_report.json' created
""")

print("#"*40, end="\n\n")
################################
