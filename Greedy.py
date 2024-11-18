import random

def numOfSubarrays(arr, k, threshold):
    target_sum = threshold * k
    current_sum = sum(arr[:k])
    count = 0
    if current_sum >= target_sum:
        count += 1
    for i in range(k, len(arr)):
        current_sum += arr[i] - arr[i - k]
        if current_sum >= target_sum:
            count += 1
    return count

random_arr = [random.randint(1, 99) for _ in range(random.randint(10, 20))]
k = random.randint(2, len(random_arr) // 2)
threshold = random.randint(1, 50)
result = numOfSubarrays(random_arr, k, threshold)

print("Array:", random_arr)
print("Subarray size (k):", k)
print("Threshold:", threshold)
print("Number of subarrays:", result)
