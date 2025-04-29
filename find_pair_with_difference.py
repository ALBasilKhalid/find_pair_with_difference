#ALBASIL AL-RAWAHI      
"""
Algorithm:
Define a function binary_search(arr, target) that implements binary search to find if the target element exists in the sorted array 'arr'.
Return True if found, False otherwise.

In the main() function:
a. Accept input for the array 'arr' and the value of 'n'.
b. Initialize a boolean variable 'found' to False.
c. Iterate through the elements of the array 'arr':
    i. For each element 'arr[i]', check if there exists an element in the array that is equal to 'arr[i] + n' using the binary_search() function.
    ii. If such an element is found, print the pair and set 'found' to True. Exit the loop.
d. If no pair is found, print that the pair does not exist.

Call the main() function to execute the code.

    
    
Test cases:
1)
Enter the elements of the array separated by space: 5 20 3 2 50 80

Enter the value of n: 78

Given: arr[] = [5, 20, 3, 2, 50, 80] , n = 78
Result: Pair Identified: (2, 80)

2)
Enter the elements of the array separated by space: 90 70 20 80 50

Enter the value of n: 45

Given: arr[] = [90, 70, 20, 80, 50] , n = 45
Result: Pair Does Not Exist
"""
#This is the usale binary search we use
def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = left + (right - left) // 2
        
        if arr[mid] == target:
            return True
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return False

def main():
    # Accept input for the array 'arr' and the value of 'n'
    arr = [int(x) for x in input("Enter the elements of the array separated by space: ").split()]
    n = int(input("Enter the value of n: "))
    
    found = False  # Initialize a boolean variable to track if a pair is found
    
    # Iterate through each element in the array
    for i in range(len(arr)):
        # Check if there exists an element in the array that is equal to 'arr[i] + n'
        if binary_search(arr, arr[i] + n):
            # If such an element is found, print the pair and set 'found' to True
            print()
            print("Given: arr[] =", arr, ", n =", n)
            print("Result: Pair Identified:", (arr[i], arr[i] + n))
            found = True
            break  # Exit the loop once a pair is found

    # If no pair is found, print that the pair does not exist
    if not found:
        print()
        print("Given: arr[] =", arr, ", n =", n)
        print("Result: Pair Does Not Exist")

# Call the main function to execute the code
main()

