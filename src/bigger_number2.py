def next_bigger(number: int) -> int:
    print(f"number: {number}")

    nums = list(str(number))
    left_index = len(nums) - 2

    print(f"nums: {nums}")
    print(f"left_index: {left_index}")
    while left_index >= 0 and nums[left_index + 1] <= nums[left_index]:
        print(
            f"left_index: {left_index}; nums[left_index + 1]: {nums[left_index + 1]}; nums[left_index]: {nums[left_index]}"
        )
        left_index -= 1

    if left_index >= 0:
        right_index = len(nums) - 1
        print(f"right_index: {left_index}")
        while nums[right_index] <= nums[left_index]:
            right_index -= 1
            print(
                f"right_index: {right_index}; nums[right_index]: {nums[right_index]}; nums[left_index]: {nums[left_index]}"
            )

        print(
            f"swapping; right_index: {right_index} ({nums[right_index]}); left_index: {left_index} ({nums[left_index]})"
        )
        swap_number(nums, right_index, left_index)

    print(f"reversing")
    reverse(nums, left_index + 1)

    answer = int("".join(nums))
    if answer <= number:
        return -1

    return answer


def swap_number(nums: list, right_index: int, left_index: int):
    nums[right_index], nums[left_index] = nums[left_index], nums[right_index]


def reverse(nums, right_index):
    left_index = len(nums) - 1
    while right_index < left_index:
        swap_number(nums, right_index, left_index)
        right_index += 1
        left_index -= 1


if __name__ == "__main__":
    print("------------3142", next_bigger(3142))
    print("------------12", next_bigger(12))
    print("------------513", next_bigger(513))
    print("------------2017", next_bigger(2017))
    print("------------9", next_bigger(9))
    print("------------111", next_bigger(111))
    print("------------531", next_bigger(531))
    print("------------123456789", next_bigger(123456789))
