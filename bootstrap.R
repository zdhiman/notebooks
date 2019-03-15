# what we really need is some way to assess the precision of our measure starting from the data sample we have.

# Bootstrap in a nutshell
## Bootstrap is a technique made in order to measure confidence intervals and/or standard error of an observable that can be calculated on a sample.

## It relies on the concept of resampling, which is a procedure that, starting from a data sample, simulates a new sample of the same size, considering every original value with replacement. Each value is taken at the same probability of the others (which is 1/N).

# Let’s say we want to measure the skewness of the sepal length in the famous iris dataset and let’s say we want to know its expected value, its standard error and the 5th and 9th percentile.

# Load the iris dataset
data(iris)

# Bootstrap library
library("bootstrap")

# e1071 library contains the "skewness" function
library("e1071")

# Set seed for replication of results
set.seed(1) 

# Store data in a vector
data = iris$Sepal.Length

# Run 200 bootstrap iterations to calculate the skewness
bs = bootstrap(data,nboot = 200,skewness)

# Store all 200 skewness values in a vector
values = bs$thetastar

# Calculate mean value, standard deviation and quantiles
mean(values)
sd(values)
quantile(values,c(0.05,0.95))
# These numbers allow us to say that the real skewness value of the dataset is 0.29 +/- 0.13 and it is between 0.10 and 0.49 with a 90% confidence.

