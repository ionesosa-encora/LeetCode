def distinctDifferenceArray(nums):
    result = []
    
    prefix_set = set()
    suffix_set = set(nums)
    
    for i in range(len(nums)):
        prefix_set.add(nums[i])
        
        suffix_set.discard(nums[i])
        
        result.append(len(prefix_set) - len(suffix_set))
    
    return result

print(distinctDifferenceArray([1, 2, 3, 4, 5]))  # Debería imprimir [-3, -1, 1, 3, 5]
print(distinctDifferenceArray([3, 2, 3, 4, 2]))  # Debería imprimir [-2, -1, 0, 2, 3]
