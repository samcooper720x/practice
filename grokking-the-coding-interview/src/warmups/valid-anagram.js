/*
 * 30-07-2023
 * Solved in 27:56
 */

// function isAnagram(s, t) {
//   if (s.length !== t.length) {
//     return false;
//   }
//
//   const [sChars, tChars] = [new Map(), new Map()];
//
//   [...s].forEach((c) => {
//     const seenTimes = sChars.get(c);
//
//     if (seenTimes) {
//       sChars.set(c, seenTimes + 1);
//     } else {
//       sChars.set(c, 1);
//     }
//   });
//
//   [...t].forEach((c) => {
//     const seenTimes = tChars.get(c);
//
//     if (seenTimes) {
//       tChars.set(c, seenTimes + 1);
//     } else {
//       tChars.set(c, 1);
//     }
//   });
//
//   for (const [k, v] of sChars.entries()) {
//     const tv = tChars.get(k);
//
//     if (!tv || tv !== v) {
//       return false;
//     }
//   }
//
//   return true;
// }

function isAnagram(s, t) {
  if (s.length !== t.length) {
    return false;
  }

  const charCounts = new Map();

  [...s].forEach((c) => {
    const entry = charCounts.get(c);

    if (entry) {
      const seenTimes = entry.c;
      charCounts.set(c, { ...entry, s: seenTimes + 1 });
    } else {
      charCounts.set(c, { s: 1 });
    }
  });

  [...t].forEach((c) => {
    const entry = charCounts.get(c);

    if (entry) {
      charCounts.set(c, { ...entry, t: entry.t ? entry.t + 1 : 1 });
    } else {
      return false;
    }
  });

  for (const counts of charCounts.values()) {
    if (counts.s !== counts.t) {
      return false;
    }
  }

  return true;
}

module.exports = isAnagram;
