######################################################################################################################################################################
#   Written for Computer Vision team on McGill Robotics by Alexander Chatron-Michaud & Tristan Struthers
#   Usage: 
#          - First command line argument is flag 1. If cross validation and test sets should be created, use the flag -test. Otherwise use the "full" flag -full
#          - If .pkl files exist in the DATA folder, they will be loaded upon execution
#
######################################################################################################################################################################

import sys, string, pickle, os, time
import numpy as np
from sklearn import svm
from sklearn.externals import joblib
from sklearn import preprocessing

X = []
X_train = []
X_cv = []
X_test = []
y = []

def addToX(textfile): #Opens "textfile" and adds line-by-line training vectors to X_train and gives them the file's name as it's y value
        correct_val = os.path.splitext(textfile)[0]
        with open(textfile) as f:
                for x in f.readlines():
                        x = x.replace(',', '')
                        x = x.replace('(', '')
                        x = x.replace(')', '')
                        line = x.split()
                        outline = []
                        for char in line:
                                outline.append(float(char))
                        X.append(outline)
                        y.append(correct_val)
                f.close()

def setup_fresh(): #takes system arguments which are text files which contain all the examples of that category
    if len(sys.argv) < 3 :
        print "Please enter one or more data files as command line arguments."
        exit()

    for index in range(2,len(sys.argv)):
        addToX(sys.argv[index])
        print str(sys.argv[index]) + "done."
    
    #Use 60% of X as training, 20% as cross validation, and 20% for testing performance
    m = len(X)
    cv_index = int(m*0.6)
    test_index = int(m*0.8)
    X_train = X[0:cv_index]
    X_cv = X[cv_index:test_index]
    X_test = X[test_index:m+1]
    y_train = X[0:cv_index]
    y_cv = X[cv_index:test_index]
    y_test = X[test_index:m+1]

    #Give zero mean and unit variance
    scaler_full = preprocessing.StandardScaler().fit(X)
    X = scaler_full.transform(X)
    scaler_test = preprocessing.StandardScaler().fit(X_train)
    X_train = scaler_test.transform(X_train)
    X_cv = scaler_test.transform(X_cv)
    X_test = scaler_test.transform(X_test)
    joblib.dump(scaler, 'DATA/scaler_full.pkl')
    joblib.dump(scaler, 'DATA/scaler_test.pkl')
    joblib.dump(X_train, 'DATA/X_train.pkl')
    joblib.dump(X_cv, 'DATA/X_cv.pkl')
    joblib.dump(X_test, 'DATA/X_test.pkl')
    joblib.dump(y_train, 'DATA/y_train.pkl')
    joblib.dump(y_cv, 'DATA/y_cv.pkl')
    joblib.dump(y_test, 'DATA/y_test.pkl')
    joblib.dump(X, 'DATA/X.pkl')
    joblib.dump(y, 'DATA/y.pkl')

def setup_load():
    X = joblib.load('DATA/X.pkl')
    X_train = joblib.load('DATA/X_train.pkl')
    y = joblib.load('DATA/y.pkl')
    y_train = joblib.load('DATA/y_train.pkl')


def main():
    if len(sys.argv) < 2:
        print "Please use flag -full or -test when running the program"
        exit()
    if sys.argv[1] == "-full":
        full = True
    elif sys.argv[1] == "-test":
        full = False
    else:
        print "Please use flag -full or -test when running the program"
        exit()

    #If existing models have been parsed, load them, otherwise we parse them fresh
    if os.path.isfile('DATA/X_train.pkl') and os.path.isfile('DATA/y_train.pkl') and os.path.isfile('DATA/y.pkl') and s.path.isfile('DATA/X.pkl'):
        print "Pre-existing .pkl files found, loading from data..."
        setup_load()
    else:
        print "No .pkl files found, setting up a fresh environment..."
        setup_fresh()


    print "Setup done. Feedforward/Backprop initializing... (This may take some time)"
    init_time = time.time()

    NN_model = MLPClassifier(algorithm='l-bfgs', alpha=1e-5, hidden_layer_sizes=(128,128), random_state=1) #550 is a rough estimate for an appropriate number of hidden units
    if full:
        NN_model.fit(X,y)
    else:
        NN_model.fit(X_train,y_train)
    print "Feedforward/Backprop done. Training took " + str(time.time() - init_time) + " seconds. Saving model..."

    joblib.dump(NN_model, 'DATA/NN_model.pkl')
    print "Model save successful"

main()