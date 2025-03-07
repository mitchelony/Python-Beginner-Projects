# Problem 1: Balanced Art Collection
# As the curator of an art gallery, you are organizing a new exhibition.
# You must ensure the collection of art pieces are balanced to attract the right range of buyers. 
# A balanced collection is one where the difference between the maximum and minimum value of the art pieces is exactly 1.

# Given an integer array art_pieces representing the value of each art piece, 
# write a function find_balanced_subsequence() that returns the length of the longest balanced subsequence.

# A subsequence is a sequence derived from the array by deleting some or no elements without changing the order of the remaining elements.
#Example 1 Explanation:  The longest balanced subsequence is [3,2,2,2,3].

# art_pieces1 = [1,3,2,2,5,2,3,7]
# sorted = [1,2,2,2,3,3,5,7]
# lst = []
# length = 4

#sort the list
#use a for loop to iterate over
#we use the var to check the diff beteween the others
#when the diff <= 1 we raise count by 1

def find_balanced_subsequence(lst):
    sorted = lst.sort
    max_count = 0
    for i in range(len(sorted)):
        current_count = 0
        for j in sorted:
            if j-sorted[i] <= 1:
                current_count += 1
        if current_count > max_count:
            current_count = max_count
    return max_count

print(find_balanced_subsequence([1,3,2,2,5,2,3,7]))