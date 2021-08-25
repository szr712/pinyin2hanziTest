import time
import traceback
import requests
from utils.diff import diff

proxies = {'https': 'http://127.0.0.1:7078'}


def adjust_pre_len(pre_pinyin, text_pinyin, pre_result):
    try:
        flag=0
        if len(pre_pinyin) == len(text_pinyin):
            return pre_result
        differences = list(diff(pre_pinyin, text_pinyin))
        for i1, i2, j1, j2, a, b in differences:
            if len(a) != len(b):
                sub=""
                for word in b:
                    data_dict = {
                        'text': word,
                        'itc': "zh-t-i0-pinyin",
                        'num': 10,
                        'ie': "utf-8",
                        'oe': "utf-8' -H 'content-length:0'",
                    }
                    # response = requests.post(
                    #     url='https://inputtools.google.com/request', data=data_dict, proxies=proxies)
                    response = requests.post(
                        url='https://inputtools.google.com/request', data=data_dict)
                    candidates = response.json()[1][0][1]
                    for candidate in candidates:
                        if len(candidate) == 1:
                            sub=sub+candidate
                            break
                pre_result=pre_result[:j1]+sub+pre_result[j1+len(a):]
    except Exception as e:
        flag += 1
        traceback.print_exc()
        print("Error")
        print(flag)
        if flag == 10:
            return ""
        time.sleep(1)
    if len(pre_result)>len(text_pinyin):
        pre_result=pre_result[:len(text_pinyin)]
    return pre_result
