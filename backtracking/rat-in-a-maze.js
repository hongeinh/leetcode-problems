// https://www.geeksforgeeks.org/rat-in-a-maze/
class Solution {
  /**
  * @param number n
  * @param number[][] arr

  * @returns string[]
  */

  // output: DDRDRR DRDDRR

  // input
  //             [[1, 0, 0, 0],
  //             [1, 1, 0, 1],
  //             [1, 1, 0, 0],
  //             [0, 1, 1, 1]]

  findPath(arr) {
    // code here
    let outputs = [];
    console.log("arr: ", arr);
    if (arr.length === 0) return outputs;
    if (arr[0][0] === 0) return outputs;
    this.traverse(arr, [], 0, 0, outputs);
    console.log("outputs: ", outputs);
    return "";
  }

  isValid(arr, x, y) {
    if (x > arr.length - 1 || y > arr.length - 1) return false;
    if (x < 0 || y < 0) return false;
    if (arr[x][y] === 0) return false;
    return true;
  }

  traverse(arr, tempPath, x, y, outputs) {
    // our base case (leaf happy case)
    if (x === arr.length - 1 && y === arr.length - 1) {
      outputs.push(JSON.parse(JSON.stringify(tempPath)));
      return;
    }
    // temp var so that we can revert the cell value after marking it as visited
    let cell = arr[x][y];
    // we mark this cell as visited
    // if next time we meet this cell again -> won't go into
    arr[x][y] = 0;
    // since we have 4 possible moves, we loop through every move then do it recursively
    for (const move of POSSIBLE_MOVES) {
      let nextX = x;
      let nextY = y;
      switch (move) {
        case "U":
          nextX--;
          break;
        case "D":
          nextX++;
          break;
        case "L":
          nextY--;
          break;
        case "R":
          nextY++;
          break;
        default:
          break;
      }
      console.log(
        `move: ${move}, arr[x][y]: ${
          arr[x][y]
        }, x: ${x}, y: ${y}, nextX: ${nextX}, nextY: ${nextY}, ${this.isValid(
          arr,
          nextX,
          nextY,
          tempPath
        )}`
      );
      // if a cell is valid then we store our step
      if (this.isValid(arr, nextX, nextY)) {
        tempPath.push(move);
        console.log("before call traverse: ", move, nextX, nextY, tempPath);
        // recursively move to the next cell and check all possible steps
        this.traverse(arr, tempPath, nextX, nextY, outputs);
        console.log("after call traverse: ", move, nextX, nextY);
        // after finish recursive -> backtrack!
        tempPath.pop();
      }
    }
    // backtracking, reset our cell back to normal
    arr[x][y] = cell;
  }
}
