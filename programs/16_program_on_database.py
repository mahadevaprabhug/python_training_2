"""
Write 15th program to send extracted data to database
"""

"""
How to use python to communicate with databases?

python-program <--Uses library to communicate -->  Any Databases (SQL/No-SQL)

Example:
python-program <--Uses library(cx-oracle) to communicate --> Oracle Databases
python-program <--Uses library(sqlite3) to communicate -->  SQLite Databases
"""

"""
We need one database
- We can use SQLite database
- lightweight, small database
- SQLite database is serverless database. database server not there
    it will create JUST 1 database file, on that file we can execute the query
"""

"""
How to create/communicate with SQLite database?

2 Options we have
Option-1: Using Sqlite software
Option-2: Without Using Sqlite software, using python library 'sqlite3'
        we can create/communicate with SQLite database
"""

print("Create database and table")
print("-"*20)
# --------------

import sqlite3

print("Creating/Connecting to database 'my_database.sqlite3'")
my_db_connection = sqlite3.connect('my_database.sqlite3')
print("Done\n")

print("Create cursor object")
my_db_cursor = my_db_connection.cursor()
print("Done\n")

print("run create table query ")
my_query = """
CREATE TABLE IF NOT EXISTS MY_TABLE(
IP VARCHAR(100),
PICS VARCHAR(100)
)
"""
my_db_cursor.execute(my_query)
print("Done\n")

print("#"*40, end="\n\n")
################################

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

print("Extract IP, PICS: Write to database")
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
        my_query = f"INSERT INTO MY_TABLE VALUES('{ip}', '{img}')"
        print("Executing Query:", my_query)
        my_db_cursor.execute(my_query)
        print("One record inserted\n")

my_db_connection.commit()
print("All records are inserted\n")

print("#"*40, end="\n\n")
################################

print("Get records from database")
print("-"*20)
# --------------

my_query = "SELECT * FROM MY_TABLE"
my_db_cursor.execute(my_query)
my_db_result = my_db_cursor.fetchall()
print(my_db_result)


print("#"*40, end="\n\n")
################################
