import os
import csv

folder_name = "../../data/preproc/Cue-Target-Pair"

with open("../../data/raw/wan_pairs.csv", "w", newline ='') as write_folder:
    writer = csv.writer(write_folder)
    for filename in os.listdir(folder_name):
        with open(os.path.join(folder_name, filename), 'r') as read_folder:
            line = read_folder.readline()
            #Skips the header line
            line = read_folder.readline().split(", ")
            while len(line) > 1:
                #Cue, target, cue-to-target strength
                writer.writerow([line[0], line[1], line[5]])
                line = read_folder.readline().split(", ")