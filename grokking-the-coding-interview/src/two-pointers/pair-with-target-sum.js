/*
 * 01-08-2023
 * Solved in 09:27
 */

// function search(arr, targetSum) {
//   let [left, right] = [0, arr.length - 1];
//
//   while (left < right) {
//     const sum = arr[left] + arr[right];
//
//     if (sum === targetSum) {
//       return [left, right];
//     } else if (sum < targetSum) {
//       left++;
//     } else if (sum > targetSum) {
//       right--;
//     }
//   }
//
//   return [-1, -1];
// }

function search(arr, targetSum) {
  let nums = {};

  for (const [i, num] of Object.entries(arr)) {
    if (nums[targetSum - num]) {
      return [Number(nums[targetSum - num]), Number(i)];
    }
    nums[num] = i;
  }
}

module.exports = search;
