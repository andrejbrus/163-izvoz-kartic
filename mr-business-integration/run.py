from sys import argv, exit

from mrbi import download_activities, report_group_by, generate_download_filename, test_trello
from mrbi.config.instance import *


if __name__ == '__main__':
	if len(argv) != 2:
		print('ERROR: Wrong number of parameters.')
		exit(1)
	
	cmd = argv[1]
	if cmd not in ALLOWED_COMMANDS:
		print('ERROR: Invalid command.')
		exit(1)

	if cmd == 'test_download':
		download_activities(
			DATA_PATH, 
			TEST_PROJECT, 
			TEST_DATE_FROM, 
			TEST_DATE_TO
		)
	elif cmd == 'test_group_by':
		exported_file = generate_download_filename(
			DOWNLOADED_FILE_PREFIX,
			TEST_PROJECT
		)
		groups = report_group_by(
			DATA_PATH,
			'__stdout__',
			exported_file
		)

		print('Groups collected for ', TEST_PROJECT)
		for k, v in groups.items():
			hours = v / 3600
			print('Group - Seconds/Hours: ', k, ' - ', v, '/', hours)

	elif cmd == "test_trello":
		print("test_trello")