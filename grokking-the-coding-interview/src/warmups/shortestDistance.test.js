const shortestDistance = require("./shortestDistance");

describe("shortestDistance", () => {
  it("returns the smallest number of words between two words in a sentence", () => {
    expect(
      shortestDistance(
        ["the", "quick", "brown", "fox", "jumps", "over", "the", "lazy", "dog"],
        "fox",
        "dog",
      ),
    ).toBe(5);

    expect(shortestDistance(["a", "c", "d", "b", "a"], "a", "b")).toBe(1);

    expect(shortestDistance(["a", "b", "c", "d", "e"], "a", "e")).toBe(4);
  });
});
