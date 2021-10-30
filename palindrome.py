def isPalindrome(input):
    print(input)
    strng = input.upper().replace(' ', '')
    if len(strng) == 0:
        return True
    if strng[0] != strng[len(strng) - 1]:
        return False
    return isPalindrome(strng[1:-1])


print(isPalindrome('anita la gorda lagartona no traga la droga latina'))
