import shutil
import json
import os

def move_file(source, category):

    with open("config/categories.json") as f:
        categories = json.load(f)

    destination = categories[category]

    os.makedirs(destination, exist_ok=True)

    shutil.move(
        source,
        os.path.join(
            destination,
            os.path.basename(source)
        )
    )