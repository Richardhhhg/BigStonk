# Logistic Regression for estimating stonk performance in future
from sklearn.linear_model import LogisticRegression

clf = LogisticRegression() # initialize logistic regression
# need to add training data to this
# X variable is weighted market semtiment and personal opinion
# Y variable is where stock price is in 2 months
    # averaged out for the week (preventing super negative or super positive biases from things like earnings)
