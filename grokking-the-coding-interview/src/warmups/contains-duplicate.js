/*
 * 30-07-2023
 * Solved in 09:23
 */

// function containsDuplicate(nums) {
//   function lookForDuplicate(num, remainingNums) {
//     if (remainingNums.includes(num)) {
//       return true;
//     } else {
//       const [nextNum, ...rest] = remainingNums;
//       if (rest.length === 0) {
//         return false;
//       } else {
//         return lookForDuplicate(nextNum, rest);
//       }
//     }
//   }
//
//   const [num, ...remainingNums] = nums;
//   return lookForDuplicate(num, remainingNums);
// }

function containsDuplicate(nums) {
  let uniqueNums = new Set();

  for (const num of nums) {
    if (uniqueNums.has(num)) {
      return true;
    } else {
      uniqueNums.add(num);
    }
  }

  return false;
}

module.exports = containsDuplicate;
