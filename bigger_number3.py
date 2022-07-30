def next_bigger(number: int) -> int:
    # Let's convert the number to a list so we can traverse it easily

    nums = list(map(int, str(number)))
    print(f"Original nums: {nums}")

    """ 
    Example input: 534976
    Expected result is: 536974 
    """

    """ 
    Step 1:
        * From right to left, find pair of digits where
        current R < L
        * Example: 74 -> no; 97 -> no; 69 -> Yes
    """

    last_index = len(nums) - 1
    target_index = last_index
    while target_index >= 0:
        if nums[target_index - 1] < nums[target_index]:
            # We found our pair
            break

        # Move index to the left
        target_index -= 1

    print(
        f"Found our index pair: target_index {target_index}. \n"
        f"target value: {nums[target_index-1]}{nums[target_index]}"
    )

    """
    Step 2: Swap target index minus 1 value with one
    """
    nums[target_index - 1], nums[last_index] = (
        nums[last_index],
        nums[target_index - 1],
    )
    print(f"Swapped values: {nums}")

    """ 
    Step 3: Sort numbers after the swapped index
    """
    nums[target_index:] = sorted(nums[target_index:])
    print(f"Sorted values: {nums}")

    return int("".join([str(i) for i in nums]))


if __name__ == "__main__":
    next_bigger(534976)
