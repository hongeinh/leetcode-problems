// https://leetcode.com/problems/contains-duplicate-ii/?envType=study-plan-v2&envId=top-interview-150
class Solution {
    public boolean containsNearbyDuplicate(int[] nums, int k) {
        Map<Integer, Integer> lastSeens = new HashMap<>();
        for (int i = 0; i < nums.length; i++) {
            if (!lastSeens.containsKey(nums[i])) {
                lastSeens.put(nums[i], i);
            } else if (i - lastSeens.get(nums[i]) <= k) {
                return true;
            } else {
                lastSeens.put(nums[i], i);
            }
        }
        return false; 
    }
}