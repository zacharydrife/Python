'''

Ray , Shiv, and Ansh are conducting a survey for a group of people. The survey is only meant for twins but there are certain people who are not twins and wanting to take part in the survey.
Write an algorithm to help them identify the person from the given input who is not a twin.

Input
The first line of input consists of an integer - inputArr_size, representing the number of entries in the array (N).
The next line consists of N space-separated integer elements in the array.

Output
Print the smallest value of the person whi is not a twin from the given array of elements.

Note
If everyone present is a twin, then return -1.

Examples
Example 1:
Input:
7
1 1 2 3 3 4 4
Output:
2

Explanation:
In the given array of the element, the only non-twin element is '2'.
So, the output is 2.

Example 2:
Input: 
4
1 1 2 2 
Output:
-1

Explanation:
Given array of element contain all the twin elements.
So, the output is -1.
'''


"""
inputArr, represents the given array of element of size inputArr_size.
"""

"""
inputArr, represents the given array of element of size inputArr_size.

"""
def funcTwins(inputArr):
	# Write your code here
	counts = {}

	# Count the occurerences of each element
	for num in inputArr:
		if num in counts:
			counts[num] += 1
		else:
			counts[num] = 1
	
	non_twin = -1

	# Find the element that is not a twin
	for num, count in counts.items():
		if count == 1:
			non_twin = num
			break

	return non_twin

def main():
	#input for inputArr
	inputArr = []
	inputArr_size  = int(input())
	inputArr = list(map(int,input().split()))
	
	
	result = funcTwins(inputArr)
	print(result)	

if __name__ == "__main__":
	main()