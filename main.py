from src.monitor import start_monitor
from config.settings import DOWNLOADS_FOLDER

if __name__ == "__main__":

    start_monitor(str(DOWNLOADS_FOLDER))