import os
import csv
import xlsxwriter
from glob import glob
from sys import exit

text_file = 'ABC_*info'
output_file = 'Report'



base_directory = '//fs2.shared.sydney.edu.au/BMRI/CRU/HBA/ABC_MRI/MRI_Data/preprocessed_data/dti'
if base_directory:
	subject_files = [os.path.join(root, subject_file) for root, dirs, files in os.walk(base_directory) for subject_file in files if subject_file.endswith((".txt")) if not os.path.basename(subject_file).startswith(('.','~'))]
	print(subject_files)#[subject_file for subject_file in glob(os.path.join(base_directory, '**', text_file), recursive = True) if not os.path.basename(subject_file).startswith(('.','~'))]
	
	if subject_files:
		with open(os.path.join(base_directory, output_file + '.csv'), 'w', newline='') as output_file:
			file_writer = csv.writer(output_file)
			header = None
			for subject_number, subject_file in enumerate(subject_files,1):
				with open(subject_file, encoding='utf-8') as csv_file:
					file_reader = csv.reader(csv_file,delimiter=':')
					for row in file_reader:
						print(row)

                    # Write values to new row, prepending with filename
					file_writer.writerow([os.path.basename(subject_file)] + list(row))