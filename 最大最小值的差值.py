def difference_max_min(list_nums):
    x = max(list_nums)
    y = min(list_nums)
    return x-y
    
# 输入整数，并将其转换为列表
numbers = list(map(int, input().split()))

# 调用函数
print(difference_max_min(numbers))
