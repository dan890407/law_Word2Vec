from tqdm import tqdm, trange
big_dict=dict()
name_type=["n","v","r"]
#big_dict={"word":[class,class,class]}
from dataclasses import dataclass
@dataclass
class wordname:
    name:str
    count:int
from udicOpenData.stopwords import *
with open("law_data/big_law_data_2.txt","r",encoding='utf-8') as f:
    lines=f.readlines()
    progress=tqdm(total=len(lines))
    for line in lines:
        tokens=[(name,types)  for name, types in list(rmsw(line,flag=True)) for i in name_type if  types in i and len(name)>1  ]
        token_set=list(set(tokens))
        for names,types in token_set:
            if names not in big_dict.keys():
                big_dict.update({names:{}})
            for names2,types2 in [(id ,tp) for id ,tp in  tokens if id!=names]:
                if names2 not in big_dict[names]:   # check names2 in names1 's list
                    big_dict[names].update({names2:int(1)})
                else:
                    big_dict[names][names2]+=1
        progress.update(1)
import json
with open('kcm_dict.json', 'w', encoding='utf-8') as f:
    json.dump(big_dict, f, ensure_ascii=False)
