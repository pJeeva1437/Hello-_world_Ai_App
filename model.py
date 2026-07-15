from sklearn.linear_model import LinearRegression

import numpy as np 

## Training
def train():
    ## Relationship will follow this equation y=2x+3
    #  Data Creation
    x=np.array([[1],[2],[3],[4],[5]]) ## 2D array as sklearn expects the input to be a 2D array(n_samplea,n_features)
    y=np.array([5,7,9,11,13])

    model=LinearRegression()
    model.fit(x,y)

    return model

