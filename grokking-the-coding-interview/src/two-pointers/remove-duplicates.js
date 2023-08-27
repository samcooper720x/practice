/*
 * 07-08-2023
 * Solved in 02:08
 */

// function remove(arr) {
//   return arr.reduce((acc, curr) => acc.add(curr), new Set()).size;
// }

function remove(arr) {
  let [i, nextNonDuplicate] = [0, 1];

  while (i < arr.length) {
    console.log("arr[nextNonDuplicate - 1]", arr[nextNonDuplicate - 1]);
    console.log("arr[i]", arr[i]);
    if (arr[nextNonDuplicate - 1] !== arr[i]) {
      arr[nextNonDuplicate] = arr[i];
      nextNonDuplicate++;
    }

    i++;
    console.log(arr);
  }

  return nextNonDuplicate;
}

module.exports = remove;
