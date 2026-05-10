# -*- encoding: UTF-8 -*-

"""
输出所有n位整数中的回文数并统计个数
"""

string = str(input(""))
result = []
for i in range(len(string) - 1):
    for j in range(i + 1, len(string)):
        clip = string[i:j]
        if clip == clip[::-1] and (clip not in result):
            result.append(clip)
for i in result:
    print(i)
print("共{}个".format(len(result)))
