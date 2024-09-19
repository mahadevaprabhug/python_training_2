"""
From the given string,
extract

IP
DATE
PICS
URL

Expected Output:
---------------
123.123.123.123
26/Apr/2000
wpaper.gif
http://www.jafsoft.com/asctortf/
---------------
"""

print("input data")
print("-"*20)
# --------------

input_data = '123.123.123.123 - - [26/Apr/2000:00:23:48 -0400] "GET /pics/wpaper.gif HTTP/1.0" 200 6248 "http://www.jafsoft.com/asctortf/" "Mozilla/4.05 (Macintosh; I; PPC)"'
print(input_data)

print("#"*40, end="\n\n")
################################

print("input data in RAW FORMAT")
print("-"*20)
# --------------

input_data = '123.123.123.123 - - [26/Apr/2000:00:23:48 -0400] "GET /pics/wpaper.gif HTTP/1.0" 200 6248 "http://www.jafsoft.com/asctortf/" "Mozilla/4.05 (Macintosh; I; PPC)"'
print(repr(input_data))

print("#"*40, end="\n\n")
################################

print("input data type")
print("-"*20)
# --------------

input_data = '123.123.123.123 - - [26/Apr/2000:00:23:48 -0400] "GET /pics/wpaper.gif HTTP/1.0" 200 6248 "http://www.jafsoft.com/asctortf/" "Mozilla/4.05 (Macintosh; I; PPC)"'
print(type(input_data))

print("#"*40, end="\n\n")
################################

print("Extract IP: 1- WAY")
print("-"*20)
# --------------

input_data = '123.123.123.123 - - [26/Apr/2000:00:23:48 -0400] "GET /pics/wpaper.gif HTTP/1.0" 200 6248 "http://www.jafsoft.com/asctortf/" "Mozilla/4.05 (Macintosh; I; PPC)"'

ip = input_data[0:15]
print(ip)

print("#"*40, end="\n\n")
################################

print("Extract IP: 2- WAY")
print("-"*20)
# --------------

input_data = '123.123.123.123 - - [26/Apr/2000:00:23:48 -0400] "GET /pics/wpaper.gif HTTP/1.0" 200 6248 "http://www.jafsoft.com/asctortf/" "Mozilla/4.05 (Macintosh; I; PPC)"'

index_of_1st_space = input_data.index(" ")

ip = input_data[0:index_of_1st_space]
print(ip)

print("#"*40, end="\n\n")
################################

print("Extract IP: 3- WAY")
print("-"*20)
# --------------

input_data = '123.123.123.123 - - [26/Apr/2000:00:23:48 -0400] "GET /pics/wpaper.gif HTTP/1.0" 200 6248 "http://www.jafsoft.com/asctortf/" "Mozilla/4.05 (Macintosh; I; PPC)"'

sp = input_data.split()
print("Splited Values:", sp, sep="\n", end="\n\n")

ip = sp[0]
print(ip)

print("#"*40, end="\n\n")
################################

print("Extract DATE")
print("-"*20)
# --------------

input_data = '123.123.123.123 - - [26/Apr/2000:00:23:48 -0400] "GET /pics/wpaper.gif HTTP/1.0" 200 6248 "http://www.jafsoft.com/asctortf/" "Mozilla/4.05 (Macintosh; I; PPC)"'

sp = input_data.split()
print("Splited Values:", sp, sep="\n", end="\n\n")

raw_date = sp[3] # '[26/Apr/2000:00:23:48'

# Remove [
raw_date = raw_date[1:] # '26/Apr/2000:00:23:48'

index_of_colon = raw_date.index(":")
dt = raw_date[:index_of_colon]
print(dt)

print("#"*40, end="\n\n")
################################

print("Extract PICS")
print("-"*20)
# --------------

input_data = '123.123.123.123 - - [26/Apr/2000:00:23:48 -0400] "GET /pics/wpaper.gif HTTP/1.0" 200 6248 "http://www.jafsoft.com/asctortf/" "Mozilla/4.05 (Macintosh; I; PPC)"'

sp = input_data.split()
print("Splited Values:", sp, sep="\n", end="\n\n")

raw_img = sp[6] # '/pics/wpaper.gif'

# 1-WAY to remove /pics/ from '/pics/wpaper.gif'
img_1 = raw_img[6:]

# 2-WAY to remove /pics/ from '/pics/wpaper.gif'
img_2 = raw_img.removeprefix("/pics/")

print(img_1, img_2, sep="\n")

print("#"*40, end="\n\n")
################################

print("Extract URL")
print("-"*20)
# --------------

input_data = '123.123.123.123 - - [26/Apr/2000:00:23:48 -0400] "GET /pics/wpaper.gif HTTP/1.0" 200 6248 "http://www.jafsoft.com/asctortf/" "Mozilla/4.05 (Macintosh; I; PPC)"'

sp = input_data.split()
print("Splited Values:", sp, sep="\n", end="\n\n")

raw_url = sp[10] # '"http://www.jafsoft.com/asctortf/"'

url = raw_url[1:-1]
print(url)

print("#"*40, end="\n\n")
################################
