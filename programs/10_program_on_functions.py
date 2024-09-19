"""
ReWrite 9th program function to take multiple log files

like
log_file_process_function('log1.log', 'log2.log', 'log3.log')

then it should return result in
[dictionary_1, dictionary2, dictionary_3]

Our function looks like
# *log_file_paths : variable positional arguments
def log_file_process_function(*log_file_paths):
    code here
"""

print("Function to process web server log file")
print("-"*20)
# --------------


def main_log_file_process_function(*log_file_paths):
    """
    function will read log file, extract info
    then return extracted info in dictionary
    :param log_file_path:
    :return dictionary:
    """
    # log_file_paths = (path1, path2 etc.)

    extracted_info = []
    for each_file_path in log_file_paths:
        each_file_output = _extract_func(each_file_path)
        extracted_info.append(each_file_output)

    return extracted_info
    # --------------



def _extract_func(log_file_path):
    my_log_file_handle = open(log_file_path, "r")

    extracted_info_dictionary = {}
    index_no = 0

    for each_line in my_log_file_handle:
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

    my_log_file_handle.close()
    return extracted_info_dictionary
    # --------------

print("#"*40, end="\n\n")
################################

print("Calling function")
print("-"*20)
# --------------

func_result_1 = main_log_file_process_function("../log/web_server.log")
print("func_result_1:", func_result_1, sep="\n", end="\n\n")

func_result_2 = main_log_file_process_function("../log/web_server.log", "../log/web_server.log", "../log/web_server.log")
print("func_result_2:", func_result_2, sep="\n", end="\n\n")

print("#"*40, end="\n\n")
################################
