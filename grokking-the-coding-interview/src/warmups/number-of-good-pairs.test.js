const numGoodPairs = require("./number-of-good-pairs");

describe("numGoodPairs", () => {
  it("returns the number of good pairs", () => {
    expect(numGoodPairs([1, 2, 3, 1, 1, 3])).toBe(4);
    expect(numGoodPairs([1, 1, 1, 1])).toBe(6);
  });

  it("returns 0 if no number repeats", () => {
    expect(numGoodPairs([1, 2, 3])).toBe(0);
  });
});
