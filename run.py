from download_organizer.download_organizer import DownloadsOrganizer
from download_organizer.files_saver import FileSaver

if __name__ == '__main__':
    organizer = DownloadsOrganizer()
    print(organizer.categorice_files())