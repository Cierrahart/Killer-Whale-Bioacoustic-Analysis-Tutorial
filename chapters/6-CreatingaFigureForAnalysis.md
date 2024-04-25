# Part 6: Creating a Figure for Analysis

### Objective
To create an image for visual analysis on the acoustic data to assess the presence and absence of killer whales at different times of the day over a series of days.

### Description
This section details the process of preparing and analyzing acoustic detection data for visual analysis. The analysis focuses on filtering and organizing data to identify unique occurrences of killer whale vocalizations by time and date, and visually representing this data in a figure.

### Steps

**1. Consolidate Data:**
- Combine all CSV output files into a single document to streamline the analysis process.
- Ensure that the document is free from typos and empty rows in key information fields.

**2. Extract Time Data:**
- Run the [PullOutDatetimes](../PullOutDatetimes.py) script to extract the year, month, day, hour, and minute from each filename. This will make filtering and analysis easier.

**3. Filter Detection Data and Remove Duplicates:**
- Apply filters to isolate rows that pertain only to killer whale (KW) detections, ensuring that the data set contains relevant entries.
- Remove duplicate records to ensure each data point represents a unique detection event based on ecotype, day and hour, preparing the data for accurate statistical analysis.

**5. Create Visualization of Data:**
- Once the data is cleaned and organized, use RStudio to run [FigureEcotypeDetectionsOverTime](../FigureEcotypeDetectionsOverTime.R) to create a figure. 
- The figure will display days on the x-axis and time of day on the y-axis to visualize the presence patterns of killer whales.
- This visualization helps in understanding patterns and trends in the data.

---

[← Previous: Raven Pro Analysis](5-RavenProAnalysis.md) | [Next: Back Home →](../README.md) 