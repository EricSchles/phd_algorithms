from typing import List
def linear_search(arr: List, value: int) -> int:
    for index, element in enumerate(arr):
        if element == value:
            return index
    else:
        return None

# Loop invariant:

# The subarray - A[0..i-1] does not contain the value
# Proof of loop invariant:

# 1. Initialization:

# We start by showing that the loop invariant holds before the first loop iteration, when index == 0.  At this point we only need to inspect A[index] == value.  If this is true then index with value 0 is returned. Otherwise we go through the iteration.

# 2. Maintenance: Next, we tackle the second property: showing that each iteration maintains the loop invariant.  The body of the for loop just checks if each element has A[index] == value, and then returns the index if the boolean is true.

# 3. Termination: Finally, we examine what happens when the loop terminates.  If any of the array values equaled the value we were looking for, then the index is returned.  Otherwise None is returned.  Since we are using a for-loop, termination is guaranteed when the number of elements runs out.


