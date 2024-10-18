import logging
import os


class LogGen:
    @staticmethod
    def loggen(log_file="Logs/automation.log"):
        """Generate a logger instance."""
        log_dir = os.path.dirname(log_file)
        if not os.path.exists(log_dir):
            os.makedirs(log_dir)

        logging.basicConfig(filename=log_file,
                            format='%(asctime)s: %(levelname)s: %(message)s',
                            datefmt='%m/%d/%Y %I:%M:%S %p',
                            level=logging.INFO)
        logger = logging.getLogger()
        return logger
