# HowManyWordsInSentence
"""
输入一句英文单词组成的句子，统计各单词的出现的次数和出现次数最多的单词及其次数。
"""

punctuation = r"""!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"""


def is_sentence(inputS):
    if len(inputS) == 0:
        return False
    for i in inputS:
        if not (i.isalpha() or i.isspace() or i in punctuation):
            return False
    return True


while inSentence := str(input("输入一句英文句子：")):
    if is_sentence(inSentence):
        break
    else:
        print("输入有问题，再次输入")
inSentence = inSentence.lower()
inWords = inSentence.split()
wordlist = {}
for i in inWords:
    if i in wordlist:
        wordlist[i] += 1
    else:
        wordlist[i] = 1
sorted_wordlist = sorted(wordlist.items(), key=lambda x: x[1], reverse=True)
for i in sorted_wordlist:
    print(i[0], ":", i[1])
