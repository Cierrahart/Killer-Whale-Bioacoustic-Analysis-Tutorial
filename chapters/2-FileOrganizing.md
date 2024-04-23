# Part 2: File Organizing

### Objective
To organize WAV files into manageable chunks to prevent software crashes and reduce processing times in PAMGuard and Raven Pro.

### Description
This section outlines the preliminary steps for organizing WAV files, particularly useful for systems with limitations on processing large volumes of data simultaneously. We will break down the data into 5-day chunks, which balances the load effectively for both detection in PAMGuard and analysis in Raven Pro.

 ### Steps
**1. Create Main Folders:**
Navigate to your main decompressed folder.
- Create subfolders to represent each 5-day period of data collection. 
- Ensure each folder is named intuitively to reflect the date range it covers. For example, name the folders as YYYY-MM-DD_to_YYYY-MM-DD, adjusting the dates accordingly.

**2. Prepare Subfolders for Output Files:**
- Inside each dated folder, create two additional subfolders:
  - MySQLFiles: This folder will store the detector outputs that are exported from MYSQL.
  - PythonFiles: This folder will hold the outputs from your Python scripts that are ready for analysis into Raven Pro.

**3. Organize WAV Files:**
- Distribute the WAV files into their corresponding 5-day folders. This step requires careful attention to ensure that each file is placed in the correct folder corresponding to its timestamp.

[← Previous: Decompressing Files](1-DecompressingFiles.md) | [Next: Building and Running the PAMGuard Detector →](3-BuildingAndRunningThePAMGuardDetector.md)
