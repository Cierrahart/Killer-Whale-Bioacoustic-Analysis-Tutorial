# -*- coding: utf-8 -*-
"""
Created on Tue Feb 20 09:01:24 2024

@author: cierr
"""

from datetime import datetime, timedelta
import pandas as pd

# Read a CSV file and automatically parse specified date columns
def read_excel_file(file_path):
    date_columns = ['UTC']
    return pd.read_csv(file_path, parse_dates=date_columns)

# Extract and convert the timestamp from a WAV filename to a datetime object
def extract_timestamp_from_wav_filename(filename):
    # Extract the timestamp part from the filename (ignoring the 337_ prefix and .wav extension)
    timestamp_str = filename.split('_', 1)[1].rsplit('.', 1)[0]
    # Replace the last underscore with a colon to correctly format milliseconds
    timestamp_str = timestamp_str[:-4] + "." + timestamp_str[-3:]
    
    # Convert the string to a datetime object
    return datetime.strptime(timestamp_str, "%Y%m%d_%H%M%S.%f")

# Convert raw detection data to a structured format with begin and end times in seconds
def process_data(df, first_wave_file):
    start_timestamp = extract_timestamp_from_wav_filename(first_wave_file)
    
    output_data = []
    for index, row in df.iterrows():
        # Convert UTC and UTCMilliseconds to Begin Time
        begin_time_utc = pd.to_datetime(row['UTC'])
        begin_time_utc = begin_time_utc + timedelta(milliseconds=row['UTCMilliseconds'])
        begin_time_s = (begin_time_utc - start_timestamp).total_seconds()
            
        # Convert Duration to End Time
        duration_ms = row['duration'] / 48000 * 1000
        end_time_utc = begin_time_utc + timedelta(milliseconds=duration_ms)
        end_time_s = (end_time_utc - start_timestamp).total_seconds()

        output_data.append({
            'Selection': row['Id'],
            'View': 1,
            'Channel': 1,
            'Begin Time (s)': begin_time_s,
            'End Time (s)': end_time_s,
            'Low Freq (Hz)': row['lowFreq'],
            'High Freq (Hz)': row['highFreq']
        })
        
    return pd.DataFrame(output_data)

 # Save the DataFrame to a text file in a tab-delimited format   
def save_to_tab_delimited(df, output_path):
    df.to_csv(output_path, sep='\t', index=False)

# Define paths for input and output files
detections_file_path = "path/to/your/detections.csv"
output_path_txt = "path/to/your/outputfile.txt"
first_wave_file = "nameoffirstwavfile.wav"

# Read the MySQL output CSV
df = read_excel_file(detections_file_path)
# Process the data to prepare for Raven Pro
processed_df = process_data(df, first_wave_file)
# Save the processed data to a tab-delimited TXT file
save_to_tab_delimited(processed_df, output_path_txt)



