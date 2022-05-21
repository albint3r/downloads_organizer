# Import
# Dates
import datetime
import datetime as dt
# System
import os
import shutil
# Hint Types
from dataclasses import dataclass, field
# Modules Project
from downloads_organizer.files_saver import FileSaver


@dataclass
class DownloadsOrganizer:
    download_files: list = field(init=False, repr=False)
    save: FileSaver = field(init=False, repr=False, default_factory=FileSaver)

    def __post_init__(self) -> None:
        self.extract_downloads_files(self.save.download_root)

    @staticmethod
    def create_target_save_directory(save_directory: str, file_name: str, extension: str) -> str:
        return os.path.join(save_directory, f'{file_name}{extension}')

    def extract_downloads_files(self, download_root: str) -> None:
        self.download_files = os.listdir(download_root)

    def get_split_download_files(self) -> list[tuple]:
        return list(map(os.path.splitext, self.download_files))

    def get_original_file_location(self, file_name: str, extension: str) -> str:
        return os.path.join(self.save.download_root, f'{file_name}{extension}')

    def get_targe_category_month_directory(self, original_file_location: str, file_name: str, extension: str) -> str:
        category_dir = self.get_save_category_directory(extension)
        category_month_dir = self.save.get_save_category_moth_dir(original_file_location, category_dir)
        if not self.save.exist_category_month(category_month_dir):
            self.save.create_category_month_directory(category_month_dir)
            print(f'Create new Targe Category Month Directory -> {category_month_dir}')
        return os.path.join(category_month_dir, f'{file_name}{extension}')

    def get_save_category_directory(self, extension: str) -> str:
        if extension in self.save.FILES_SAVE_DIRECTORIES.get('Images'):
            return os.path.join(self.save.save_downloads_root, 'Images')

        if extension in self.save.FILES_SAVE_DIRECTORIES.get('Video'):
            return os.path.join(self.save.save_downloads_root, 'Video')

        if extension in self.save.FILES_SAVE_DIRECTORIES.get('Audio'):
            return os.path.join(self.save.save_downloads_root, 'Audio')

        if extension in self.save.FILES_SAVE_DIRECTORIES.get('Text'):
            return os.path.join(self.save.save_downloads_root, 'Text')

        if extension in self.save.FILES_SAVE_DIRECTORIES.get('SpreedSheets'):
            return os.path.join(self.save.save_downloads_root, 'SpreedSheets')

        if extension in self.save.FILES_SAVE_DIRECTORIES.get('Zip'):
            return os.path.join(self.save.save_downloads_root, 'Zip')

        else:
            return os.path.join(self.save.save_downloads_root, 'Others')

    def move_download_files_to_targe_directory(self):
        for file, ext in self.get_split_download_files():
            original_file_location = self.get_original_file_location(file, ext)
            final_save_path = self.get_targe_category_month_directory(original_file_location, file, ext)
            shutil.copyfile(original_file_location, final_save_path)


if __name__ == '__main__':
    organizer = DownloadsOrganizer()
