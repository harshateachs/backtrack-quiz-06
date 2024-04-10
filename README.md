# Backtrack Quiz 06

**Question:**

You're provided with two lists of integers, `list1` and `list2`, each containing distinct elements. Your task is to implement a function called `list_operations` that performs various operations on these lists and returns the result.

The function should support the following operations:

1. **Merge**: Merge the two lists into a single list, maintaining the order of elements.

2. **Remove Duplicates**: Remove any duplicate elements that may arise from merging the lists.

3. **Sort**: Sort the merged list in ascending order.

4. **Reverse**: Reverse the order of elements in the merged list.

Your function should take a list of operations as input and perform them in the order specified. Each operation is represented by a character:
- `'M'`: Merge
- `'R'`: Remove Duplicates
- `'S'`: Sort
- `'V'`: Reverse

**Function Signature:**
```python
def list_operations(list1: List[int], list2: List[int], operations: str) -> List[int]:
    pass
```

**Input:**
- Two lists of integers, `list1` and `list2`, each containing distinct elements.
- A string `operations` containing a sequence of characters representing the operations to be performed.

**Output:**
- Return the final list after performing the specified operations.

**Examples:**
```python
assert list_operations([1, 3, 2], [4, 3, 5], 'MRS') == [1, 2, 3, 4, 5]
assert list_operations([7, 5, 3], [4, 2, 1], 'RMV') == [7, 5, 4, 3, 2, 1]
```

**Submission Guidelines:**
- Clone the repository.
- Create a separate branch using the format `<name>`.
- Implement the code within the specified time limit of 15 minutes.
- Push the changes to your branch.
- Open a merge request to the main branch.

**Note:**
- Ensure that your implementation is correct by testing it with various input cases, including edge cases.
- You can use internet browsing during the implementation process.
- Avoid using AI tools like ChatGPT, Bard, etc.