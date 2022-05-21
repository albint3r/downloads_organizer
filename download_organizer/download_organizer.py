# Imports
import os
# Hint Types
from dataclasses import dataclass, field
# Modules Project
from download_organizer.files_saver import FileSaver


@dataclass
class DownloadsOrganizer:

    download_files: list = field(init=False, repr=False)
    save: FileSaver = field(init=False, repr=False, default_factory=FileSaver)

    def __post_init__(self):
        self.extract_downloads_files(self.save.download_root)

    def extract_downloads_files(self, download_root):
        self.download_files = os.listdir(download_root)

    def categorice_files(self):
        for file in self.download_files:
            name, file_ext = os.path.splitext(file)
            print(name, file_ext)


if __name__ == '__main__':
    organizer = DownloadsOrganizer()
