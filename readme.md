# File Sorter

The File Sorter is a Python script for automatically sorting the files in a directory by their formats. It goes through each file in the directory and its subdirectories, identifies the file type based on its extension, and moves the file to a directory for that file type.

## Features

- Automatic file sorting based on the file extensions.
- Creation of directories (if they don't exist) for storing sorted files.
- Shows a progress bar indicating the progress of the sorting process.

## File Types

The script currently sorts files into the following categories:

- Videos
- Images
- Documents
- Music
- Archives
- Code
- Spreadsheets
- Others (for file types that don't fit into the above categories)

## Dependencies

The script depends on the following Python libraries:

- os
- shutil
- tqdm

## Usage

1. Install Python on your machine if you haven't already.
2. Make sure the dependencies are installed. You can install them using pip:

```
pip install tqdm
```

3. Open the script and replace `/path/to/files` in `directory_path = "/path/to/files"` at the end of the script with the path to the directory you want to sort.
4. Run the script in a Python environment:

```
python file_sorter.py
```

The script will sort all the files in the specified directory and its subdirectories.

## Note

The script moves the files to their respective directories. Ensure that you have a backup of the files in case anything goes wrong. You are solely responsible for any data loss.

## License

This project is open source and available under the [MIT License](LICENSE).

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change. Please make sure to update tests as appropriate.