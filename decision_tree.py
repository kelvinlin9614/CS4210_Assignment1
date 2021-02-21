#-------------------------------------------------------------------------
# AUTHOR: ZEWEN LIN
# FILENAME: decision_tree
# SPECIFICATION: plot a decision tree
# FOR: CS 4210- Assignment #1
# TIME SPENT: 1hr
#-----------------------------------------------------------*/

#IMPORTANT NOTE: DO NOT USE ANY ADVANCED PYTHON LIBRARY TO COMPLETE THIS CODE SUCH AS numpy OR pandas. You have to work here only with standard vectors and arrays

#importing some Python libraries
from sklearn import tree
import matplotlib.pyplot as plt
import csv
db = []
X = []
Y = []

#reading the data in a csv file
with open('contact_lens.csv', 'r') as csvfile:
  reader = csv.reader(csvfile)
  for i, row in enumerate(reader):
      if i > 0: #skipping the header
         db.append (row)
         print(row)
#transform the original training features to numbers and add to the 4D array X. For instance Young = 1, Prepresbyopic = 2, Presbyopic = 3, so X = [[1, 1, 1, 1], [2, 2, 2, 2], ...]]
#--> add your Python code here
for i in range(len(db)):
    temp = []
    for j in range(len(db[i]) - 1):
        if db[i][j] == 'Young':
            temp.append(1)
        elif db[i][j] == 'Myope':
            temp.append(1)
        elif db[i][j] == 'No':
            temp.append(1)
        elif db[i][j] == 'Reduced':
            temp.append(1)
        elif db[i][j] == 'Presbyopic':
            temp.append(2)
        elif db[i][j] == 'Hypermetrope':
            temp.append(2)
        elif db[i][j] == 'Yes':
            temp.append(2)
        elif db[i][j] == 'Normal':
            temp.append(2)
        elif db[i][j] == 'Prepresbyopic':
            temp.append(3)
    X.append(temp)

#transform the original training classes to numbers and add to the vector Y. For instance Yes = 1, No = 2, so Y = [1, 1, 2, 2, ...]
#--> addd your Python code here
for i in range(len(db)):
    if db[i][4] == 'Yes':
        Y.append(1)
    elif db[i][4] == 'No':
        Y.append(2)

#fitting the decision tree to the data
clf = tree.DecisionTreeClassifier(criterion = 'entropy')
clf = clf.fit(X, Y)

#plotting the decision tree
tree.plot_tree(clf, feature_names=['Age', 'Spectacle', 'Astigmatism', 'Tear'], class_names=['Yes','No'], filled=True, rounded=True)
plt.show()


