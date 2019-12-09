import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS


font_path = 'c:\\windows\\fonts\\NANUMSQUAREB.ttf'
wordcloud = WordCloud(
    background_color='#ffffff',
    font_path = font_path,
    width = 1000,
    height = 500,
    colormap="nipy_spectral"
)

text=open('output.txt').read()
wordcloud = wordcloud.generate(text)

fig = plt.figure(figsize=(10,5))
plt.imshow(wordcloud, interpolation="bilinear", aspect="auto")
plt.axis("off")
plt.show()
fig.savefig('C:/Users/LG/Desktop/CloudCom/page/projectPage/img/wordcloud.png',dpi=800)

