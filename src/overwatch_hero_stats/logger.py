import logging

class Logger:
    instance = None
    def __new__(cls):
        if cls.instance is None:
            cls.instance = super().__new__(cls)
            logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
            cls.instance.log = logging.getLogger()
        return cls.instance

    def __init__(self):
        self.log.debug("Logging Initialized")

    def error(self, msg, *args, **kwargs):
        self.log.error(msg, *args, **kwargs)
    
    def exception(self, msg, *args, **kwargs):
        self.log.exception(msg, *args, True, **kwargs)

    def warn(self, msg, *args, **kwargs):
        self.log.warning(msg, *args, **kwargs)
    
    def debug(self, msg, *args, **kwargs):
        self.log.debug(msg, *args, **kwargs)

    def info(self, msg, *args, **kwargs):
        self.log.info(msg, *args, **kwargs)

    def setHTTPLogLevel(self): # requests library
        logging.getLogger("requests").setLevel(logging.WARNING)
        logging.getLogger("urllib3").setLevel(logging.WARNING)