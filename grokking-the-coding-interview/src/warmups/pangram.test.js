const checkIfPangram = require("./pangram");

describe("checkIfPangram", () => {
  it("returns true if pangram", () => {
    expect(checkIfPangram("TheQuickBrownFoxJumpsOverTheLazyDog")).toBe(true);
  });

  it("returns false if not a pangram", () => {
    expect(checkIfPangram("This is not a pangram")).toBe(false);
  });
});
