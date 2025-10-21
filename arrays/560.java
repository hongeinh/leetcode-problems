// https://leetcode.com/problems/subarray-sum-equals-k/description/
class Solution {
    public int subarraySum(int[] nums, int k) {
        int n = nums.length;
        int[] prefix = new int[n];
        int sum = 0;
        for (int i = 0; i < n; i++) {
            prefix[i] = sum + nums[i];
            sum = prefix[i];
        }

        // Arrays.asList(prefix).stream().forEach(i -> System.out.print(i + " "));
        int count = 0;
        for (int start = 0; start < n; start++) {
            for (int end = start; end < n; end++) {
                if (prefix[end] - prefix[start] + nums[start] == k) count++;
            }
        }
        return count;
    }
}