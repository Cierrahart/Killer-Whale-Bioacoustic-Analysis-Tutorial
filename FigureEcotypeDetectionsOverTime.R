
# Load required libraries
library(readxl)
library(ggplot2)
library(lubridate)
library(viridis)

# Set the file path for the Excel data
file_path <- "path/to/your/unique/detections.xlsx"

# Read data from Excel
data <- read_excel(file_path)

# Ensure 'Hour' is treated as numeric for time calculations
data$Hour <- as.numeric(as.character(data$Hour))

# Create a datetime object from separate date and time components for easier plotting
data$DateTime <- with(data, ymd_h(paste(Year, Month, Day, Hour, sep="-")))

# Convert 'Ecotype' to a factor for consistent coloring in the plot
data$Ecotype <- factor(data$Ecotype)

# Adjust hour labeling to place 'Midnight' last
hour_labels <- c("1 AM", "2 AM", "3 AM", "4 AM", "5 AM", "6 AM", 
                 "7 AM", "8 AM", "9 AM", "10 AM", "11 AM", "Noon", 
                 "1 PM", "2 PM", "3 PM", "4 PM", "5 PM", "6 PM", "7 PM", 
                 "8 PM", "9 PM", "10 PM", "11 PM", "Midnight")
data$Hour <- factor(ifelse(data$Hour == 0, 24, data$Hour), levels = 1:24, labels = hour_labels)

# Plot data using ggplot2 with color based on 'Ecotype' and custom date axis formatting
ggplot(data, aes(x=DateTime, y=Hour, color=Ecotype)) +
  geom_point(size=3, aes(alpha = Ecotype)) +
  scale_x_datetime(date_breaks = "1 week", date_labels = "%Y-%m-%d",
                   limits = as.POSIXct(c('2023-10-18', '2023-12-12'))) +
  scale_color_viridis(discrete = TRUE) +
  theme_minimal() +
  theme(axis.text.x = element_text(angle = 90, hjust = 1)) +
  labs(x = "Date", y = "Time of Day", color = "Ecotype", title = "Detection Timeline") +
  theme(legend.position = "bottom")

# Save the plot to a file
ggsave("ecotype_detections_over_time.png", path = file_path, width = 10, height = 6, dpi = 300)
