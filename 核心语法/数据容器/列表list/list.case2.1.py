#合并两个列表中的元素，并对合并的结果进行去重处理(去除列表中的重复元素)。
#if i not in 去重
num_list1 = [19,23,54,64,875,20,109,232,123,54]
num_list2 = [55,80,72,35,60,123,54,29,91]
#合并
num_list = [*num_list1,*num_list2]    #  * : 解包

new_list = []
for i in num_list:
    if i not in new_list:
        new_list.append(i)
print(f"合并后的原始列表：{num_list}")
print(new_list)