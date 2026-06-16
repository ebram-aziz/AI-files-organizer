# AI File Organizer

An AI-powered file organization tool that learns from your existing documents and automatically organizes newly downloaded files into the correct folders.

## Features

* Learns from your existing files
* Monitors the Downloads folder in real time
* Supports PDF, DOCX, and TXT files
* OCR support for scanned PDFs
* Uses Sentence Transformers and FAISS for semantic document classification
* Automatically moves files to the correct folder
* Configurable categories and destinations

## How It Works

1. Place existing documents inside category folders:

```text
training_data/
├── Physics/
├── Math/
├── ComputerScience/
```

2. Train the model:

```bash
python -m src.trainer
```

3. Start the organizer:

```bash
python main.py
```

4. New files downloaded to your Downloads folder are automatically classified and moved to the most relevant category.

## Configuration

### Define Categories

Edit:

```text
config/categories.json
```

Example:

```json
{
  "Physics": "D:/University/Physics",
  "Math": "D:/University/Math",
  "ComputerScience": "D:/University/ComputerScience"
}
```

### Set Downloads Folder

Edit:

```python
config/settings.py
```

```python
DOWNLOADS_FOLDER = r"C:/Users/YourName/Downloads"
```

## Technologies

* Sentence Transformers
* FAISS
* Watchdog
* Tesseract OCR
* PDFMiner

## Future Improvements

* GUI dashboard
* Active learning and retraining
* Additional file formats
* Cloud synchronization
