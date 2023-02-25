# Uncomment the code below and fix the bug as described in the question.
# Underneath the fixed code, describe what the initial issue was and how
# you fixed it.


CONVERSION_RATE = 0.393701
def height_conversion(heights):
    #Make the list the same length as the input list
    heights_in_inches = [0] * len(heights)
    #was called idx, but the for loop was using i
    for i in range(0, len(heights)):
        converted_height = heights[i] * CONVERSION_RATE
        heights_in_inches[i] = converted_height
    return heights_in_inches


height_conversion([1, 2, 3, 4, 5])
