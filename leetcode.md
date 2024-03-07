# Interview Crash Course, Data Structures and Algorithms

## Arrays and Strings
Arrays and strings are the most basic data structures. They are used to store data in a linear fashion. Arrays are used to store a collection of elements of the same type. Strings are used to store a collection of characters.

***

### Two Pointers
Two pointers is a technique that uses two pointers to solve problems. The two pointers can be used to solve problems that involve searching, sorting, and merging

pseduo code:
```python
function fn(arr):
    left = 0
    right = arr.length - 1

    while left < right:
        Do some logic here depending on the problem
        Do some more logic here to decide on one of the following:
            1. left++
            2. right--
            3. Both left++ and right--

    return something
```
Runtime: O(n), if work within the while loop is O(1)

Example:
Is string is a palindrome?
```python
function isPalindrome(s):
    left = 0
    right = s.length - 1

    while left < right:
        if s[left] != s[right]:
            return False
        left++
        right--

    return True
```

***

### Sliding Window
Sliding window is a technique that uses a window to solve problems. The window is used to solve problems that involve searching, sorting, and merging.

pseduo code:
```python
function fn(arr):
    left = 0
    right = 0

    while right < arr.length:
        Do some logic here depending on the problem
        right++

        while window needs to shrink:
            Do some logic here to shrink the window
            left++

    return something
```