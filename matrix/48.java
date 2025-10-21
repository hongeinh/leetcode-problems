// https://leetcode.com/problems/rotate-image/description/?envType=study-plan-v2&envId=top-interview-150
class Solution {
    public void rotate(int[][] matrix) {
        int n = matrix.length;
        int[][] tmp = new int[n][n];

        for (int r = 0; r < n; r++) {
            for (int c = 0; c < n; c++) {
                tmp[c][n - 1 - r] = matrix[r][c];
            }
        }
        for (int r = 0; r < n; r++) {
            for (int c = 0; c < n; c++) {
                matrix[r][c] = tmp[r][c];
            }
        }
    }
}