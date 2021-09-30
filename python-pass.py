def printSubStr(str, low, high):
    for i in range(low, high + 1):
        print(str[i], end="")


class solution:
    @staticmethod
    def longest_palindromic(s : str)-> str:
        n = len(s)

        maxLength = 1
        start = 0

        for i in range(n):
            for j in range(i, n):
                flag = 1

                # Check palindrome
                for k in range(0, ((j - i) // 2) + 1):
                    if (s[i + k] != s[j - k]):
                        flag = 0

                # Palindrome
                if (flag != 0 and (j - i + 1) > maxLength):
                    start = i
                    maxLength = j - i + 1

        printSubStr(s, start, start + maxLength - 1)
        return str(maxLength)

        pass


 print("\nLength is: ",solution.longest_palindromic("babad"))
    print("\nLength is: ",solution.longest_palindromic("cbbd"))
    print("\nLength is: ",solution.longest_palindromic("a"))
    print("\nLength is: ",solution.longest_palindromic("ac"))
