# -*- coding: utf-8 -*-
"""
Created on Fri Apr 12 15:57:49 2024

@author: cierr
"""
import csv
import os

def convert_tsv_to_csv(txt_file_path):

    # Extract the directory from the provided file path
    directory = os.path.dirname(txt_file_path)
    # Create the CSV filename by replacing the .txt extension with .csv
    csv_file_path = os.path.join(directory, os.path.basename(txt_file_path).replace('.txt', '.csv'))
    
    # Open the TSV file in read mode and the CSV file in write mode
    with open(txt_file_path, 'r') as txt_file:
        # Create a CSV writer that delimits fields with commas
        with open(csv_file_path, 'w', newline='') as csv_file:
            writer = csv.writer(csv_file, delimiter=',')
            
            # Read the TSV file line by line
            for line in txt_file:
                # Split each line by tabs and remove any leading/trailing whitespace
                data = line.strip().split('\t')
                # Write the list of values to the CSV file
                writer.writerow(data)

    # Return the path of the created CSV file for confirmation
    return csv_file_path

# Specify the path of the TSV file to convert
txt_file_path = r"path/to/your/text/file.txt"

# Convert the TSV file to a CSV file and capture the new file's location
csv_file_path = convert_tsv_to_csv(txt_file_path)

# Print the location of the newly created CSV file to the console
print(f'CSV file has been created at: {csv_file_path}')


