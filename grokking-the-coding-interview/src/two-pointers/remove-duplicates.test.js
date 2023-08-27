const remove = require("./remove-duplicates");

describe("remove", () => {
  it("returns the number of unique elements in the array", () => {
    expect(remove([2, 3, 3, 3, 6, 9, 9])).toBe(4);
    expect(remove([2, 2, 2, 11])).toBe(2);
  });
});
