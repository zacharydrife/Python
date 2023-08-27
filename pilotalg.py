'''
A pilot was asked to drop food packets in a terrain. He must fly over the entire terrain only once but cover a maximum number of drop points. The points are given as inputs in the form of integer coordinates in a two-dimensional field. The flight path can be horizontal or vertical, but not a mix of the two or diagonal.
Write an algorithm to find the maximum number of drop points that can be covered by flying over the terrain once.

Input
The first line of input consists of an integer - xCoordinate_size, representing the number of x coordinates (N).
The next line consists of N space-separated integers representing the x coordinates. 
The third line consists of an integer- yCoordinate_size, representing the number of y coordinates (M).
The next line consists of M space-separated integers representing the y coordinates.

Output
Print an integer representing the number of coordinates in the best path which covers the maximum number of drop points by flying over the terrain once.

Note
A path is a valid path if, more than one drop points are connected (single coordinates don't create any path, so the pilot cannot fly over it).

Constraints
1 < N, M <= 700 (where N is always equal to M)

Example
Input:
5
2 3 2 4 2
5
2 2 6 5 8

Output:
3

Explanation:
There are 5 coordinates - (2, 2), (3, 2), (2, 6), (4, 5), (2, 8).
The best path is the horizontal one covering (2, 2), (2, 6), (2, 8).
So the output is 3.

Input
4
1 2 2 3
4
2 3 4 5

Expected output 2
'''


"""
xCoordinate, represents the N coordinates on x-axis.
yCoordinate, represents the M coordinates on y-axis.
"""
def funcDrop(xCoordinate, yCoordinate):
    # Combine the coordinates
    coordinates = [(xCoordinate[i], yCoordinate[i]) for i in range(len(xCoordinate))]

    # Sort by x values
    coordinates.sort()

    max_count = 0

    # Count consecutive coordinates with the same x value
    i = 0
    while i < len(coordinates):
        count = 1
        while i + 1 < len(coordinates) and coordinates[i][0] == coordinates[i + 1][0]:
            count += 1
            i += 1
        max_count = max(max_count, count)
        i += 1

    # Sort by y values
    coordinates.sort(key=lambda coord: coord[1])

    # Count consecutive coordinates with the same y value
    i = 0
    while i < len(coordinates):
        count = 1
        while i + 1 < len(coordinates) and coordinates[i][1] == coordinates[i + 1][1]:
            count += 1
            i += 1
        max_count = max(max_count, count)
        i += 1

    return max_count

def main():
    xCoordinate_size = int(input())
    xCoordinate = list(map(int, input().split()))

    yCoordinate_size = int(input())
    yCoordinate = list(map(int, input().split()))

    result = funcDrop(xCoordinate, yCoordinate)
    print(result)

if __name__ == "__main__":
    main()
