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
    corrector=0
    for preFile in os.listdir(preFileDir):
        print(preFile)
        with open(os.path.join(preFileDir, preFile), "r", encoding="utf-8")as fw:
            preContents = fw.readlines()
        with open(os.path.join(textFileDir, preFile[:-7]+"_text.txt"), "r", encoding="utf-8")as fw:
            textContents = fw.readlines()
        for pre,text in zip(preContents,textContents):
            total+=1
            if len(pre)!=len(text):
                pre_pinyin, _ = wenzi2pinyin(pre)
                text_pinyin,_=wenzi2pinyin(text)
                pre=pre.replace("\n", "")
                text=text.replace("\n","")
                oripre=pre
                pre=adjust_pre_len(pre_pinyin,text_pinyin,pre)
                notEqual+=1
                if len(pre)==len(text):
                    corrector+=1
                #print("pre:{}text:{}".format(pre,text))
                print("pre:{}\ntext:{}\noripre:{}".format(pre,text,oripre))
        print("total:{} notEqual:{}corrector:{}".format(total,notEqual,corrector))
        #print("total:{} notEqual:{}".format(total,notEqual))

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
    # pre = "在我国风蚀荒漠化多见于西北地区水时荒漠化多分布于南方低山丘陵和西南卡死特地去盐渍化主要分布在西北干旱灌溉渠和华北办事run驱动图荒漠化发生的青藏高原地区"
    # print(pre)
    # oripre=pre
    # text= "在我国风蚀荒漠化多见于西北地区水蚀荒漠化多分布于南方低山丘陵和西南喀斯特地区盐渍化主要分布在西北干旱灌溉区和华北半湿润区冻土荒漠化发生的青藏高原地区"

    # pre_pinyin, _ = wenzi2pinyin(pre)
    # text_pinyin,_=wenzi2pinyin(text)
    # print(pre_pinyin,text_pinyin)
    # # if len(pre_pinyin)!=len(text_pinyin):
    # pre=adjust_pre_len(pre_pinyin,text_pinyin,pre)
    # print("text:{}\npre:{}\nori:{}".format(text,pre,oripre))

