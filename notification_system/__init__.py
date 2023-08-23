from pathlib import Path
WORKDIR = Path('.').absolute()


path_to_db_with_files = Path.joinpath(WORKDIR.parent.absolute(), 'db')
path_to_db_with_files.mkdir(exist_ok=True)

path_to_db_with_sensors_file = Path.joinpath(path_to_db_with_files, 'sensors')
path_to_db_with_sensors_file.mkdir(exist_ok=True)

from notification_system.converters.files_creator_controller import FilesCreatorController

FilesCreatorController.PATH_TO_FILE_DB = path_to_db_with_sensors_file