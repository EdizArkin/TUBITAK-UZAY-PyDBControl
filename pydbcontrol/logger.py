"""
Logger: İşlem geçmişini log dosyasına yazan sınıf.
"""
import logging

class Logger:
    def __init__(self, log_file='pydbcontrol.log'):
        """
        Log dosyasını başlatır.
        """
        self.logger = logging.getLogger('PyDBControlLogger')
        self.logger.setLevel(logging.INFO)
        fh = logging.FileHandler(log_file)
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        fh.setFormatter(formatter)
        self.logger.addHandler(fh)

    def log_action(self, action: str, detail: str = ""):
        """
        İşlem ve detayını loglar.
        """
        self.logger.info(f"{action}: {detail}")
