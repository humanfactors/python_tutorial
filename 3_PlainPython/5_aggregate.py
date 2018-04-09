# This file takes the questions in the data directory and aggregates them into a single file
# ~ Michael

# Load required modules
import glob
import os
import csv

# Set an empty list to contain ALL our results
full_results_list = []

# Iterate over files in the glob file search
for file in sorted(glob.glob("./data/*.txt")):
        # Open each file
        opened_file = open(file, 'r')
        # Read the contents of each file
        read_file = opened_file.readlines()
        # Make the first element of new results list = basefilname of the file without the extension
        # Remember - use print(results) to inspect the status of it at each point of the loop
        results = [os.path.splitext(os.path.basename(file))[0]]
        
        # Then for each line the file, take everything after the first 2 characters
        # and strip trailing new lines
        for line in read_file:
            line = line[2:].strip()
            results.append(line)

        # Add the results to our final list
        full_results_list.append(results)

# open final_results.csv for writing, and then write all of our results list to it
# Note that writerows writes a list of list to CSVs without the need for iteration
with open('final_results.csv', 'w') as csvfile:
    my_writer = csv.writer(csvfile)
    my_writer.writerows(full_results_list)
