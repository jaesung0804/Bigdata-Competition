import pandas as pd
import requests
from time import sleep
from bs4 import BeautifulSoup as bs
from tqdm import tqdm

unique_word = set()
def crawling_related_word(queue, n):
    global unique_word
    if len(queue)==0 or n==0:
        print('크롤링 종료')
        return
    df = pd.DataFrame()
    next_queue = []
    print(queue)

    for word in queue:
        temp_df = pd.DataFrame()
        temp_list = []
        url = 'https://search.daum.net/search?nil_suggest=btn&w=tot&DA=SBC&q=' + word

        while True:
            try:
                response = requests.get(url)
                break
            except:
                print("sleeping...")
                sleep(5)

        if response.status_code == 200:
            html = response.text
            document = bs(html, 'html.parser')
            try:
                div_inner = document.find('div',class='list_keyword type2')
                related_word_list = div_inner.findall('span', class='wsn')
            except:
                if pd.isna(div_inner):
                    try:
                        divinner = document.find('div', class='list_keyword')
                        related_word_list = div_inner.findall('span',class='wsn')
                    except:
                        print(word,'연관 검색어가 없습니다.')
                        related_word_list = []

        if len(related_word_list) == 0: continue

        for idx, related_word in enumerate(related_word_list):
            next_word = related_word_list[idx].text
            temp_list.append(next_word)
            if not next_word in unique_word:
                next_queue.append(next_word)
                unique_word.add(next_word)
            # print(related_word_list[idx].text)

        temp_df['sub_word'] = temp_list
        temp_df['sup_word'] = word
        df = pd.concat([df,temp_df],axis=0)
    df = pd.concat([df, crawling_related_word(next_queue, n-1)], axis=0)
    return df.reset_index(drop=True)

word_list = ['코로나 확진자', '코로나19']
df_crawl = crawling_related_word(word_list,3)

## 데이터프레임 저장 for 형태소 분석
df_crawl.to_csv("data_from_daum1.csv", index=False)
## DTM 파일 읽어오기
dtm = pd.read_csv("DTM1.csv")
dtm
## text network: 단어쌍 만들기
from tqdm import tqdm

dataset = dtm.copy()
column_list = dataset.columns
word_length = len(column_list)

count_dict = {}

for doc_number in tqdm(range(len(dataset)), desc='단어쌍 만들기 진행중'):
  tmp = dataset.loc[doc_number] # 현재 문서의 단어 출현 빈도 데이터를 가져온다. 
  for i, word1 in enumerate(column_list): 
    if tmp[word1]: # 현재 문서에 첫번째 단어가 존재할 경우 
      for j in range(i + 1, word_length): 
        if tmp[column_list[j]]: # 현재 문서에 두번째 단어가 존재할 경우 
          count_dict[column_list[i], column_list[j]] = count_dict.get((column_list[i], column_list[j]), 0) + max(tmp[word1], tmp[column_list[j]])

# count_list에 word1, word2, frequency 형태로 저장할 것이다.
count_list = []

for words in count_dict:
    count_list.append([words[0], words[1], count_dict[words]])

# 단어쌍 동시 출현 빈도를 DataFrame 형식으로 만든다.
df = pd.DataFrame(count_list, columns=["word1", "word2", "freq"])
df = df.sort_values(by=['freq'], ascending=False)
df = df.reset_index(drop=True)

# 이 작업이 오래 걸리기 때문에 csv파일로 저장 후 사용하는 것을 추천한다.
df.to_csv('networkx.csv', encoding='utf-8-sig')