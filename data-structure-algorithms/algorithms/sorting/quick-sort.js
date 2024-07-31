function quickSort(arr, low, high) {
  if (low < high) {
    const partitionIndex = partition(arr, low, high);
    // -1 & +1 because the position of partitionIndex is sorted -> no need to sort it
    // recursively sort two sides of the partition
    quickSort(arr, low, partitionIndex - 1);
    quickSort(arr, partitionIndex + 1, high);
  }
}

function partition(arr, low, high) {
  // if pivot is not the last element -> algo can be different
  const pivot = arr[high];
  // two pointers, the goal is to move smaller elements to the left, larger to the right
  // if seen arr[j] <= pivot -> swap with a[i], which is on the left aka move arr[j] to the left. Dont care if a[i] is greater or not
  let i = low - 1;
  for (j = low; j < high; j++) {
    console.log(i, j, arr[j], pivot);
    if (arr[j] <= pivot) {
      i++;
      let temp = arr[j];
      arr[j] = arr[i];
      arr[i] = temp;
    }
  }
  // after traversing, all smaller elements are from a[i--] -> the position for pivot is the arr[++i]
  i++;
  let temp = arr[i];
  arr[i] = arr[high];
  arr[high] = temp;
  return i;
}

(() => {
  const arr = [10, 80, 30, 90, 40];
  console.log(arr);
  // arr.length - 1 since we use pivot as the last element
  quickSort(arr, 0, arr.length - 1);
  console.log(arr);
})();
