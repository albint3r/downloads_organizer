# Imports
import os
# Hint Types
from dataclasses import dataclass, field


@dataclass
class FileSaver:

    FILES_SAVE_DIRECTORIES = {'Images': ['.jpeg', '.gif', '.jpg', '.jfif', '.png'],
                              'Video': ['.mp4', '.mkv'],
                              'Audio': ['.mp3', '.WAV'],
                              'Text': ['.html', '.pdf', '.docx', '.pptx'],
                              'SpreedSheets': ['.csv', '.exe', '.xlsx'],
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

    def get_desktop_path(self, desktop_file: str = "~\Desktop"):
        self.desktop_root = os.path.expanduser(desktop_file)

    def get_downloads_path(self, download_file: str = '~\Downloads'):
        self.download_root = os.path.expanduser(download_file)

    def get_save_path(self, directory_name: str = 'organize_downloads'):
        self.save_downloads_root = os.path.join(self.desktop_root, directory_name)

    def exist_save_downloads_root(self) -> bool:
        return os.path.isdir(self.save_downloads_root)

    def create_new_save_download_files(self):
        if not self.exist_save_downloads_root():
            os.mkdir(self.save_downloads_root)
            print(f'Create {self.save_downloads_root}')

    def create_file_types_save_directories(self):
        for file_type in self.FILES_SAVE_DIRECTORIES:
            save_file_type_dir = os.path.join(self.save_downloads_root, file_type)
            if not os.path.isdir(save_file_type_dir):
                os.mkdir(save_file_type_dir)
                print(f'Create new directory -> {save_file_type_dir}')
