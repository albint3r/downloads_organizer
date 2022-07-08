# Import
# Dates
import datetime
import datetime as dt
# System
import os
# Hint Types
from dataclasses import dataclass, field


@dataclass
class FileSaver:
    FILES_SAVE_DIRECTORIES = {'Images': ['.jpeg', '.gif', '.jpg', '.jfif', '.png'],
                              'Video': ['.mp4', '.mkv'],
                              'Audio': ['.mp3', '.WAV'],
                              'Text': ['.html', '.pdf', '.docx', '.pptx', '.opera'],
                              'SpreedSheets': ['.csv', '.xlsx'],
                              'Zip': ['.zip'],
                              'Others': None}

    desktop_root: str = field(init=False, repr=False)
    download_root: str = field(init=False, repr=False)
    save_downloads_root: str = field(init=False, repr=False)

    def __post_init__(self):
        self.get_desktop_path()
        self.get_downloads_path()
        self.get_save_path()
        self.create_new_save_download_files()
        self.create_file_types_save_directories()

    def create_new_save_download_files(self):
        if not self.exist_save_downloads_root():
            os.mkdir(self.save_downloads_root)
            print(f'Create targe root directory in your desktop -> {self.save_downloads_root}')

    def create_file_types_save_directories(self):
        for file_type in self.FILES_SAVE_DIRECTORIES:
            save_file_type_dir = os.path.join(self.save_downloads_root, file_type)
            if not os.path.isdir(save_file_type_dir):
                os.mkdir(save_file_type_dir)
                print(f'Create new directory -> {save_file_type_dir}')

    def create_category_month_directory(self, month_path: str) -> str:
        os.mkdir(month_path)

    @staticmethod
    def get_save_category_moth_dir(original_file: str, category_directory: str) -> str:
        month = FileSaver.get_original_file_save_month(original_file)
        return os.path.join(category_directory, month)

    def exist_save_downloads_root(self) -> bool:
        return os.path.isdir(self.save_downloads_root)

    def exist_category_month(self, category_month: str) -> bool:
        return os.path.isdir(category_month)

    def get_desktop_path(self, desktop_file: str = "~\Desktop"):
        self.desktop_root = os.path.expanduser(desktop_file)

    def get_downloads_path(self, download_file: str = '~\Downloads'):
        self.download_root = os.path.expanduser(download_file)

    def get_save_path(self, directory_name: str = 'organize_downloads'):
        self.save_downloads_root = os.path.join(self.desktop_root, directory_name)

    @staticmethod
    def get_original_file_save_month(original_file: str) -> str:
        unix_time = os.path.getmtime(original_file)
        date = dt.datetime.fromtimestamp(unix_time)
        return date.strftime('%b')
