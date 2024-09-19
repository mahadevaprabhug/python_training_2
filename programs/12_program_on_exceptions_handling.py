"""
Write 7th program with handling exceptions
"""

print("Read data from 'log_report_3.json'")
print("-"*20)
# --------------

try:
    my_json_file_handle = open("log_report_3.json", "r")
except FileNotFoundError as msg:
    print("Not able open json file: Reason-",msg)
    print("Exiting")
    exit()
else:
    try:
        import json
    except ModuleNotFoundError as msg:
        print("Not able import json Reason:", msg)
        print("Exiting")
        exit()
    else:
        try:
            json_file_content = json.load(my_json_file_handle)
        except Exception as msg:
            print("Not able read json file, Reason:", msg)
            print("Exiting")
            exit()
finally:
    try:
        my_json_file_handle.close()
    except Exception as msg:
        print("Not able close file handle, Reason:", msg)
        print("Exiting")
        exit()

print("json_file_content:", json_file_content)
print("type of json_file_content:", type(json_file_content))

print("#"*40, end="\n\n")
################################

print("Write to 'log_report_4.txt'")
print("-"*20)
# --------------

try:
    my_txt_file_handle = open("log_report_4.txt", "w")
    print("IP", "DATE", "PICS", "URL", sep="\t", file=my_txt_file_handle)

    for i, j, k, l in json_file_content.values():
        print(i, j, k, l, sep="\t", file=my_txt_file_handle)

    my_txt_file_handle.close()

    print("""
    Created log_report_4.txt file
    please check
    """)

except Exception as msg:
    print("Not able to complete write operations. Reason:", msg)

print("#"*40, end="\n\n")
################################
