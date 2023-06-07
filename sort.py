import os
import shutil
from tqdm import tqdm

def sort_files_by_format(directory):
    total_files = sum([len(files) for _, _, files in os.walk(directory)])
    progress_bar = tqdm(total=total_files, unit='file(s)')

    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)

            # Get the file extension
            _, ext = os.path.splitext(file)
            ext = ext.lower()  # Convert the extension to lowercase for comparison

            # Create the output directories if they don't exist
            video_dir = os.path.join(directory, 'Videos')
            image_dir = os.path.join(directory, 'Images')
            doc_dir = os.path.join(directory, 'Documents')
            music_dir = os.path.join(directory, 'Music')
            archive_dir = os.path.join(directory, 'Archives')
            code_dir = os.path.join(directory, 'Code')
            spreadsheet_dir = os.path.join(directory, 'Spreadsheets')
            other_dir = os.path.join(directory, 'Others')
            os.makedirs(video_dir, exist_ok=True)
            os.makedirs(image_dir, exist_ok=True)
            os.makedirs(doc_dir, exist_ok=True)
            os.makedirs(music_dir, exist_ok=True)
            os.makedirs(archive_dir, exist_ok=True)
            os.makedirs(code_dir, exist_ok=True)
            os.makedirs(spreadsheet_dir, exist_ok=True)
            os.makedirs(other_dir, exist_ok=True)

            # Move the file to the appropriate directory based on the extension
            if ext in ['.mp4', '.avi', '.mkv']:
                shutil.move(file_path, os.path.join(video_dir, file))
            elif ext in ['.jpg', '.jpeg', '.png', '.gif']:
                shutil.move(file_path, os.path.join(image_dir, file))
            elif ext in ['.txt', '.pdf', '.doc', '.docx']:
                shutil.move(file_path, os.path.join(doc_dir, file))
            elif ext in ['.mp3', '.wav', '.flac']:
                shutil.move(file_path, os.path.join(music_dir, file))
            elif ext in ['.zip', '.rar', '.7z']:
                shutil.move(file_path, os.path.join(archive_dir, file))
            elif ext in ['.py', '.java', '.cpp', '.c', '.h']:
                shutil.move(file_path, os.path.join(code_dir, file))
            elif ext in ['.xls', '.xlsx', '.csv']:
                shutil.move(file_path, os.path.join(spreadsheet_dir, file))
            else:
                shutil.move(file_path, os.path.join(other_dir, file))

            progress_bar.update(1)

    progress_bar.close()
    print("Files sorted successfully!")

# Provide the directory path where the files are located
directory_path = "D:/recovery"

sort_files_by_format(directory_path)
