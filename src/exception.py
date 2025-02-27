import sys
import logging
import src.logger

def error_message_detail(error, error_detail: sys):
    """
    Extracts detailed error message, including filename, line number, and error message.
    """
    _, _, exc_tb = error_detail.exc_info()  # Correct method to retrieve exception details
    file_name = exc_tb.tb_frame.f_code.co_filename
    error_message = "Error occurred in python script: [{0}], line number: [{1}], error message: [{2}]".format(
        file_name, exc_tb.tb_lineno, str(error)
    )
    return error_message  # Correct placement of return statement


class CustomException(Exception):
    def __init__(self, error_message, error_detail: sys):
        """
        Custom Exception class to format detailed error messages.
        """
        super().__init__(error_message)  # Correct way to call the parent class constructor
        self.error_message = error_message_detail(error_message, error_detail)

    def __str__(self):
        return self.error_message
    
