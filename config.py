"""
Module for configuration of the application
"""
import os
import dotenv

dotenv.load_dotenv()


TG_TOKEN = os.getenv("TG_TOKEN")
