# Description
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.

 

### Example 1:
Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Explanation: 
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].
Notice that the order of the output and the order of the triplets does not matter.

### Example 2:
Input: nums = [0,1,1]
Output: []
Explanation: The only possible triplet does not sum up to 0.

### Example 3:
Input: nums = [0,0,0]
Output: [[0,0,0]]
Explanation: The only possible triplet sums up to 0.

# Solution idea
## S1 - Brute force
Sort list
Loop through the array with 3 nested loop, each loop is responsible for an index. 
For each combination of (i, j, k), create a set for equivalent loop values:
- exist_i: if the value nums[i] have been added to the result
- exist_j: if the value nums[j] have been added to the result
- exist_k: if the value nums[k] have been added to the result
Only execute if the currently considered nums[v] has not been added to the set
Check if sum of the values are 0.
Add to list if true.

## S2 - Improved brute force
Since list is already sorted:
- If nums[k] satisfies for (i, j, k) combinations, all k+n index does not satisfy the condition
- If nums[i] + nums[j] == 0, no nums[k] will satisfy the condition. 
