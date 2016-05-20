#INPUT: list of text files as arguments to use for training

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
    for index in range(1,len(sys.argv)):
            addToX(sys.argv[index])
    
    #Use 60% of X as training, 20% as cross validation, and 20% for testing performance
    m = len(X)
    cv_index = int(m*0.6)
    test_index = int(m*0.8)
    X_train = X[0:cv_index]
    X_cv = X[cv_index:test_index]
    X_test = X[test_index:m+1]

    #Give zero mean and unit variance
    scaler = preprocessing.StandardScaler().fit(X_train)
    X_train = scaler.transform(X_train)
    X_cv = scaler.transform(X_cv)
    X_test = scaler.transform(X_test)
    #joblib.dump(scaler, 'DATA/scaler.pkl')
    joblib.dump(X_train, 'DATA/X_train.pkl')
    joblib.dump(X_cv, 'DATA/X_cv.pkl')
    joblib.dump(X_test, 'DATA/X_test.pkl')

def setup_load():
	X_train = joblib.load('DATA/X_train.pkl')
    X_cv = joblib.load('DATA/X_cv.pkl')
    X_test = joblib.load('DATA/X_test.pkl')


def main():
        
    setup_fresh() #use if no pkl files exist for sets
    #setup_load()
	print "Setup done. Feedforward/Backprop initializing... (This may take some time)"

	init_time = time.time()
    NN_model = MLPClassifier(algorithm='l-bfgs', alpha=1e-5, hidden_layer_sizes=(), random_state=1)
    print "Feedforward/Backprop done. Training took " + str(time.time() - init_time) + " seconds. Saving model..."

	joblib.dump(NN_model, 'DATA/NN_model.pkl')
    print "Model save successful"
    #debug(NN_model, X_cv, y)

main()