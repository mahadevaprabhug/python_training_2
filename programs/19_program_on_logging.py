"""
ReWrite 12th program to capture the log
"""

print("Configure logger")
print("-"*20)
# --------------

import logging

my_logger = logging.getLogger(__name__)

logging.basicConfig(filename='my_19th_program_log.log', filemode="w" ,level=logging.DEBUG, format="%(levelname)s : %(asctime)s : %(filename)s : %(message)s")

print("#"*40, end="\n\n")
################################


print("Testing our logger")
print("-"*20)
# --------------

my_logger.info("This is info")
my_logger.debug("This is debug")
my_logger.warning("This is warning")
my_logger.error("This is error")
my_logger.critical("This is critical")

print("#"*40, end="\n\n")
################################

print("Read data from 'log_report_3.json'")
print("-"*20)
# --------------

try:
    my_logger.info("Opening file")
    my_json_file_handle = open("log_report_3.json", "r")
    my_logger.info("Opening file completed")
except FileNotFoundError as msg:
    my_logger.error(f"Not able open json file: Reason- {msg}")
    my_logger.error("Exiting")
    exit()
else:
    try:
        my_logger.info("importing json library")
        import json
        my_logger.info("importing json library completed")
    except ModuleNotFoundError as msg:
        my_logger.error(f"Not able import json Reason:{msg}")
        my_logger.error("Exiting")
        exit()
    else:
        try:
            my_logger.info("Reading json file content")
            json_file_content = json.load(my_json_file_handle)
            my_logger.info("Reading json file content completed")
        except Exception as msg:
            my_logger.error(f"Not able read json file, Reason:{msg}")
            my_logger.error("Exiting")
            exit()
finally:
    try:
        my_logger.info("Closing file handle")
        my_json_file_handle.close()
        my_logger.info("Closing file handle completed")
    except Exception as msg:
        my_logger.error(f"Not able close file handle, Reason:{msg}")
        my_logger.error("Exiting")
        exit()

print("json_file_content:", json_file_content)
print("type of json_file_content:", type(json_file_content))

print("#"*40, end="\n\n")
################################

print("Write to 'log_report_4.txt'")
print("-"*20)
# --------------

my_logger.info("Writing log_report_4.txt started")

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

my_logger.info("Writing log_report_4.txt completed")

print("""
log of this program captured in 'my_19th_program_log.log'
please check
""")

print("#"*40, end="\n\n")
################################
