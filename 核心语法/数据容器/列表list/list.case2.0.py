#合并两个列表中的元素，并对合并的结果进行去重处理(去除列表中的重复元素)。
#双重循环去重
num_list1 = [19,23,54,64,875,20,109,232,123,54]
num_list2 = [55,80,72,35,60,123,54,29,91]
#合并
for i in num_list2:
    num_list1.append(i)
print(f"合并后的原始列表：{num_list1}")
new_list = []
for num in range(len(num_list1)):
    is_duplicate = False
    for i in range(num + 1,len(num_list1)):
        if num_list1[num] == num_list1[i]:
            is_duplicate = True
            break
    if not is_duplicate:
        new_list.append(num_list1[num])
print(new_list)