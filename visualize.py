from PIL import Image
from wordcloud import ImageColorGenerator
import matplotlib.pyplot as plt
import numpy as np

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