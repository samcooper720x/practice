"""
https://leetcode.com/explore/interview/card/top-interview-questions-easy/127/strings/879/
solved and tested in 22m 56s
"""
def reverse(s):
    forward_ptr = 0
    backward_ptr = len(s) - 1

    while forward_ptr < backward_ptr:
        temp_ptr = s[forward_ptr]
        s[forward_ptr] = s[backward_ptr]
        s[backward_ptr] = temp_ptr

        forward_ptr += 1
        backward_ptr -= 1

    return s
