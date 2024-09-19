"""
Get data from web_server.log file

then

pull
IP
DATE
PICS
URL

then

write extracted data to log_report.txt
"""
print("Get data from web_server.log file")
print("-"*20)
# --------------

my_log_file_handle = open(r"../log/web_server.log", "r")
log_file_content = my_log_file_handle.readlines()
my_log_file_handle.close()

print(log_file_content)

print("#"*40, end="\n\n")
################################

print("Extract Info and write to file")
print("-"*20)
# --------------

my_out_file_handle = open("log_report.txt", "w")
print("IP", "DATE", "PICS", "URL", sep="\t", file=my_out_file_handle)

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

        print(ip, dt, img, url, sep="\t", file=my_out_file_handle)

my_out_file_handle.close()

print("""
log_report.txt created. Please check
""")

print("#"*40, end="\n\n")
################################
