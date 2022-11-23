def read_silently(nums: list[int]) -> list[int]:
    lucky = []
    n = 1
    if len(nums) == 0:
        return lucky
    lucky.append(nums[0])
    if len(nums) == 1:
        return lucky
    while n + 1 < len(nums):
        if nums[n - 1] % 10 == nums[n + 1] % 10:
            n += 1
        else:
            lucky.append(nums[n])
            n += 1
    lucky.append(nums[n])
    return lucky


assert (read_silently([1, 2, 5, 12, 15]) == [1, 2, 15])
assert (read_silently([2, 4, 12, 14, 2, 8]) == [2, 2, 8])
assert (read_silently([2, 22, 222, 2222]) == [2, 2222])
assert (read_silently([10, 4, 0, 4, 7]) == [10, 4, 7])
assert (read_silently([999]) == [999])
assert (read_silently([]) == [])
assert (read_silently([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5])
assert (read_silently([490, 350]) == [490, 350])
assert (read_silently([95, 330, 475]) == [95, 475])
assert (read_silently([255, 75, 45, 80]) == [255, 45, 80])
assert (read_silently([240, 370, 10, 340, 60]) == [240, 60])
assert (read_silently([156, 116]) == [156, 116])
assert (read_silently([48, 168, 388]) == [48, 388])
assert (read_silently([144, 400, 100, 212]) == [144, 400, 100, 212])
assert (read_silently([332, 116, 36, 80, 40]) == [332, 116, 36, 80, 40])
