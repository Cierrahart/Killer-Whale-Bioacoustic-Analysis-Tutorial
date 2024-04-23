# Part 4: Preparing Results for Raven Pro

### Objective
To convert MySQL exported data into a format that is compatible with Raven Pro, enabling efficient analysis of acoustic detections.

### Description
This section provides a guide to exporting detection summaries from MySQL and converting them into a format readable by Raven Pro. The process includes using a Python script to reformat the MySQL CSV output, which facilitates the review and analysis of acoustic data for calls detected by the Whistle and Moan Detector.

### Steps

**1. Export Data from MySQL:**
- Open MySQL and access the database used by the Whistle and Moan Detector.
- Locate the table summarizing killer whale call detections.
- Click on the 'Export' button and save the CSV output to a folder designated for organization, such as “MySQLFiles”, within the respective data collection period's folder.

**2. Script Preparation:**
- Open Python and the script named [CSVtoRAVEN](../CSVtoRAVEN.py).
- Edit the script to include the correct paths for the input CSV and the output TXT file.
- Ensure the first WAV file is correctly listed for timestamp reference.

**3. File Conversion:**
- Execute the “CSVtoRAVEN” script to convert the MySQL CSV file into a TXT file that Raven Pro can read.

**4. Finalization:**
- Confirm the newly created TXT file is located in the output directory.
- This file is now formatted correctly and ready to be imported into Raven Pro for subsequent analysis.

[← Previous: Building and Running the PAMGuard Detector](3-BuildingAndRunningThePAMGuardDetector.md) | [Next: Raven Pro Analysis →](5-RavenProAnalysis.md) 