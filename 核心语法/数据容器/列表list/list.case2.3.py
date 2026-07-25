#合并两个列表中的元素，并对合并的结果进行去重处理(去除列表中的重复元素)。
#转换成dict(字典)去重(保留顺序，底层是哈希表)
num_list1 = [19,23,54,64,875,20,109,232,123,54]
num_list2 = [55,80,72,35,60,123,54,29,91]
#合并
merged = num_list1 + num_list2
print(f"合并后的原始列表：{merged}")
new_list = list(dict.fromkeys(merged))
print(f"调试输出:{dict.fromkeys(merged)}")#调试输出
print(new_list)