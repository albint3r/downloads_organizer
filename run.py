from downloads_organizer.download_organizer import DownloadsOrganizer
from downloads_organizer.files_saver import FileSaver

if __name__ == '__main__':
    organizer = DownloadsOrganizer()
    organizer.move_download_files_to_targe_directory()