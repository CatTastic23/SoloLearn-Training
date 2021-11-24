# Data Science - Pandas Pandas Pandas
Finding the next centroid

Unsupervised learning algorithm clustering involves updating the centroid of each cluster. Here we find the next centroids for given data points and initial centroids.

## Task
* Assume that there are two clusters among the given two-dimensional data points and two random points (0, 0), and (2, 2) are the initial cluster centroids. Calculate the euclidean distance between each data point and each of the centroid, assign each data point to its nearest centroid, then calculate the new centroid. If there's a tie, assign the data point to the cluster with centroid (0, 0). If none of the data points were assigned to the given centroid, return None.
 
## Input Format 
* First line: an integer to indicate the number of data points (n)
* Next n lines: two numeric values per each line to represent a data point in two dimensional space.

## Output Format
* Two lists for two centroids. Numbers are rounded to the second decimal place.

## Sample Input 
    3
    1 0
    0 .5
    4 0

## Sample Output 
    [0.5  0.25]
    [4. 0.]
