import numpy as np
from random import shuffle

def softmax_loss_naive(W, X, y, reg):
  """
  Softmax loss function, naive implementation (with loops)

  Inputs have dimension D, there are C classes, and we operate on minibatches
  of N examples.

  Inputs:
  - W: A numpy array of shape (D, C) containing weights.
  - X: A numpy array of shape (N, D) containing a minibatch of data.
  - y: A numpy array of shape (N,) containing training labels; y[i] = c means
    that X[i] has label c, where 0 <= c < C.
  - reg: (float) regularization strength

  Returns a tuple of:
  - loss as single float
  - gradient with respect to weights W; an array of same shape as W
  """
  # Initialize the loss and gradient to zero.
  loss = 0.0
  dW = np.zeros_like(W)

  #############################################################################
  # TODO: Compute the softmax loss and its gradient using explicit loops.     #
  # Store the loss in loss and the gradient in dW. If you are not careful     #
  # here, it is easy to run into numeric instability. Don't forget the        #
  # regularization!                                                           #
  #############################################################################
  num_train = X.shape[0]
  num_classes = W.shape[1]
  
  scores = np.dot(X, W) 

  for i in range(num_train):
      s = scores[i] - np.max(scores[i])
      p = np.exp(s[y[i]]) / np.sum(np.exp(s))
      loss += -np.log(p)
 
      for j in range(num_classes):
          if j == y[i]:
              dW[:, j] += -X[i] + np.exp(s[j]) / np.sum(np.exp(s)) * X[i]
          else: 
              dW[:, j] += np.exp(s[j]) / np.sum(np.exp(s)) * X[i]

  loss /= num_train
  loss += reg * np.sum(W * W)

  dW /= num_train
  dW += reg * 2 * W
  #############################################################################
  #                          END OF YOUR CODE                                 #
  #############################################################################

  return loss, dW


def softmax_loss_vectorized(W, X, y, reg):
  """
  Softmax loss function, vectorized version.

  Inputs and outputs are the same as softmax_loss_naive.
  """
  # Initialize the loss and gradient to zero.
  loss = 0.0
  dW = np.zeros_like(W)

  #############################################################################
  # TODO: Compute the softmax loss and its gradient using no explicit loops.  #
  # Store the loss in loss and the gradient in dW. If you are not careful     #
  # here, it is easy to run into numeric instability. Don't forget the        #
  # regularization!                                                           #
  #############################################################################
  num_train = X.shape[0]

  scores = np.dot(X, W)
  scores -= np.max(scores, axis=1)[:, np.newaxis]
  probs = np.exp(scores[range(num_train), y]) / np.sum(np.exp(scores), axis=1)
  loss += np.sum(-np.log(probs))

  p = np.exp(scores) / np.sum(np.exp(scores), axis=1)[:, np.newaxis]
  p[range(num_train), y] -= 1
  dW += np.dot(X.T, p)
  loss /= num_train
  loss += reg * np.sum(W * W)

  dW /= num_train
  dW += reg * 2 * W
  #############################################################################
  #                          END OF YOUR CODE                                 #
  #############################################################################

  return loss, dW

