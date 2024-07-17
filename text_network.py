## text network: 그리기
import networkx as nx
import operator
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

dtm = pd.read_csv("DTM1.csv")
df = pd.read_csv("my_csv.csv")
dataset = df.copy()

font_name = "원하는 폰트 넣기"

G_centrality = nx.Graph()

for ind in range(len(np.where(dataset['freq'] >= 100)[0])):
  G_centrality.add_edge(dataset['word1'][ind], dataset['word2'][ind], weight=int(dataset['freq'][ind]))
  
dgr = nx.degree_centrality(G_centrality)
btw = nx.betweenness_centrality(G_centrality)
cls = nx.closeness_centrality(G_centrality)
egv = nx.eigenvector_centrality(G_centrality)
pgr = nx.pagerank(G_centrality)

sorted_dgr = sorted(dgr.items(), key=operator.itemgetter(1), reverse=True) 
sorted_btw = sorted(btw.items(), key=operator.itemgetter(1), reverse=True) 
sorted_cls = sorted(cls.items(), key=operator.itemgetter(1), reverse=True) 
sorted_egv = sorted(egv.items(), key=operator.itemgetter(1), reverse=True) 
sorted_pgr = sorted(pgr.items(), key=operator.itemgetter(1), reverse=True)

G = nx.Graph()

for i in range(len(sorted_pgr)): 
  G.add_node(sorted_pgr[i][0], nodesize=sorted_dgr[i][1])

for ind in range(len(np.where(dataset['freq'] >= 100)[0])):
  G.add_weighted_edges_from([(dataset['word1'][ind], dataset['word2'][ind], int(dataset['freq'][ind]))])

sizes = [G.nodes[node]['nodesize'] * 10000+500 for node in G]

pos = nx.spring_layout(G, k=4, iterations=100)
options = { 'edge_color': '#F07249', 'width': 1, 'with_labels': True, 'font_weight': 'regular', 'node_color':"#D22C2C", 'font_color':"#000000"}

plt.figure(figsize=(12, 12))

nx.draw(G, node_size=sizes, pos=pos, **options, font_family=font_name) # font_family로 폰트 등록 

# labels = nx.get_edge_attributes(G, 'weight')
# nx.draw_networkx_edge_labels(G, pos=pos, edge_labels=labels )
 
ax = plt.gca()
ax.collections[0].set_edgecolor("#555555")
plt.savefig("Graph.png", format="PNG")
plt.show()

# 단어 별 개수 구하기
word_num = dtm.apply(lambda col: sum(col), axis=0)
word_str = ''
for key, value in word_num.items():
    word_str += (key+' ')*value
from wordcloud import WordCloud

wc = WordCloud(width=1000, height=600, background_color="white", random_state=0, font_path=path)
# fontprop = fm.FontProperties(fname=path, size=18).get_name()
plt.imshow(wc.generate_from_frequencies(word_num))
plt.axis("off")
plt.show()