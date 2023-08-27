const containsDuplicate = require("./contains-duplicate");

describe("containsDuplicate", () => {
  it("returns true when there are duplicates", () => {
    expect(containsDuplicate([1, 2, 3, 1])).toBe(true);
    expect(containsDuplicate([1, 1])).toBe(true);
  });

  it("returns false when there are no duplicates", () => {
    expect(containsDuplicate([1, 2, 3, 4])).toBe(false);
  });
});
