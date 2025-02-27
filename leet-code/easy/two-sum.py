def two_sum(nums: list, target: int):
	
    selected = {}

    for i, num in enumerate(nums):
        index = target - num

        if num in selected:
            return [selected[num], i]

        else:
            selected[index] = i

    return None
    

if __name__ == "__main__":
    nums = [1, 2, 3, 4, 5, 6]
    
    target = 9

    print(two_sum(nums, target))