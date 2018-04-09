# Google: how to add to list in python

import glob
import os

full_results_list = []


# Inefficient way
for file in glob.glob("./data/*.txt"):

        opened_file = open(file, 'r')
        read_file = opened_file.readlines()

        participant_id = os.path.basename(file)

        # Conditional line reading
        for line in read_file:
            if "1." in line:
                response_q1 = line
            if "2." in line:
                response_q2 = line
            
        results = [participant_id, response_q1, response_q2]
        full_results_list.append(results)

print(full_results_list)


# More efficient way
for file in glob.glob("./data/*.txt"):

        opened_file = open(file, 'r')
        read_file = opened_file.readlines()

        results = [os.path.basename(file)]

        for line in read_file:
            results.append(line)
        full_results_list.append(results)

print(full_results_list)
