Technical Log for Problem: Find the Distinct Difference Array
Overview:
This problem asks us to compute the distinct difference array of a given array nums. The distinct difference array diff at index i is calculated as the number of distinct elements in the prefix (nums[0, ..., i]) minus the number of distinct elements in the suffix (nums[i + 1, ..., n - 1]). Our goal is to return this diff array for the input nums.

Context:
We are tasked with calculating, for each index i, how the distinct elements in the prefix compare to the distinct elements in the suffix. The main challenge is efficiently managing the distinct elements in both the prefix and suffix at every step of the iteration. We use sets to store distinct elements, which allow us to handle duplicates effectively, ensuring we calculate only the unique elements at each step.

Solution:

We initialize an empty list result to store the distinct difference values for each index.

A set prefix_set is used to track the distinct elements in the prefix (nums[0, ..., i]).

A set suffix_set is initialized with all elements of nums to represent the distinct elements in the suffix (nums[i + 1, ..., n - 1]).

As we iterate through each index i:

The current element nums[i] is added to prefix_set, as it is now part of the prefix.
The current element is removed from suffix_set, as it no longer belongs to the suffix.
The difference at index i is computed as the size of prefix_set minus the size of suffix_set, and this value is appended to the result list.
This process ensures that for each index i, we correctly compute the distinct difference between the prefix and suffix.

Alternative Solutions:

One alternative could involve recalculating the distinct elements for both the prefix and suffix in each iteration using list slicing. However, this would significantly increase time complexity due to repeated operations on slices of the array.
Another option could involve creating two separate counters to maintain the frequency of elements in both the prefix and suffix. This might reduce some memory overhead compared to using sets, but it would require more complex handling of element counts.
