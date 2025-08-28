// https://leetcode.com/problems/sort-the-matrix-diagonally/description/
class Solution {
    public int[][] diagonalSort(int[][] mat) {
        int n = mat.length;
        if (n == 0) {
            return mat;
        }
        int m = mat[0].length;
        List<List<Integer>> diagonals = transformDiagonal(n, m, mat);
        return transformGrid(n, m, diagonals);
    }

    public List<List<Integer>> transformDiagonal(int rows, int cols, int[][] mat) {
        List<List<Integer>> diagonals = new ArrayList<>();
        int row = 0, col = cols - 1;
        int min = Math.min(rows, cols);
        while (row < rows) {
            // System.out.println("row=" + row + ", col=" + col);
            List<Integer> diagonal = new ArrayList<>();
            
            for (int k = 0; k < min; k++) {
                if (row + k >= rows || col + k >= cols) break;
                diagonal.add(mat[row + k][col + k]);
            }
            Collections.sort(diagonal);
            diagonals.add(diagonal);
            // System.out.println(diagonal);
            if (col > 0) {
                col--;
            } else {
                row++;
            }
        }
        return diagonals;
    }

    public int[][] transformGrid(int rows, int cols, List<List<Integer>> diagonals) {
        int[][] mat = new int[rows][cols];
        int row = 0, col = cols - 1;
        for (List<Integer> diagonal: diagonals) {
            for (int k = 0; k < diagonal.size(); k++) {
                mat[row + k][col + k] = diagonal.get(k);
            }
            if (col > 0) {
                col--;
            } else {
                row++;
            }
        }

        return mat;
    }
}

