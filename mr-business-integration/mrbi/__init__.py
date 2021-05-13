from simplejson import load
from mrbi.config.instance import *
import totra


def generate_download_filename(prefix, project):
	"""Geberate filename for downloaded file
	
	Arguments:
		prefix str -- String from mrbi.config.instance module
		project str --  Project name from configuration
	
	Returns:
		str: filename
	"""
	return prefix + project.lower().replace(' ', '-') + '.json'


def download_activities(destination_path, project, from_date, to_date):
	"""Download activities from Top Tracker
	
	Arguments:
		destination_path str Absolute path to data dir where downloaded file should be saved
		project str - Name of the project we are working on.
		from_date str -- From date in format YYYY-MM-DD
		to_date str -- To date in format YYYY-MM-DD
	"""
	down_file = generate_download_filename(
		DOWNLOADED_FILE_PREFIX,
		project
	)
	data = totra.report_activities(
		TT_USERNAME, 
		TT_PASSWORD,
		workers=None,  # We do not need that, because only one worker is working on a project at the momet.
		projects=[project], 
		start_date=from_date,
		end_date=to_date
	)
	data_in_requested_format = totra.format_activities(data, format='json')
	destination_file_path = '/'.join([
		destination_path,
		down_file
	])
	totra.save_output(data_in_requested_format, destination_file_path)


def report_group_by(source_path, destination_path, exported_file):
	"""Report group by
	
	Group activities with the same description and show how many seconds 
	did you spend on a praticular activity
	
	Arguments:
		source_path str -- Absolute path to folder where file for reading is stored.
		destination_path str - [not used yet] At the moment everything goes to console.
		project str -- Project identifier
	"""
	exported_path = '/'.join([
		source_path,
		exported_file
	])
	print('File for reading activities from:', exported_path)

	groupped = dict()
	with open(exported_path, 'r') as file_handle:
		data = load(file_handle)
		for d in data:
			if d['description'] not in groupped:
				groupped[d['description']] = 0
			
			groupped[d['description']] += d['seconds']

	return groupped

def test_trello ():
	pass
































