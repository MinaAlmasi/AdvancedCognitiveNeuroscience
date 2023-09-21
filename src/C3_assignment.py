from ndslib.data import load_data
import numpy as np

from sklearn.naive_bayes import GaussianNB
from sklearn.model_selection import cross_validate
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline

from sklearn.neural_network import MLPClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC

def cross_validator(clf, X, y, n_folds, return_dict=True): 
    # setup pipeline for classifcation
    pipe = Pipeline([
        ("scale", StandardScaler()),
        ("clf", clf)]
    )

    output = cross_validate(pipe, X, y, cv=n_folds, return_estimator=True)

    if return_dict: 
        return output 

    else:
        return np.mean(output["test_score"])        

    return output 

def main(): 
    abide_data = load_data("abide2")

    # extract features
    X = abide_data.filter(like='fs')
    y = abide_data["group"]

    # define n folds
    n_folds = 5

    # init classifiers
    clf_KNN = KNeighborsClassifier()
    clf_GNB = GaussianNB()
    clf_SVC = SVC()
    clf_MLP = MLPClassifier(hidden_layer_sizes=(30, ))

    # run loop 
    for clf in [clf_GNB, clf_KNN, clf_SVC, clf_MLP]:
        mean_score = cross_validator(clf, X, y, n_folds=n_folds, return_dict=False)
        print(f"{clf.__class__.__name__} mean score: {round(mean_score, 4)}")


if __name__ == "__main__":
    main()