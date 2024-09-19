"""
Read data from 'log_report_3.json'

then

write log_report_4.txt file

Expected Output in log_report_4.txt should be similar to log_report.txt

"""

print("Read data from 'log_report_3.json'")
print("-"*20)
# --------------

my_json_file_handle = open("log_report_3.json")

import json
json_file_content = json.load(my_json_file_handle)

my_json_file_handle.close()

print("json_file_content:", json_file_content)
print("type of json_file_content:", type(json_file_content))

print("#"*40, end="\n\n")
################################

print("Write to 'log_report_4.txt'")
print("-"*20)
# --------------

my_txt_file_handle = open("log_report_4.txt", "w")
print("IP", "DATE", "PICS", "URL", sep="\t", file=my_txt_file_handle)

for i, j, k, l in json_file_content.values():
    print(i, j, k, l, sep="\t", file=my_txt_file_handle)

my_txt_file_handle.close()

print("""
Created log_report_4.txt file
please check
""")

print("#"*40, end="\n\n")
################################
