# -*- coding: utf-8 -*-
"""
Created on Sun Jun  7 19:42:48 2020

@author: lucas
"""
import threading
from multiprocessing.pool import ThreadPool

import pandas as pd
import matplotlib.pyplot as plt

from sklearn.tree import DecisionTreeClassifier
from sklearn.neural_network import MLPClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC

from sklearn.metrics import plot_confusion_matrix


from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.metrics import mean_squared_error as MSE

from sklearn.metrics import classification_report, confusion_matrix


##############################################################
import warnings
warnings.filterwarnings("ignore") #pour ignorer les warning dans la console
##############################################################

DIR_PATH_DATA = "F:\programmation\Docker\project_api_Docker\data"
FILE_DATA_CSV = "KDD_clean_database.csv"




def loop_better_classifier(classifiers, X, Y):
    ListDicAlgo = [] 
    for clf_name, clf in classifiers:
        X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size = 0.3, random_state = 1)
        
        clf.fit(X_train, Y_train)
        clf_predict = clf.predict(X_test)
        
        clf_accuracy_score = accuracy_score(Y_test, clf_predict)
        
        # print(confusion_matrix(Y_test, clf_predict))
        # print(classification_report(Y_test, clf_predict))
        
        # print(clf_name, " accuracy score : ",clf_accuracy_score)
        
        mse_clf = MSE(clf_predict, Y_test)
        rmse_clf = mse_clf ** (1/2)
        ListDicAlgo.append({clf_name: rmse_clf})

    return ListDicAlgo 



def displayBetterAlgo(DIR_PATH_DATA, FILE_DATA_CSV):

    df = pd.read_csv(DIR_PATH_DATA + FILE_DATA_CSV)

    X = df.drop('attack_name', axis = 1)
    Y = df['attack_name']


    mlp = MLPClassifier(hidden_layer_sizes = (64,32,16), random_state = 1)
    dt = DecisionTreeClassifier(min_samples_leaf = 1, random_state = 1)
    rfc = RandomForestClassifier(n_estimators = 10, max_depth = 16, random_state = 1)
    lr = LogisticRegression(random_state = 1)
    svm = SVC()# c'est un classifier 


    classifiers = [('DTC',dt), ('MLPC', mlp), ('RF', rfc), ("LR", lr)]
        

    pool = ThreadPool(processes=1)

    async_result = pool.apply_async(loop_better_classifier, (classifiers, X, Y))


    # thread_classifier_loop = threading.Thread(target = loop_better_classifier(classifiers, ListDicAlgo))
    # thread_classifier_loop.start()

    
    ListDicAlgo = async_result.get()

    return ListDicAlgo

