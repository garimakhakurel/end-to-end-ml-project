#writing own custom exception
import sys

def error_message_detail(error, error_detail:sys):
    _,_,exc_tb = error_detail.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename

    error_message = "Error occurred in Python script name[{0}]; line number [{1}]; error message [{2}]".format(
        file_name, exc_tb.tb_lineno, str(error)
    )
    return error_message
    

#creating a custom exception class that is inheriting from parent exception
class CustomException(Exception):
    def __init__(self, error_message, error_detail:sys): #defining constructor
        super().__init__(error_message) #inheriting the init function
        self.error_message = error_message_detail(error_message,error_detail=error_detail)

    def __str__(self):
        return self.error_message
    
