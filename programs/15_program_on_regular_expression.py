"""
Write 14th program using regular expression extract information
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

print("Extract IP")
print("-"*20)
# --------------

import re

for each_line in data_in_list:
    match_result = re.match(r'(\d\d\d\.\d{3}\.\d{1,3}\.[0-9]{3}).*', each_line)
    # print("Each Line:", each_line)
    # print("match_result:", match_result, end="\n\n")
    if match_result is not None:
        # print("Each Line:", each_line)
        ip =match_result.group(1)
        print(ip)

# COMMENT
r"""
Regular Expression

IDENTIFIERS
----------
\d -> to tell any ONE digit b/n 0 to 9
\D -> to tell any ONE non-digit. except 0 to 9 any character
. -> to tell some character. ONE character
\. -> strictly DOT
[0-9] -> to tell any ONE digit b/n 0 to 9
----------

QUANTIFIERS
-----------
\d{3} -> \d\d\d
\d{1,3} -> minimum 1, maximum 3
-----------

MODIFIERS
-----------
* -> 0 or more times
+ -> 1 or more times
? -> 0 or 1 time
-----------

Grouping
- put () to IP address pattern
- this is called group
- each group as index starting from 1

"""

print("#"*40, end="\n\n")
################################

print("Extract IP, PICS: PARTIAL OUTPUT-1")
print("-"*20)
# --------------

import re

for each_line in data_in_list:
    match_result = re.match(r'(\d\d\d\.\d{3}\.\d{1,3}\.[0-9]{3}).*(GET|POST)\s+/pics/([a-zA-Z0-9_]+\.(gif|jpg)).*', each_line)
    if match_result is not None:
        ip = match_result.group(1)
        img = match_result.group(3)
        print(ip, img)

# COMMENT
r"""
\s -> One Space
\s+ -> one or more space
\S -> One Non-Space character, except space any characterx

[a-zA-Z0-9_] # which means, any one character present in this group of character

[a-zA-Z0-9_] -> shortcut \w
[^a-zA-Z0-9_] -> except these characters, shortcut \W
"""

print("#"*40, end="\n\n")
################################

print("Extract IP, PICS: FINAL OUTPUT")
print("-"*20)
# --------------

import re

for each_line in data_in_list:
    match_result = re.match(r'(\d\d\d\.\d{3}\.\d{1,3}\.[0-9]{3}).*(GET|POST)\s+/(pics/([a-zA-Z0-9_]+\.(gif|jpg)))?.*', each_line)
    if match_result is not None:
        ip = match_result.group(1)
        img = match_result.group(4)
        if img is None:
            img = "No Image"
        print(ip, img)

# COMMENT
r"""
Make 'pics/wpaper.gif' pattern optional so that
lines which is not having pics also captured

(pics/([a-zA-Z0-9_]+\.(gif|jpg)))?

"""

print("#"*40, end="\n\n")
################################
