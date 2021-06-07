"""
core/YamlLoader.py
Loads YAML file
Copyright 2021 Stellestia1673
"""

import os
import sys
import yaml

from core.RootLogger import Logger


class YamlLoader:
    def __init__(self):
        self.logger = Logger(__name__).setup()

    def load(self, path):
        if not os.path.isfile(path):
            self.logger.fatal(f"\'{path}\' not found")
            sys.exit()
        else:
            with open(path) as file:
                try:
                    data = yaml.load(file, Loader=yaml.FullLoader)
                except yaml.YAMLError:
                    self.logger.fatal("Unexpected error has occured: ", exc_info=True)
                    sys.exit()
                else:
                    self.logger.info(f"Successfully loaded \'{path}\' file")
                    return data
