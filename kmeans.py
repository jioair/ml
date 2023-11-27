#KMEANS 

import numpy as np

# Define the dataset
data = np.array([2, 4, 6, 8, 10, 12, 18, 25, 30])

# Initial mean values
m1 = 2
m2 = 18

# Number of iterations
max_iters = 5

# Lists to store means and clusters at each iteration
mean_history = [m1, m2]
cluster_history = []

for _ in range(max_iters):
    # Initialize empty clusters
    cluster1 = []
    cluster2 = []

    # Assign each data point to the nearest mean
    for point in data:
        dist_to_m1 = abs(point - m1)
        dist_to_m2 = abs(point - m2)

        if dist_to_m1 < dist_to_m2:
            cluster1.append(point)
        else:
            cluster2.append(point)

    # Calculate the new means (handle empty clusters)
    new_m1 = np.mean(cluster1) if cluster1 else m1
    new_m2 = np.mean(cluster2) if cluster2 else m2

    # Record the means and clusters at this iteration
    mean_history.append((new_m1, new_m2))
    cluster_history.append((cluster1, cluster2))

    # Check for convergence
    if m1 == new_m1 and m2 == new_m2:
        break

    m1 = new_m1
    m2 = new_m2

# Output the clusters and means at each iteration
for i, (m1, m2) in enumerate(zip(mean_history, mean_history[1:])):
    print(f"Iteration {i + 1} - Mean 1: {m1}, Mean 2: {m2}")
    
    # Check if cluster history is not empty before accessing indices
    if cluster_history and i < len(cluster_history):
        print("Cluster 1:", cluster_history[i][0])
        print("Cluster 2:", cluster_history[i][1])
    print()
