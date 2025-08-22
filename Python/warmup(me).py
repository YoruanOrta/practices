def max_number(nums):
    return max(nums)

def is_palindrome(s):
    return s == s[::-1]

def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

def the_longest_lenghth(sentence):
    words = sentence.split()
    return max (len(word) for word in words)

def reverse(n):
    return int(str(n)[::-1])

if __name__ == "__main__":

    nums = [1, 3, 5, 7, 9]
    print("Max number:", max_number(nums))

    s = "yoruan"
    print("Is palindrome:", is_palindrome(s))

    n = 18
    print("Factorial of", n, "is :", factorial(n))

    sentence = "Here testing my ability to write codes for my self"
    print("Longest word length:", the_longest_lenghth(sentence))

    n = 71106
    print("Reversed integer:", reverse(n))