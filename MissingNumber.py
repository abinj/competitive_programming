
# Method 1
# n = int(input())
# input_values = list(map(int, input().strip().split()))[:n]
# prev_num = 0
#
# input_values.sort()
# for i in range(n):
#     if i == len(input_values):
#         print(input_values[i-1] + 1)
#         break
#     if input_values[i] - prev_num != 1:
#         print(input_values[i] - 1)
#         break
#     prev_num = input_values[i]


# Best method
n = int(input())
arr = input().split()

arr = sum(map(int, arr))
total = (n * (n+1)) / 2
print(total - arr)
