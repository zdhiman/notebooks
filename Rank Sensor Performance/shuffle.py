# create data.csv
# randomly shuffle all the rows so that they can be divided into training data sets and test data sets
import random
fid = open("data/raw_data.csv", "r")
li = fid.readlines()
fid.close()
print(li)

random.shuffle(li)
print(li)

fid = open("data.csv", "w")
fid.writelines(li)
fid.close()