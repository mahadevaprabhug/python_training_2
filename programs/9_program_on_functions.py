"""
Write function to process web server log file

We will pass log file path as an argument to function
that function should read log file, extract info
then return extracted info in dictionary
"""

print("Function to process web server log file")
print("-"*20)
# --------------


def log_file_process_function(*, log_file_path):
    """
    function will read log file, extract info
    then return extracted info in dictionary
    :param log_file_path:
    :return dictionary:
    """

    # --------------
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

print("Calling Function")
print("-"*20)
# --------------

func_result = log_file_process_function(log_file_path=r"../log/web_server.log")
print("func_result:", func_result, end="\n\n")

print("#"*40, end="\n\n")
################################
