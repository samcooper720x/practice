const mySqrt = require("./sqrt");

describe("mySqrt", () => {
  it("returns the square root", () => {
    expect(mySqrt(8)).toBe(2);
    expect(mySqrt(4)).toBe(2);
    expect(mySqrt(2)).toBe(1);
    expect(mySqrt(1)).toBe(1);
    expect(mySqrt(27)).toBe(5);
  });
});
