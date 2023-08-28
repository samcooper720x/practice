class Solution:
    def longest_palindrome(s: str) -> str:
        if len(s) < 2:
            return s
        
        doubled_centres = []
        for i, char in enumerate(s):
            if not i < len(s) - 1:
                break

            if s[i+1] == char:
                doubled_centres.append(f'{char}{s[i+1]}'

        longest_found = ''

        for i, char in enumerate(s):
            if not i < len(s) - 1:  
                break

            palindrome = char

            left_ptr = i - 1
            right_ptr = i + 1

            while left_ptr >= 0 and right_ptr <= len(s) - 1:
                if s[left_ptr] != s[right_ptr]:
                    break

                palindrome = f'{s[left_ptr]}{palindrome}{s[right_ptr]}'
                left_ptr -= 1
                right_ptr += 1

            if len(palindrome) > len(longest_found):
                longest_found = palindrome

        for i, centre in enumerate(doubled_centres):

        return longest_found

# driver code for debugging
Solution.longest_palindrome('ccc')
