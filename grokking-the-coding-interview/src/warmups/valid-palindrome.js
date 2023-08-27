/*
 * 30-07-2023
 */

function isPalindrome(s) {
  function match(a, b) {
    return a.toLowerCase() === b.toLowerCase();
  }
  function isLetter(c) {
    return c.toLowerCase() !== c.toUpperCase();
  }
  function isNumber(c) {
    return c !== " " && !isNaN(Number(c));
  }

  const alphaNumerics = [...s].filter((c) => isLetter(c) || isNumber(c));

  let [left, right] = [0, alphaNumerics.length - 1];

  while (left <= right) {
    if (match(alphaNumerics[left], alphaNumerics[right])) {
      left++;
      right--;
    } else {
      return false;
    }
  }

  return true;
}

module.exports = isPalindrome;
