import os
import difflib
from utils.adjust_pre_len import adjust_pre_len
from utils.diff import diff
from pypinyin import pinyin
import pypinyin
from utils.wenzi2pinyin import wenzi2pinyin
from tqdm import tqdm


def restore_result(preFileDir, oriFileDir, restoreFileDir):
    for oriFile in os.listdir(oriFileDir):
        with open(os.path.join(oriFileDir, oriFile), "r", encoding="utf-8") as fw:
            oriContents = fw.readlines()
        with open(os.path.join(preFileDir, oriFile+"pre.txt"), "r", encoding="utf-8")as fw:
            preContents = fw.readlines()

def test_result_len_equal(preFileDir,textFileDir):
    total=0
    notEqual=0
    for preFile in os.listdir(preFileDir):
        with open(os.path.join(preFileDir, preFile), "r", encoding="utf-8")as fw:
            preContents = fw.readlines()
        with open(os.path.join(textFileDir, preFile[:-7]+"_text.txt"), "r", encoding="utf-8")as fw:
            textContents = fw.readlines()
        for pre,text in zip(preContents,textContents):
            total+=1
            if len(pre)>len(text):
                notEqual+=1
                print("pre:{}text:{}".format(pre,text))
        print("total:{} notEqual:{}".format(total,notEqual))

# def diff(a, b):
#     for tag, i1, i2, j1, j2 in difflib.SequenceMatcher(a=a, b=b).get_opcodes():
#         if tag!='equal':
#             yield a[i1:i2], b[j1:j2]


# def adjust_pre_len(preList,textList):
#     for pre,text in zip(preList,textList):
#         # for a,b in zip(pre,text):
#             # aList=pinyin(a,heteronym=True,style=pypinyin.NORMAL)
#             # bList=pinyin(b,heteronym=True,style=pypinyin.NORMAL)
#             # flag=0
#             # for i in bList[0]:
#             #     if i in aList[0]:
#             #         flag=1
#             #         break
#             # if not flag:
#             #     print("pre:{}text:{}".format(pre,text))
#             #     print("a:{} b:{}".format(a,b))
#         pre_pinyin, _ = wenzi2pinyin(pre)
#         text_pinyin,_=wenzi2pinyin(text)
#         # if len(pre)==len(text):

#         if pre_pinyin!=text_pinyin:
#             print("pre:{}text:{}".format(pre,text))
#             # print("a:{} b:{}".format(a,b))
#             result=list(diff(pre_pinyin,text_pinyin))
#             print(result)
#             # for a,b in zip(pre_pinyin,text_pinyin):
#             #     if a!=b:
#             #         print("pre:{}text:{}".format(pre,text))
#             #         print("a:{} b:{}".format(a,b))
#             #         result=list(diff(a,b))
#             #         print(result)
        

if __name__=="__main__":
    test_result_len_equal("./preFile","./textFile")
    # for preFile in os.listdir("./preFile"):
    #     with open(os.path.join("./preFile", preFile), "r", encoding="utf-8")as fw:
    #         preContents = fw.readlines()
    #     with open(os.path.join("./textFile", preFile[:-7]+"_text.txt"), "r", encoding="utf-8")as fw:
    #         textContents = fw.readlines()
    #     for pre,text in zip(preContents,textContents):
    #         pre=pre.replace("\n", "")
    #         oripre=pre
    #         text=text.replace("\n", "")
        # pre = "应满足饥饿的饥饿解你好啊"
        # print(pre)
        # text= "满足解的解解你还啊"

            # pre_pinyin, _ = wenzi2pinyin(pre)
            # text_pinyin,_=wenzi2pinyin(text)
            # pre=adjust_pre_len(pre_pinyin,text_pinyin,pre)
            # if len(pre_pinyin)!=len(text_pinyin):
            #     print("text:{}\npre:{}\nori:{}".format(text,pre,oripre))

