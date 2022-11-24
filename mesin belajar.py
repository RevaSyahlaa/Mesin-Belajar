from sklearn import tree
 
#database : gerbang logika AND
# x = data, Y = Target

x = [[0,0],[0,1],[1,0],[1,1],[0,2],[2,1],[1,2],[2,2],[0,3]]
y = [0,0,0,1,2,1,2,2,0]

# Training and Classify
clf = tree.DecisionTreeClassifier()
clf = clf.fit(x,y)

#prediksi
print ("logika AND Metode Decision Tree")
print ("Logika = Prediksi")
print ("0 0 = ", clf.predict([[0,0]]))
print ("0 1 = ", clf.predict([[0,1]]))
print ("1 0 = ", clf.predict([[1,0]]))
print ("1 1 = ", clf.predict([[1,1]]))
print ("0 2 = ", clf.predict([[0,2]]))
print ("2 1 = ", clf.predict([[2,1]]))
print ("1 2 = ", clf.predict([[1,2]]))
print ("2 2 = ", clf.predict([[2,2]]))
print ("0 3 = ", clf.predict([[0,3]]))
