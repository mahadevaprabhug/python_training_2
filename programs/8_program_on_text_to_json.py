"""
Get data from web_server.log file

then

pull
IP
DATE
PICS
URL

then

Obtain dictionary

then

write dictionary to log_report_5.json
"""

print("Get data from web_server.log file")
print("-"*20)
# --------------

my_log_file_handle = open("../log/web_server.log")
log_file_content = my_log_file_handle.readlines()
my_log_file_handle.close()

print(log_file_content)

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
for each_line in log_file_content:
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

print("Write to log_report_5.json")
print("-"*20)
# --------------

my_json_file_handle = open("log_report_5.json", "w")

import json
json.dump(extracted_info_dictionary, my_json_file_handle)

my_json_file_handle.close()

print("""
File 'log_report_5.json' created
""")

print("#"*40, end="\n\n")
################################
