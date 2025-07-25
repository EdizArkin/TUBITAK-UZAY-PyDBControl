"""
Logger: Class that writes the operation history to a log file.
"""

import os
import logging

class Logger:
    def __init__(self, log_file='logs/pydbcontrol.log'):
        """
        Initializes the logger and sets up the log file.
        Ensures the log file is always created inside the logs/ directory.
        """
        try:
            # Always use logs/ as the directory
            logs_dir = 'logs'
            if not os.path.exists(logs_dir):
                os.makedirs(logs_dir)
            # If user gave just a filename, prepend logs/
            log_file_name = os.path.basename(log_file)
            log_file_path = os.path.join(logs_dir, log_file_name)
            self.logger = logging.getLogger('PyDBControlLogger')
            self.logger.setLevel(logging.INFO)
            fh = logging.FileHandler(log_file_path)
            formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
            fh.setFormatter(formatter)
            self.logger.addHandler(fh)
        except Exception as e:
            print(f"Logger setup error: {e}")

    def log_action(self, action: str, detail: str = ""):
        """
        Logs the action and its details to the log file.
        Catches and prints user-friendly error messages if logging fails.
        """
        try:
            self.logger.info(f"{action}: {detail}")
        except Exception as e:
            print(f"Logger error: {e}")

    def get_log(self):
        """
        Returns the contents of the log file as a string.
        Catches and prints user-friendly error messages if reading fails.
        """
        try:
            for handler in self.logger.handlers:
                if isinstance(handler, logging.FileHandler):
                    log_file = handler.baseFilename
                    with open(log_file, 'r', encoding='utf-8') as f:
                        return f.read()
            return "No log file handler found."
        except Exception as e:
            print(f"Error reading log file: {e}")
            return ""

    def print_log(self):
        """
        Prints the contents of the log file to the terminal.
        """
        try:
            for handler in self.logger.handlers:
                if isinstance(handler, logging.FileHandler):
                    log_file = handler.baseFilename
                    with open(log_file, 'r', encoding='utf-8') as f:
                        print(f.read())
                    return
            print("No log file handler found.")
        except Exception as e:
            print(f"Error reading log file: {e}")

    def clear_log(self):
        """
        Clears the contents of the log file.
        Catches and prints user-friendly error messages if clearing fails.
        """
        try:
            for handler in self.logger.handlers:
                if isinstance(handler, logging.FileHandler):
                    log_file = handler.baseFilename
                    with open(log_file, 'w', encoding='utf-8') as f:
                        f.write("")
                    print("Log file cleared.")
                    return
            print("No log file handler found.")
        except Exception as e:
            print(f"Error clearing log file: {e}")