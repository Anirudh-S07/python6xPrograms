def is_palindrome(s):
    if s == s[::-1]:
        print("is Palindrome")
        return True
    else:
        print("Not a Palindrome")
        return False


is_palindrome("ada")


