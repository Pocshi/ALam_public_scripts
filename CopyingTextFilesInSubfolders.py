import os
import csv
import xlsxwriter
from glob import glob


#Searches name of text files
text_file = 'Name_of_text_files'

#name of the output csv file
output_file = 'Name_of_output_file'


#base directory that you are searching from
base_directory = 'file_location'

if base_directory:
	subject_files = [os.path.join(root, subject_file) for root, dirs, files in os.walk(base_directory) for subject_file in files if subject_file.endswith((".txt")) if not os.path.basename(subject_file).startswith(('.','~'))]
	print(subject_files) #this line will print out the filenames, remove this if you don't want the console to explode.
	
	if subject_files:
		with open(os.path.join(base_directory, output_file + '.csv'), 'w', newline='') as output_file:
			file_writer = csv.writer(output_file)
			header = None
			for subject_number, subject_file in enumerate(subject_files,1):
				with open(subject_file, encoding='ansi') as csv_file: #encoding of the text file, change from ansi to another as required.
					file_reader = csv.reader(csv_file,delimiter=':') #change delimiter depending on your file
					for row in file_reader:
						print(row) #this will print out the files, remove this if you don't want the console to explode

                    # write value to csv file
					file_writer.writerow([os.path.basename(subject_file)] + list(row))