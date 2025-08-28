// https://leetcode.com/problems/sort-matrix-by-diagonals/description/?envType=daily-question&envId=2025-08-28
class Solution {
    public int[][] sortMatrix(int[][] grid) {
        int n = grid.length;
        List<List<Cell>> diagonals = this.transformDiagonal(n, grid);
        return transformGrid(n, diagonals);

    }

    public List<List<Cell>> transformDiagonal(int n, int[][] grid) {
        List<List<Cell>> diagonals = new ArrayList<>();
        int row = 0, col = n - 1;
        while (row < n) {
            List<Cell> diagonal = new ArrayList<>();
            for (int k = 0; k < n; k++) {
                if (row + k >= n || col + k >= n) break;
                diagonal.add(new Cell(row + k, col + k, grid[row + k][col + k]));
            }
            if (row == 0 && col > 0) {
                Collections.sort(diagonal);
            } else {
                Collections.sort(diagonal, Collections.reverseOrder());
            }
            diagonals.add(diagonal);
            if (col > 0) {
                col--;
            } else {
                row++;
            }
        }
        return diagonals;
    }

    public int[][] transformGrid(int n, List<List<Cell>> diagonals) {
        int[][] result = new int[n][n];
        int row = 0, col = n - 1;
        for (List<Cell> diagonal : diagonals) {
            for (int k = 0; k < diagonal.size(); k++) {
                if (row + k >= n || col + k >= n) break;
                result[row + k][col + k] = diagonal.get(k).getValue();
            }
            if (col > 0) {
                col--;
            } else {
                row++;
            }
        }
        return result;
    }
}

class Cell implements Comparable<Cell> {
    int row;
    int col;
    int value;

    Cell(int row, int col, int value) {
        this.row = row;
        this.col = col;
        this.value = value;
    }

    public String toString() {
        return "(" + this.row + "," + this.col + ") = " + this.value;
    }

    public int getValue() {
        return this.value;
    }

    public int compareTo(Cell other) {
        return Integer.compare(this.value, other.value);
    }
}