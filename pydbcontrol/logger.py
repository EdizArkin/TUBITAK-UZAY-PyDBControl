"""
Logger: Class that writes the operation history to a log file.
"""
import logging

class Logger:
    def __init__(self, log_file='pydbcontrol.log'):
        """
        Initializes the logger and sets up the log file.
        """
        self.logger = logging.getLogger('PyDBControlLogger')
        self.logger.setLevel(logging.INFO)
        fh = logging.FileHandler(log_file)
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        fh.setFormatter(formatter)
        self.logger.addHandler(fh)

    def log_action(self, action: str, detail: str = ""):
        """
        Logs the action and its details to the log file.
        """
        self.logger.info(f"{action}: {detail}")
