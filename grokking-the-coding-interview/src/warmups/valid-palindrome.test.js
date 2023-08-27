const isPalindrome = require("./valid-palindrome");

describe("isPalindrome", () => {
  it("returns true if s is a palindrome", () => {
    expect(isPalindrome("A man, a plan, a canal, Panama!")).toBe(true);
    expect(isPalindrome("Was it a car or a cat I saw?")).toBe(true);
  });

  it("returns false if s is not a palindrome", () => {
    expect(isPalindrome("12345")).toBe(false);
  });
});
