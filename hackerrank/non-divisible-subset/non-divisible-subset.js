/*
 * Complete the 'nonDivisibleSubset' function below.
 *
 * The function is expected to return an INTEGER.
 * The function accepts following parameters:
 *  1. INTEGER k
 *  2. INTEGER_ARRAY s
 */

function nonDivisibleSubset(k, s) {
  // Write your code here
  let countArray = new Array(k).fill(0);
  for (const num of s) {
    countArray[num % k] += 1;
  }
  console.log(countArray);
  let maxLength = 0;
  // case first index = 0, get max 1 element
  maxLength += Math.min(countArray[0], 1);
  // special case where k is even -> only take at most 1 element at index k / 2
  if (k % 2 === 0) {
    maxLength += Math.min(Math.floor(countArray[k / 2]), 1);
  }
  // k / 2 + 1 because we compare index q versus index k - q
  // when q increments over k / 2 + 1 -> k - q will be smaller than q -> overlap
  for (let q = 1; q < Math.floor(k / 2) + 1; q++) {
    // -1 since p can only goes from 0 to k-1
    // if k is odd
    if (q != k - q) {
      maxLength += Math.max(countArray[q], countArray[k - q]);
    }
  }
  return maxLength;
}
