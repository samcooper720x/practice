const search = require("./pair-with-target-sum");

describe("search", () => {
  it("returns indices of a pair that add up to the target sum", () => {
    expect(search([1, 2, 3, 4, 6], 6)).toStrictEqual([1, 3]);
    expect(search([2, 5, 9, 11], 11)).toStrictEqual([0, 2]);
  });
});
