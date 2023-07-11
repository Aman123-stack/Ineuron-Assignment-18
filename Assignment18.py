q1>def merge_intervals(intervals):
    intervals.sort(key=lambda x: x[0])  # Sort intervals based on start time
    merged = []

    for interval in intervals:
        if not merged or interval[0] > merged[-1][1]:
            # If the result list is empty or the current interval does not overlap with the last interval
            merged.append(interval)
        else:
            # There is an overlap, update the end time of the last interval in the result list
            merged[-1][1] = max(merged[-1][1], interval[1])

    return merged


q2>def sortColors(nums):
    low = mid = 0
    high = len(nums) - 1

    while mid <= high:
        if nums[mid] == 0:
            nums[mid], nums[low] = nums[low], nums[mid]
            low += 1
            mid += 1
        elif nums[mid] == 1:
            mid += 1
        else:
            nums[mid], nums[high] = nums[high], nums[mid]
            high -= 1

# Test the function
nums = [2, 0, 2, 1, 1, 0]
sortColors(nums)
print(nums)



q3>def firstBadVersion(n):
    left = 1
    right = n

    while left < right:
        mid = left + (right - left) // 2  # Calculate the middle version

        if isBadVersion(mid):  # Check if the middle version is bad
            right = mid  # The bad version is in the left half, so update the right pointer
        else:
            left = mid + 1  # The bad version is in the right half, so update the left pointer

    return left  # Return the first bad version

# Test the function
bad_version = 4
def isBadVersion(version):
    return version >= bad_version

n = 10
first_bad = firstBadVersion(n)
print("The first bad version is:", first_bad)



q4>def maximumGap(nums):
    if len(nums) < 2:
        return 0

    # Find the maximum element in the array
    max_num = max(nums)

    # Perform Radix Sort
    exp = 1  # Current digit position
    n = len(nums)
    sorted_nums = [0] * n

    while max_num // exp > 0:
        count = [0] * 10  # Counting array for digits 0 to 9

        # Count the frequency of each digit
        for num in nums:
            count[(num // exp) % 10] += 1

        # Calculate the cumulative count
        for i in range(1, 10):
            count[i] += count[i - 1]

        # Build the sorted array based on the current digit
        for i in range(n - 1, -1, -1):
            digit = (nums[i] // exp) % 10
            sorted_nums[count[digit] - 1] = nums[i]
            count[digit] -= 1

        # Update the original array with the sorted array
        nums = sorted_nums.copy()

        exp *= 10

    # Calculate the maximum difference between two successive elements
    max_diff = 0
    for i in range(1, n):
        max_diff = max(max_diff, nums[i] - nums[i - 1])

    return max_diff

q5>def maximumGap(nums):
    if len(nums) < 2:
        return 0

    # Find the maximum element in the array
    max_num = max(nums)

    # Perform Radix Sort
    exp = 1  # Current digit position
    n = len(nums)
    sorted_nums = [0] * n

    while max_num // exp > 0:
        count = [0] * 10  # Counting array for digits 0 to 9

        # Count the frequency of each digit
        for num in nums:
            count[(num // exp) % 10] += 1

        # Calculate the cumulative count
        for i in range(1, 10):
            count[i] += count[i - 1]

        # Build the sorted array based on the current digit
        for i in range(n - 1, -1, -1):
            digit = (nums[i] // exp) % 10
            sorted_nums[count[digit] - 1] = nums[i]
            count[digit] -= 1

        # Update the original array with the sorted array
        nums = sorted_nums.copy()

        exp *= 10

    # Calculate the maximum difference between two successive elements
    max_diff = 0
    for i in range(1, n):
        max_diff = max(max_diff, nums[i] - nums[i - 1])

    return max_diff



q6>def containsDuplicate(nums):
    num_set = set()

    for num in nums:
        if num in num_set:
            return True
        num_set.add(num)

    return False



q7>def findMinArrowShots(points):
    if not points:
        return 0

    points.sort(key=lambda x: x[1])  # Sort balloons based on end positions
    arrows = 1  # Initialize the number of arrows to 1
    end = points[0][1]  # Initialize the end position

    for i in range(1, len(points)):
        if points[i][0] > end:
            # If the current balloon does not overlap with the previous one, a new arrow is needed
            arrows += 1
            end = points[i][1]

    return arrows



q8>def find132pattern(nums):
    n = len(nums)
    stack = []  # Stack to store the candidates for the '2' position

    max_2 = float('-inf')  # Maximum value for the '2' position

    for i in range(n - 1, -1, -1):
        if nums[i] < max_2:
            return True  # Found a '1', '3', '2' pattern

        while stack and nums[i] > stack[-1]:
            max_2 = stack.pop()  # Update the maximum value for the '2' position

        stack.append(nums[i])  # Add the current number to the stack

    return False  # No '1', '3', '2' pattern found

