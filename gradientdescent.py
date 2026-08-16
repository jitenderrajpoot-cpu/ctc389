# Jitender Rajpoot

#function find bottom of hill
def gradient_descent(f_derivative, start, learning_rate, epochs):
  x = start             #start here on hill
  for _ in range(epochs):   #take steps depending on size of epoch
    gradient = f_derivative(x)    #which way is hill pointing
    x = x - learning_rate * gradient  #controls how big step is
  return x

def derivative(x):    #derivative of x**2 is 2x
  return 2 * x

#start at 10
result = gradient_descent(derivative, 20, 0.1, 20)

print(result)
