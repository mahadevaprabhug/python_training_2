"""
Write class 'LogProcessClass' with below functionality

L1 = Log_Process_Class("../log/web_server.log")
ips_list = L1.get_ips()
all_list = L1.get_all()
L1.to_json("log_report_6.json") # This shuld create json file
"""

print("LogProcessClass:")
print("-"*20)
# --------------

class LogProcessClass:
    def __init__(self, log_file_path):
        my_log_file_handle = open(log_file_path, "r")
        self.log_file_content = my_log_file_handle.readlines()
        my_log_file_handle.close()

    def get_ips(self):
        extracted_info_list = []
        for each_line in self.log_file_content:
            if each_line.startswith('123'):
                sp = each_line.split()
                ip = sp[0]
                extracted_info_list.append(ip)
        return extracted_info_list

    def get_all(self):
        extracted_info_list = []
        for each_line in self.log_file_content:
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
                extracted_info_list.append(each_line_tuple)
        return extracted_info_list

    def to_json(self, json_file_path):
        # Get all records
        extracted_info_list = self.get_all()

        # Write to json file
        my_json_file_handle = open(json_file_path, "w")
        import json
        json.dump(extracted_info_list, my_json_file_handle)
        my_json_file_handle.close()

print("#"*40, end="\n\n")
################################

print("Using LogProcessClass")
print("-"*20)
# --------------

my_object_1 = LogProcessClass("../log/web_server.log")
ips_list = my_object_1.get_ips()
all_records = my_object_1.get_all()
my_object_1.to_json("log_report_6.json")
print("Created log_report_6.json file please check")

my_object_2 = LogProcessClass("../log/web_server.log")
ips_list = my_object_2.get_ips()
all_records = my_object_2.get_all()
my_object_2.to_json("log_report_7.json")
print("Created log_report_7.json file please check")

print("#"*40, end="\n\n")
################################
