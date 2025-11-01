import numpy as np
import kagglehub

# Problem 1
arr1 = np.arange(10, 51)
print(arr1)
print(f"Mean: {arr1.mean()}")
print(f"Max: {arr1.max()}")
print(f"Min: {arr1.min()}")

# Problem 2
arr2 = np.arange(1, 10).reshape(3, 3)
print("Array: \n", arr2)
print("Transpose: \n", arr2.T)
print("Sum: ", np.sum(arr2))
# Problem 3
nums = np.random.randint(1, 101, 10)
print("Average: ", nums.mean())
print("Greater Than 50", np.sum(nums > 50))
path = kagglehub.dataset_download("rockyjoseph/nifty-50-stock-market-data-2000-2023")

print("Path to dataset files:", path)