/*
 * 30-07-2023
 * Solved in 02:33
 */

// function checkIfPangram(sentence) {
//   const chars = [...sentence.replaceAll(" ", "").toLowerCase()];
//
//   const alphabet = [..."abcdefghijklmnopqrstuvwxyz"];
//
//   return alphabet.every((letter) => chars.includes(letter));
// }

function checkIfPangram(sentence) {
  let uniqueLetters = new Set();

  for (const letter of sentence) {
    if (letter.toLowerCase() !== letter.toUpperCase()) {
      uniqueLetters.add(letter.toLowerCase());
    }
  }

  return uniqueLetters.size === 26;
}

module.exports = checkIfPangram;
