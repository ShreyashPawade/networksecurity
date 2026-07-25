import sys
from types import ModuleType
from networksecurity.logging import logger

class NetworkSecurityException(Exception):
    """
    Custom Exception class to capture file name, line number, 
    and exact error message for modular debugging.
    """
    def __init__(self, error_message: Exception, error_details: ModuleType):
        super().__init__(error_message)
        self.error_message = error_message
        
        # Capture the active traceback tuple: (type, value, traceback)
        _, _, exc_tb = error_details.exc_info()
        
        if exc_tb is not None:
            self.file_name = exc_tb.tb_frame.f_code.co_filename
            self.lineno = exc_tb.tb_lineno
        else:
            self.file_name = "Unknown File"
            self.lineno = "Unknown Line"

    def __str__(self) -> str:
        return (
            f"Error occurred in script: [{self.file_name}] "
            f"at line number: [{self.lineno}] | "
            f"Error message: [{str(self.error_message)}]"
        )
        

if __name__=='__main__':
    try:
        logger.logging.info("Enter the try block")
        a=1/0
        print("This will not be printed",a)
    except Exception as e:
           raise NetworkSecurityException(e,sys)