// https://leetcode.com/problems/number-of-people-aware-of-a-secret/description/?envType=daily-question&envId=2025-09-09
class Solution {

    private static final int MOD = 1000000007;

    public int peopleAwareOfSecret(int n, int delay, int forget) {
        int[]  dp = new int[n + 1];
        dp[1] = 1;

        int share = 0;
        for (int d = 2; d <= n; d++) {
            if (d - delay > 0) share = (share + dp[d - delay]) % MOD;
            if (d - forget > 0) share = (share - dp[d - forget] + MOD) % MOD;
            dp[d] = share; 
        }

        int know = 0;
        for (int i = n - forget + 1; i <= n; i++) {
            know = (know + dp[i]) % MOD;
        }
        return know;
    }
}