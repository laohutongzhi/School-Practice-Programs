# setsomething
"""
输入两个集合，求它们的并集和交集
"""

a = set("abracadabra")
b = set("alacazam")

union_ab = a | b  # 并集
print("a 并 b =", union_ab)
intersection_ab = a & b  # 交集
print("a 交 b =", intersection_ab)
