
def isPalindrome(x):
        palindrome =""
        xvalue=str(x)

        for i in range(len(xvalue)-1,-1,-1):
         palindrome += xvalue[i]
         print("plaintramas",palindrome)
         print("x value",x)
        return palindrome == xvalue

print(isPalindrome(121))
# print(isPalindrome(10))
# print(isPalindrome(123))
