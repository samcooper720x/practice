const isAnagram = require("./valid-anagram");

describe("isAnagram", () => {
  it("returns true if s is an anagram of t", () => {
    expect(isAnagram("listen", "silent")).toBe(true);
  });

  it("returns false if s is not an anagram of t", () => {
    expect(isAnagram("rat", "car")).toBe(false);
    expect(isAnagram("hello", "world")).toBe(false);
  });
});
