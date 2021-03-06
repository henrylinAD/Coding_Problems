# link: https://www.algoexpert.io/questions/Four%20Number%20Sum
# Difficulty: hard

# Four Number Sum
# Write a function that takes in a non-empty array of distinct integers and an integer representing a target sum. The
# function should find all quadruplets in the array that sum up to the target sum and return a two-dimensional array of
# all these quadruplets in no particular order.
# If no four numbers sum up to the target sum, the function should return an empty array.

# Sample Input
# array = [7, 6, 4, -1, 1, 2]
# targetSum = 16

# Sample Output
# [[7, 6, 4, -1], [7, 6, 1, 2]] // the quadruplets could be ordered differently

# Average: O(n^2) time | O(n^2) space: 2 for loops=2O(n^2)=> O(n^2)
# Worst: O(n^3) time | O(n^2) space

# Solution: create a hash table to store sum of every pair (for pair of numbers ), and quadruplets to store all
# possible quadruplets. Two for loops: first loop = current value + every value after current number, append current
# number and new number to the quadruplets array; second loop = current value + every value before current number, if
# currentSum not in allPairSums, then create a new key, value pair,
#
# Sample Input: [7, 6, 4, -1, 1, 2]
# allPairSums: (sum of current/main number and previous numbers, avoid duplication)
# main #  6   ,     4     ,     4     ,    -1     ,      -1  ,  1    ,     -1    ,     1    ,      1   ,       1
# { 13:[[7,6]], 11:[[7,4]], 10:[[6,4]], 6:[[7,-1]], 5:[[6,-1], [4,1]], 3:[[4,-1]], 8:[[7,1]], 7:[[6,1]], 0:[[-1,1]]}

def fourNumberSum(array, targetSum):
    allPairSums = {}  # hash table, store sum of every pair (for values before current number and current number) as
    # the difference b/t targetSum and currentSum; pairing numbers (before current number) to avoid duplicates
    quadruplets = []  # array, holds sums of the quadruplet, the value to return
    for i in range(1, len(array) - 1):  # skip 1st and last value, since no value before 1st or after last
        for j in range(i + 1, len(array)):  # loop through values after current number
            currentSum = array[i] + array[j]  # current sum = current value + value after current number
            difference = targetSum - currentSum  # difference b/t current sum and target sum
            if difference in allPairSums:  # if difference is in the hash table
                for pair in allPairSums[difference]:  # if so, iterate through all pairs in the hash table
                    quadruplets.append(pair + [array[i], array[j]])  # add the original pair and new points to
                    # quadruplets
        for k in range(0, i):  # loop through values before current number (excluded i)
            currentSum = array[i] + array[k]  # currentSum = current number + number k (before current value)
            if currentSum not in allPairSums:   # if currentSum not in allPairSums
                allPairSums[currentSum] = [[array[k], array[i]]]  # create new key, value pair (array) in allPairSums
            else:   # else if currentSum is in allPairSums
                allPairSums[currentSum].append([array[k], array[i]])  # added it to allPairSums
    return quadruplets
