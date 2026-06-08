from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

from src.classifier import classify
from src.extractor import *
from src.ocr import ocr_pdf
from src.mover import move_file

import time

class DownloadHandler(FileSystemEventHandler):

    def on_created(self, event):

        if event.is_directory:
            return

        path = event.src_path

        text = ""

        if path.endswith(".pdf"):

            text = extract_pdf(path)

            if len(text.strip()) < 50:
                text = ocr_pdf(path)

        elif path.endswith(".docx"):
            text = extract_docx(path)

        elif path.endswith(".txt"):
            text = extract_txt(path)

        else:
            return

        category, score = classify(text)

        if score > 0.75:
            move_file(path, category)

def start_monitor(folder):

    observer = Observer()

    observer.schedule(
        DownloadHandler(),
        folder,
        recursive=False
    )

    observer.start()

    try:
        while True:
            time.sleep(5)

    except KeyboardInterrupt:
        observer.stop()

    observer.join()