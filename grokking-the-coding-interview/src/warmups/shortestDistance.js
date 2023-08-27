/*
 * 31-07-2023
 * Solved in 24:28
 */

// function shortestDistance(words, word1, word2) {
//   let fromWord1 = 0;
//   let fromWord2 = 0;
//   let shortestDistance = words.length - 1;
//
//   for (const word of words) {
//     if (word === word1 && fromWord2 > 0) {
//       if (fromWord2 < shortestDistance) {
//         shortestDistance = fromWord2;
//       }
//
//       fromWord2 = 0;
//     } else if (word === word2 && fromWord1 > 0) {
//       if (fromWord1 < shortestDistance) {
//         shortestDistance = fromWord1;
//       }
//
//       fromWord1 = 0;
//     }
//
//     if (word === word1) {
//       fromWord1 = 1;
//     } else if (word === word2) {
//       fromWord2 = 1;
//     } else if (fromWord1 > 0) {
//       fromWord1++;
//     } else if (fromWord2 > 0) {
//       fromWord2++;
//     }
//   }
//
//   return shortestDistance;
// }

function shortestDistance(words, word1, word2) {
  let [pos1, pos2] = [null, null];
  let shortestDistance = words.length;

  for (const [i, word] of words.entries()) {
    if (word === word1) {
      pos1 = i;
    } else if (word === word2) {
      pos2 = i;
    }

    if (pos1 !== null && pos2 !== null) {
      shortestDistance = Math.min(shortestDistance, Math.abs(pos1 - pos2));
    }
  }

  return shortestDistance;
}

module.exports = shortestDistance;
