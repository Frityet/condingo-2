"""
This function takes in a list of numbers and returns the 
average of all the numbers rounded down.

Arguments:
    list_of_nums (List[int] Array of integers): A list of the numbers
Returns:
    the median of all numbers in the list
Examples:
    [1,2,3,4] => 2.5
    [6,4,1,2,3,5] => 3.5
    [100,35,70] => 70
Notes:
    - You can assume that the list is not empty
"""


def median_of_list(list_of_nums: [int]) -> int:
    """
    if #list_of_nums % 2 == 0 then calculate the average of the two middle numbers
    else return the middle number
    """
    list_of_nums.sort()
    return (list_of_nums[len(list_of_nums) // 2] + list_of_nums[len(list_of_nums) // 2 - 1]) / 2 if len(list_of_nums) % 2 == 0 else list_of_nums[len(list_of_nums) // 2]