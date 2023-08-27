/*
 * 30-07-2023
 * Solved in 11:18
 */

// function mySqrt(x) {
//   let lastSqrt = 0;
//
//   for (let i = 0; i <= x; i++) {
//     const sq = i * i;
//
//     if (sq === x) {
//       return i;
//     } else if (sq > x) {
//       return lastSqrt;
//     } else {
//       lastSqrt = i;
//     }
//   }
//
//   return lastSqrt;
// }

function mySqrt(x) {
  if (x < 2) {
    return x;
  }

  let [left, right] = [2, Math.floor(x / 2)];

  while (left <= right) {
    const pivot = Math.floor(right - (right - left) / 2);
    const pivotSq = pivot * pivot;

    if (pivotSq < x) {
      left = pivot + 1;
    } else if (pivotSq > x) {
      right = pivot - 1;
    } else {
      return pivot;
    }
  }

  return right;
}

module.exports = mySqrt;
