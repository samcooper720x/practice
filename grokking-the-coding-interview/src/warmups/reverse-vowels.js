/*
 * 30-07-2023
 * Solved in 17:07
 */

// function reverseVowels(s) {
//   function isVowel(c) {
//     return ["a", "e", "i", "o", "u"].includes(c.toLowerCase());
//   }
//
//   let [leftWord, rightWord] = ["", ""];
//   let [left, right] = [0, s.length - 1];
//
//   while (left <= right) {
//     const leftVowel = isVowel(s[left]);
//     const rightVowel = isVowel(s[right]);
//
//     if (left === right) {
//       return leftWord + s[left] + rightWord;
//     } else if (leftVowel && rightVowel) {
//       leftWord = leftWord + s[right];
//       rightWord = s[left] + rightWord;
//       left++;
//       right--;
//     } else if (leftVowel) {
//       rightWord = s[right] + rightWord;
//       right--;
//     } else if (rightVowel) {
//       leftWord = leftWord + s[left];
//       left++;
//     } else {
//       leftWord = leftWord + s[left];
//       rightWord = s[right] + rightWord;
//       left++;
//       right--;
//     }
//   }
//
//   return leftWord + rightWord;
// }

function reverseVowels(s) {
  function isVowel(c) {
    return ["a", "e", "i", "o", "u"].includes(c.toLowerCase());
  }

  let vowels = [...s].filter(isVowel);

  return [...s]
    .map((c) => {
      if (isVowel(c)) {
        return vowels.pop();
      } else {
        return c;
      }
    })
    .join("");
}

module.exports = reverseVowels;
