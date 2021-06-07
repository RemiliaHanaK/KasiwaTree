"""
core/ExtensionManager.py
Manage command modules
Copyright 2021 Stellestia1673
"""

import os

from core.RootLogger import Logger
import discord.ext.commands.errors as e


class ExtensionManager:
    def __init__(self, bot):
        self.logger = Logger(__name__).setup()
        self.bot = bot

    def load(self, filename):
        try:
            self.bot.load_extension(f"modules.{filename}")
        except ModuleNotFoundError:
            self.logger.warning(f"Failed to load \'{filename}\': \n"
                                f"ModuleNotFoundError: No class that inherits commands.Cog")
            return False
        except e.ExtensionAlreadyLoaded:
            self.logger.warning(f"Module \'{filename}\' is already loaded")
            return False
        except Exception:
            self.logger.error("Unexpected error has occured", exc_info=True)
            return False
        else:
            self.logger.info(f"Successfully loaded module \'{filename}\'")
            return True

    def load_all(self):
        for filename in os.listdir("./modules"):
            if filename.endswith(".py") and not filename.startswith("_"):
                self.load(filename[:-3])

        self.logger.info(f"{len(self.bot.cogs)} modules have been loaded")

    def unload(self, filename):
        try:
            self.bot.unload_extension(f"modules.{filename}")
        except e.ExtensionNotLoaded:
            self.logger.warning(f"Module \'{filename}\' has not been loaded")
            return False
        else:
            self.logger.info(f"Unloaded module \'{filename}\'")
            return True

    def unload_all(self):
        for extension in self.bot.cogs.keys():
            self.unload(extension)

        self.logger.info("All modules have been unloaded")

    def reload(self, filename):
        self.logger.info(f"Reloading module \'{filename}\'...")
        if self.unload(filename) is False:
            return False
        if self.load(filename) is False:
            return False
        return True

    def reload_all(self):
        self.logger.info(f"Reloading all modules...")
        self.unload_all()
        self.load_all()
