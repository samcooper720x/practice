const reverseVowels = require("./reverse-vowels");

describe("reverseVowels", () => {
  it("reverses vowels", () => {
    expect(reverseVowels("AEIOU")).toBe("UOIEA");
    expect(reverseVowels("hello")).toBe("holle");
    expect(reverseVowels("DesignGUrus")).toBe("DusUgnGires");
  });
});
