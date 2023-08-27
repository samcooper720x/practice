/*
 * 01-08-2023
 * Solved in 09:23
 */

// function numGoodPairs(nums) {
//   let numGoodPairs = 0;
//   for (let i = 0; i < nums.length - 1; i++) {
//     for (let j = i + 1; j < nums.length; j++) {
//       if (nums[i] === nums[j]) {
//         numGoodPairs++;
//       }
//     }
//   }
//
//   return numGoodPairs;
// }

function numGoodPairs(nums) {
  let numGoodPairs = 0;
  let occurrences = {};

  for (const num of nums) {
    occurrences[num] = (occurrences[num] || 0) + 1;
    numGoodPairs += occurrences[num] - 1;
  }

  return numGoodPairs;
}

module.exports = numGoodPairs;
