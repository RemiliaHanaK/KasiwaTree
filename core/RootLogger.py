"""
core/RootLogger.py
Logs everything of this project
Copyright 2021 Stellestia1673
"""

import logging
import datetime

from logging.handlers import TimedRotatingFileHandler


class Logger(logging.Logger):
    def __init__(self, name, level=logging.INFO):
        super().__init__(name, level)
        self.logger = logging.getLogger(name)
        self.logger.setLevel(level)

    def setup(self):
        # [12:34:56.78 INFO] __main__: Kyouka is my waifu
        formatter = logging.Formatter("[%(asctime)s %(levelname)s] %(name)s: %(message)s", "%H:%M:%S.%m")

        file_handler = TimedRotatingFileHandler("./logs/log_{:%Y%m%d}".format(datetime.datetime.now()),
                                                when="midnight", backupCount=180, encoding="utf-8")
        file_handler.setFormatter(formatter)

        stream_handler = logging.StreamHandler()
        stream_handler.setFormatter(formatter)

        self.logger.addHandler(stream_handler)
        self.logger.addHandler(file_handler)

        return self.logger
