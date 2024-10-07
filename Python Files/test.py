def sum67(nums):
  if len(nums) == 0:
    return 0
  result = 0
  index = 0
  for i in nums:
    if i == 6:
      bad_index = index
      nums[bad_index] = 0
    if bad_index < (len(nums)-1):
      while i != 7:
        nums[index] = 0
          
      
    result += nums[index]
    index += 1
  return result
  
sum67([1, 2, 2, 6, 99, 99, 7])
