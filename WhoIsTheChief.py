"""
某小区发生盗窃案，有四个人嫌疑最大，警察找来讯问。

A说：不是我。

B说：是C。

C说：是D。

D说：他冤枉人。

四人中有一人说了假话
"""


suspects = "ABCD"
for killer in suspects:
    statements = 0
    # A: "不是我"  → 真当且仅当 killer != 'A'
    if killer != 'A':
        statements += 1
    # B: "是C"  → 真当且仅当 killer == 'C'
    if killer == 'C':
        statements += 1
    # C: "是D"  → 真当且仅当 killer == 'D'
    if killer == 'D':
        statements += 1
    # D: "他冤枉人" 意思是 'C 说的(是D)是假的' → 凶手不是D → 真当且仅当 killer != 'D'
    if killer != 'D':
        statements += 1
    if statements == 3:  # 四人中有一人说了假话，所以三人说了真话
        print(f"凶手是 {killer}")