def isPalindrome(string):
    left, right = 0, len(string) - 1
    while right >= left:
        if not string[left] == string[right]:
            return False
        left += 1;right -= 1
        return True

string_one = 'nurses run'
print(isPalindrome(string_one))

print(isPalindrome('redrum murder'))