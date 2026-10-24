# load libraries
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn import metrics

# column names
col_names = ['Satisfaction_Score', 'Productivity_Score', 'Accuracy_Rating', 'Would_Recommend']
# load dataset
pima = pd.read_csv(r"E:\neskill\NexSkill course AI bin\Practice dated 10-10-26\AI_Usage_and_Impact_on_Students_and_Professionals.csv", usecols=col_names)
pima = pima.dropna()

# x and y split
feature_cols = ['Satisfaction_Score', 'Productivity_Score', 'Accuracy_Rating']
X = pima[feature_cols]
y = pima.Would_Recommend

# train and test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=1)

# create tree model
clf = DecisionTreeClassifier()

# train model
clf = clf.fit(X_train,y_train)

# predict
y_pred = clf.predict(X_test)

# accuracy
print("Accuracy:",metrics.accuracy_score(y_test, y_pred))

# tree image 1
from sklearn.tree import export_graphviz
from six import StringIO  
from IPython.display import Image  
import pydotplus

dot_data = StringIO()
export_graphviz(clf, out_file=dot_data,  
                filled=True, rounded=True,
                special_characters=True,feature_names = feature_cols,class_names=['Maybe','No','Yes'])
graph = pydotplus.graph_from_dot_data(dot_data.getvalue())  
graph.write_png('AIUsageV1.png')
Image(graph.create_png())

# new tree with entropy and max depth 3
clf = DecisionTreeClassifier(criterion="entropy", max_depth=3)

# train model
clf = clf.fit(X_train,y_train)

# predict
y_pred = clf.predict(X_test)

# accuracy
print("Accuracy:",metrics.accuracy_score(y_test, y_pred))

# tree image 2
from six import StringIO 
from IPython.display import Image  
from sklearn.tree import export_graphviz
import pydotplus
dot_data = StringIO()
export_graphviz(clf, out_file=dot_data,  
                filled=True, rounded=True,
                special_characters=True, feature_names = feature_cols,class_names=['Maybe','No','Yes'])
graph = pydotplus.graph_from_dot_data(dot_data.getvalue())  
graph.write_png('AIUsageV2.png')
Image(graph.create_png())

input("Wait for me...")