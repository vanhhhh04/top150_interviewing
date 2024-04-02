# Example 1:

# Input: s = "A man, a plan, a canal: Panama"
# Output: true
# Explanation: "amanaplanacanalpanama" is a palindrome.
# Example 2:

# Input: s = "race a car"
# Output: false
# Explanation: "raceacar" is not a palindrome.
# Example 3:

# Input: s = " "
# Output: true
# Explanation: s is an empty string "" after removing non-alphanumeric characters.
# Since an empty string reads the same forward and backward, it is a palindrome.
def check_valid_palindrome(s):
    i = 0
    j = len(s) - 1
    d = 0
    while True :
        if i == j or i > j :
            return True
        else :
            if s[i] == s[j] :
                i += 1
                j -= 1
            else :
                return False

s= " "
print(check_valid_palindrome(s))

def test(strs):
    # Use a list comprehension to check if each string in 'strs' is a palindrome (reads the same forwards and backwards)
    return [s == s[::-1] for s in strs]

