"""
https://leetcode.com/explore/interview/card/top-interview-questions-easy/127/strings/883/
solved in 32m 28s
slow because had to filter for alphanumerics, need to learn this filter method
"""

def isPalindrome(s: str) -> bool:
    s = s.lower()
    
    alphanumeric_filter = filter(str.isalnum, s)
    s = "".join(alphanumeric_filter)

    fwd_ptr = 0
    bwd_ptr = len(s) - 1

    while fwd_ptr < bwd_ptr:
        if s[fwd_ptr] != s[bwd_ptr]:
            return False

        fwd_ptr += 1
        bwd_ptr -= 1
    
    return True
