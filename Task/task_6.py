import pandas as pd
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt
from wordcloud import STOPWORDS
import webscraper

def run() :
    dataset = pd.read_csv('spotify_data.csv')                   # importing dataset.
    top_songs = dataset.nlargest(5, 'pop')                      # dataframe from the 5 highest value of pop.
    top_songs_title = top_songs.iloc[:,0].tolist()              # selects the titles and artists and makes two lists.
    top_songs_artists = top_songs.iloc[:,1].tolist()
    new_dict = dict(zip(top_songs_title, top_songs_artists))    # creates a dict from the two lists.
    print(new_dict)
    top_songs

    driver = webscraper.init_webdriver()                        # driver setup (OBS! This is called from another module inorder to initialize our webdriver).
    driver.get('https://www.azlyrics.com/')                     # URL to get songs from.
    driver.implicitly_wait(1)

    song_texts = []
    for key, value in new_dict.items():
        elem = driver.find_element_by_xpath('//*[@id="q"]')     # selects the search form.
        elem.click()                                            # selects form.
        elem.send_keys(key, ' ', value)                         # types in the dict values in the form.
        elem.submit()                                           # submits form.

        driver.find_element_by_xpath('/html/body/div[2]/div/div/div[1]/table/tbody/tr[1]/td/a').click()     # clicks the top song.
        txt = driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div[5]').text                      # selects the text.
        
        txt.replace('\n', '')                                   # replaces '\n' with '' so we get a cleaner text.
                      
        print('\n' + key, value)                                # prints song title and artist name.
        print(txt)                                              # prints the song text.
        song_texts.append(txt)                                  # adds the txt to song_text array.

    upper_stopwords = [x.upper() for x in STOPWORDS]            # takes the stopwords set and,
    lower_stopwords = [x.lower() for x in STOPWORDS]            # converts it to both upper and lower.
    combined_stopwords = upper_stopwords + lower_stopwords      # combines the upper and lower stopwords

    for x in song_texts:                                        # for each song text generate a wordcloud

        wordcloud = WordCloud(collocations=False, stopwords=combined_stopwords).generate(x)                 # collocations prevent duplicates (stopwords = combined_stopwords)

        plt.imshow(wordcloud, interpolation='bilinear')         # interpolation makes the image appear smoother
        plt.axis("off")                                         # axis makes the words both horizontal and vertical
        plt.show()                                              # prints the generated image
        print(wordcloud.words_.keys())