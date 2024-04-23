# -*- coding: utf-8 -*-
"""
Created on Fri Apr 19 21:46:01 2024

@author: cierr
"""

import pandas as pd

# Specify the path to the Excel file containing the acoustic detection data
file_path = "path/to/your/detections.xlsx"
# Load the Excel file into a pandas DataFrame
df = pd.read_excel(file_path)

# Parse the date and time from a given filename.
def parse_datetime(filename):
    
    # Split the filename into parts using underscore as the delimiter
    parts = filename.split('_')
    date_part = parts[1]  # Extracts the date part (YYYYMMDD)
    time_part = parts[2]  # Extracts the time part (HHMMSS)

    # Extract year, month, day from the date part
    year = date_part[:4]
    month = date_part[4:6]
    day = date_part[6:8]
    # Extract hour and minute from the time part
    hour = time_part[:2]
    minute = time_part[2:4]

    return year, month, day, hour, minute

# Apply the parse_datetime function to each filename in the 'Begin File' column
# This creates new columns for Year, Month, Day, Hour, and Minute in the DataFrame
df['Year'], df['Month'], df['Day'], df['Hour'], df['Minute'] = zip(*df['Begin File'].apply(parse_datetime))

# Define the path where the modified Excel file will be saved
output_file_path = "path/to/your/outputfile.xlsx"

# Write the modified DataFrame back to an Excel file, without the index
df.to_excel(output_file_path, index=False)

print("File processed and saved as", output_file_path)

