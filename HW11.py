# =============================================================================
# Homework #10 utilized as input for Homework #11
# Utilize Numpy and SKlearn for Linear Regression
# =============================================================================

##########################################################################
#BEGIN FROM HOMEWORK #10

import numpy as np

def generate_data(n_points=10000, n_features=3, use_nonlinear=True, 
                    noise_std=0.1, train_test_split = 4):
    """
    Arguments:
    n_points - number of data points to generate
    n_features - a positive integer - number of features
    use_nonlinear - if True, generate non-linear data
    train_test_split - an integer - what portion of data to use for testing
    
    Return:
    X_train, Y_train, X_test, Y_test, n_train, n_features
    """
    
    # Linear data or non-linear data?
    if use_nonlinear:
        weights = np.array([[1.0, 0.5, 0.2],[0.5, 0.3, 0.15]])
    else:
        weights = np.array([1.0, 0.5, 0.2])
        

    
    bias = np.ones(n_points).reshape((-1,1))
    low = - np.ones((n_points,n_features),'float')
    high = np.ones((n_points,n_features),'float')
        
    np.random.seed(42)
    X = np.random.uniform(low=low, high=high)
    
    np.random.seed(42)
    noise = np.random.normal(size=(n_points, 1))
    noise_std = 0.1
    
    if use_nonlinear:
        Y = (weights[0,0] * bias + np.dot(X, weights[0, :]).reshape((-1,1)) + 
             np.dot(X*X, weights[1, :]).reshape([-1,1]) +
             noise_std * noise)
    else:
        Y = (weights[0] * bias + np.dot(X, weights[:]).reshape((-1,1)) + 
             noise_std * noise)
    
    n_test = int(n_points/train_test_split)
    n_train = n_points - n_test
    
    X_train = X[:n_train,:]
    Y_train = Y[:n_train].reshape((-1,1))

    X_test = X[n_train:,:]
    Y_test = Y[n_train:].reshape((-1,1))
    
    return X_train, Y_train, X_test, Y_test, n_train, n_features

X_train, Y_train, X_test, Y_test, n_train, n_features = generate_data(use_nonlinear=False)
X_train.shape, Y_train.shape


#END FROM HOMEWORK #10
####################################################################################################
#BEGIN HOMEWORK #11

#Linear Regression with SKLearn
def sklearn_lin_regress(X_train, Y_train):
    """
    Arguments:
    X_train  - np.array of size (n by k) where n is number of observations 
                of independent variables and k is number of variables
    Y_train - np.array of size (n by 1) where n is the number of observations of dependend variable
    
    Return:
    np.array of size (k+1 by 1) of regression coefficients
    """ 
    from sklearn.linear_model import LinearRegression
    lin_reg = LinearRegression()
    ndim = X_train.shape[1]
    
    try: 
        from sklearn.linear_model import LinearRegression
    except ImportError:
        raise("ImportError: No module named sklearn.linear_model found")
    
    X_train = np.hstack((np.ones((X_train.shape[0], 1)), X_train))
    reg = LinearRegression(fit_intercept = False)
    reg.fit(X_train, Y_train)
    theta_sklearn = reg.coef_

    return theta_sklearn

theta_sklearn = sklearn_lin_regress(X_train, Y_train)
part_2 = list(theta_sklearn.squeeze())
try:
    part2 = " ".join(map(repr, part_2))
except TypeError:
    part2 = repr(part_2)
    
theta_sklearn.squeeze()

#ARRAY OUTPUT: array([0.99946227, 0.99579039, 0.499198  , 0.20019798])

#END HOMEWORK #11
