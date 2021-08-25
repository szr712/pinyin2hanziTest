import os
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
        

if __name__=="__main__":
    test_result_len_equal("./preFile","./textFile")

