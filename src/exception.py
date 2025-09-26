''' for exeception handling'''
# sys library helps us to manipulate python runtime environment
import sys 

# Whenever any exception occurs this eror will be raised 
def error_message_detail(error, error_detail):
    # exc_info() returns a tuple of three values that gives information about the exception that is currently being handled.
    _,_,exc_tb = error_detail.exc_info()
    # Getting the line number where exception occured
    line_number = exc_tb.tb_lineno
    file_name = exc_tb.tb_frame.f_code.co_filename
    error_message  = "Error occured in python script name [{0}] line number [{1}] error message [{2}]".format(
        file_name, line_number, str(error)

    )
    return error_message
    
class CustomException(Exception):
    def __init__(self, error_message, error_detail):
        super().__init__(error_message)
        self.error_message = error_message_detail(error_message, error_detail)

    def __str__(self):
        return str(self.error_message)
    