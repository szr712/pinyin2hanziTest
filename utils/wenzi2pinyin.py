from re import S
from pypinyin import Style, pinyin
from pypinyin.core import lazy_pinyin


def wenzi2pinyin(text):
    pinyin_list = lazy_pinyin(text, style=Style.TONE3)
    # print(pinyin_list)
    tones_list = [int(py[-1]) if py[-1].isdigit()
                  else 0 for py in pinyin_list]
    pinyin_list = lazy_pinyin(text, style=Style.NORMAL)
    return pinyin_list, tones_list
