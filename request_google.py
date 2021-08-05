import time
import traceback

import pypinyin
from utils.wenzi2pinyin import wenzi2pinyin
from utils.tone_equal import tone_equal

import requests
from pypinyin import Style, lazy_pinyin,pinyin

proxies = {'https': 'http://127.0.0.1:7078' }


def requset_google(py_list, tones_list):
    if not py_list:
        return ""
    item_pinyin = "".join(str(v) for v in py_list)
    data_dict = {
        'text': item_pinyin,
        'itc': "zh-t-i0-pinyin",
        'num': 10,
        'ie': "utf-8",
        'oe': "utf-8' -H 'content-length:0'",
    }
    flag = 1
    while flag:
        try:
            # response = requests.post(
            #    url='https://inputtools.google.com/request', data=data_dict, proxies=proxies)
            response = requests.post(
                url='https://inputtools.google.com/request', data=data_dict)
            flag = 0
        except Exception as e:
            traceback.print_exc()
            print("Error")
            time.sleep(1)
            
    candidates = response.json()[1][0][1]
    result = candidates[0]

    result_pinyin = pinyin(result, style=Style.TONE3)
    result_tones = [int(py[0][-1]) if py[0][-1].isdigit() else 0 for py in result_pinyin]

    if not tone_equal(result_tones, tones_list):
        for j in range(1, len(candidates)):
            candidate = candidates[j].replace('\'', '')
            pre_len = len(candidate)
            if not tone_equal(result_tones[:pre_len], tones_list[:pre_len]):
                candidate_pinyin = pinyin(candidate, style=Style.TONE3)
                candidate_tones = [int(py[0][-1]) if py[0][-1].isdigit() else 0 for py in candidate_pinyin]
                if tone_equal(candidate_tones, tones_list[:pre_len]):
                    result = candidate
                    break

    return result + requset_google(py_list[len(result):], tones_list[len(result):])



if __name__ == "__main__":
    string = "究发现酸的浓度越大，产生气体的速度越快，与甲比较，对丁分析正确的是    （填编号）。"
    pinyin_list,tones_list=wenzi2pinyin(string)
    # print(pinyin_list)
    print(requset_google(pinyin_list,tones_list))
