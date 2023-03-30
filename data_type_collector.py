import os
import json
from udicOpenData.stopwords import *
import logging
import re
logger = logging.getLogger(__name__)
logging.basicConfig(
    format="%(asctime)s - %(levelname)s - %(name)s - %(message)s",
    datefmt="%m/%d/%Y %H:%M:%S",
    level=logging.INFO,
)
path = "output/"
key_word=['judgement','opinion']
index=0
big_dict=[]
with open("data.json","w+",encoding='utf-8') as big_f:
    for root, dirs, files in os.walk(path, topdown=False):
        for jk,name in enumerate(files):
            file_path=os.path.join(root, name)
            with open(file_path,"r",encoding="utf-8") as r:
                doc=json.load(r)
                small_list=[]
                for key,value in doc.items():
                    try:
                        if type(value)==str and key in key_word:
                            strings=value.strip().replace("\n","")
                            string_line=re.split("，|。",strings)
                            for each_line in string_line:
                                small_list.append(list(rmsw(each_line,flag=True)))
                    except Exception as e:
                        print(e)
                big_dict.append({"id":index,"tokens":small_list})
                index+=1
                logger.info(f"processed{jk}/{len(files)} {name} ")
    json.dump(big_dict, big_f, ensure_ascii=False,indent=2)

