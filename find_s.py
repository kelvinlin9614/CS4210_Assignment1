#-------------------------------------------------------------------------
# AUTHOR: ZEWEN LIN
# FILENAME: find_s
# SPECIFICATION: find_s algorithm
# FOR: CS 4210- Assignment #1
# TIME SPENT: 1hr
#-----------------------------------------------------------*/

#IMPORTANT NOTE: DO NOT USE ANY ADVANCED PYTHON LIBRARY TO COMPLETE THIS CODE SUCH AS numpy OR pandas. You have to work here only with standard vectors and arrays

#importing some Python libraries
import csv

num_attributes = 4
db = []
print("\n The Given Training Data Set \n")

#reading the data in a csv file
with open('contact_lens.csv', 'r') as csvfile:
  reader = csv.reader(csvfile)
  for i, row in enumerate(reader):
      if i > 0: #skipping the header
         db.append (row)
         print(row)
print("\n The initial value of hypothesis: ")
hypothesis = ['0'] * num_attributes #representing the most specific possible hypothesis
print(hypothesis)

#find the first positive training data in db and assign it to the vector hypothesis
##--> add your Python code here
i = 0
while db[i][4] != 'Yes':
    i = i + 1
hypothesis = db[i]
print("\n The first positive training data: ")
print(hypothesis)

#find the maximally specific hypothesis according to your training data in db and assign it to the vector hypothesis (special characters allowed: "0" and "?")
##--> add your Python code here
j = i + 1
for j in range(len(db)):
    if db[j][4] == 'Yes':
        if hypothesis[0] != '?':
            if db[j][0] != hypothesis[0]:
                hypothesis[0] = '?'
        if hypothesis[1] != '?':
            if db[j][1] != hypothesis[1]:
                hypothesis[1] = '?'
        if hypothesis[2] != '?':
            if db[j][2] != hypothesis[2]:
                hypothesis[2] = '?'
        if hypothesis[3] != '?':
            if db[j][3] != hypothesis[3]:
                hypothesis[3] = '?'
print("\n The Maximally Specific Hypothesis for the given training examples found by Find-S algorithm:\n")
print(hypothesis)