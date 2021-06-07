"""
main/__main__.py
Main part of project
Copyright 2021 Stellestia1673
"""

import time

from core.RootLogger import Logger
from utils.YamlLoader import YamlLoader
from discord.ext import commands
from core.ExtensionManager import ExtensionManager


class Main:
    def __init__(self, data):
        self.logger = Logger(__name__).setup()
        self.bot = commands.Bot(command_prefix=data["prefix"])
        self.data = data

    def run(self):
        ExtensionManager(self.bot).load_all()

        @self.bot.event
        async def on_connect():
            self.logger.info("Successfully established connection to Discord API server")

        @self.bot.event
        async def on_ready():
            self.logger.info(f"Logged in as \'{self.bot.user.name}\'({self.bot.user.id})")
            self.logger.info(f"Current version: {config['version']}")
            self.logger.info(f"Done! ({round(time.time() - timer, 3)}s)")

        self.bot.run(self.data["token"])  # └[∵┌]└[ ∵ ]┘[┐∵]┘


if __name__ == "__main__":
    timer = time.time()
    config = YamlLoader().load("config.yaml")

    Main(config).run()  # 凹[◎凸◎]凹 //System Online//
