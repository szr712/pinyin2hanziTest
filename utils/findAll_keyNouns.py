

def findAll_keyNouns(pinyin, tones, subpinyin, subtones):
    index = []
    for i in range(0, len(pinyin)-len(subpinyin)+1):
        sub = pinyin[i:i+len(subpinyin)]
        if sub == subpinyin and tones[i:i+len(subpinyin)] == subtones:
            index.append(i)
    return index


if __name__ == "__main__":
    import sys
    sys.path.append("..")
    from Convertor import Convertor
    words = "【知识点】『互斥事件的概率加法公式互斥事件的概率加法公式』"
    convertor = Convertor()
    tar, sen = convertor.convert(words)
    sub, _ = convertor.convert("公式")
    print(sen)
    index = findAll_keyNouns(
        tar[0].pinyin, tar[0].yindiao, sub[0].pinyin, sub[0].yindiao)
    print(index)
    print(sen[0][index[0]:index[0]+2])
