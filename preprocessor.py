import os
import csv

folder_name = "Cue-Target-Pair"

with open("All-Pairs.csv", "wb") as write_folder:
    writer = csv.writer(write_folder)
    for filename in os.listdir(folder_name):
        with open(os.path.join(folder_name, filename), 'r') as read_folder:
            line = read_folder.readline()
            #Skips the header line
            line = read_folder.readline().split(" ")
            while len(line) > 1:
                #cue, target, cue-to-target strength
                writer.writerow([line[0], line[1], line[5]])
                line = read_folder.readline().split(" ")

            # while line:
            #     print(line.split(" ")[0])
            #     line = f.readline()