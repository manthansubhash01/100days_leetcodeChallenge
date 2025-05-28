######################################################################################
######################################################################################
'''
401. Binary Watch
Solved
Easy
Topics
premium lock iconCompanies
Hint

A binary watch has 4 LEDs on the top to represent the hours (0-11), and 6 LEDs on the bottom to represent the minutes (0-59). Each LED represents a zero or one, with the least significant bit on the right.

    For example, the below binary watch reads "4:51".

Given an integer turnedOn which represents the number of LEDs that are currently on (ignoring the PM), return all possible times the watch could represent. You may return the answer in any order.

The hour must not contain a leading zero.

    For example, "01:00" is not valid. It should be "1:00".

The minute must consist of two digits and may contain a leading zero.

    For example, "10:2" is not valid. It should be "10:02".

 

Example 1:

Input: turnedOn = 1
Output: ["0:01","0:02","0:04","0:08","0:16","0:32","1:00","2:00","4:00","8:00"]

Example 2:

Input: turnedOn = 9
Output: []

 

Constraints:

    0 <= turnedOn <= 10
'''
######################################################################################
######################################################################################
rows, cols = map(int, input().split())
    grid = [list(input()) for _ in range(rows)]
    visited = [[False] * cols for _ in range(rows)]
    total_eaten = 0
    for row in range(rows):
        if 'S' not in grid[row]:
            for col in range(cols):
                if not visited[row][col]:
                    visited[row][col] = True
                    total_eaten += 1
    for col in range(cols):
        if all(grid[row][col] != 'S' for row in range(rows)):
            for row in range(rows):
                if not visited[row][col]:
                    visited[row][col] = True
                    total_eaten += 1
    print(total_eaten)
