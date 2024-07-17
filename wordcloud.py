from wordcloud import WordCloud
import matplotlib.pyplot as plt
from PIL import Image
import numpy as np

text = '''python python python python python
big data big dat big data big data big data big data big data big data big data big data
crawling crawling crawling crawling
analysis analysis analysis analysis
visualization visualization visualization visualization
machine learning machine learning machine learning machine learning machine learning
deep learning deep learning deep learning deep learning deep learning deep learning
'''

wc = WordCloud(width=1000, height=600, background_color="white", random_state=0, font_path=r'c:\Windows\Fonts\malgun.ttf')
plt.imshow(wc.generate(text))
plt.axis("off")
plt.show()

def plot_cloud(wordcloud):
    # Set figure size
    plt.figure(figsize=(10, 10))
    # Display image
    plt.imshow(wordcloud) 
    plt.axis("off");

image_mask = np.array(Image.open('mask.jpg'))
image_colors = ImageColorGenerator(image_mask)

wordcloud = WordCloud(width = 1000, height = 1000,
    random_state=1, background_color='white', font_path=path, 
    colormap='Set2', collocations=False, mask=image_mask).generate_from_frequencies(word_num)
plot_cloud(wordcloud.recolor(color_func=image_colors))
plt.savefig('wordcloud.png')