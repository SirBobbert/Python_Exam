import pandas as pd
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt
from wordcloud import STOPWORDS
from shutil import which
from selenium import webdriver
    
def init_webdriver():
    FIREFOXPATH = which("firefox")
    CHROMEPATH = which("chrome") or which("chromium")
    """Simple Function to initialize and configure Webdriver"""
    if FIREFOXPATH != None:
        print(FIREFOXPATH)#cm
        from selenium.webdriver.firefox.options import Options

        options = Options()
        options.binary = FIREFOXPATH
        options.add_argument("-headless")
        return webdriver.Firefox(firefox_options=options, log_path="geckodriver.log")

    elif CHROMEPATH != None:
        print(CHROMEPATH)#cm
        from selenium.webdriver.chrome.options import Options

        options = Options()
        options.binary_location = CHROMEPATH
        options.add_argument("--headless")
        return webdriver.Chrome(chrome_options=options, service_args=['--verbose'], service_log_path="chromedriver.log")

def run() :
    # importing dataset
    dataset = pd.read_csv('spotify_data.csv')

    # dataframe from the 5 highest value of pop
    top_songs = dataset.nlargest(5, 'pop')

    # selects the titles and artists and makes two lists
    top_songs_title = top_songs.iloc[:,0].tolist()
    top_songs_artists = top_songs.iloc[:,1].tolist()

    # creates a dict from the two lists
    new_dict = dict(zip(top_songs_title, top_songs_artists))

    print(new_dict)
    top_songs


    # url
    url = 'https://www.azlyrics.com/'

    # driver setup
    driver = init_webdriver()
    driver.get(url)

    # wait for and accept cookies
    driver.implicitly_wait(5)
    #driver.find_element_by_xpath('//*[@id="onetrust-accept-btn-handler"]').click()

    song_texts = []

    for key, value in new_dict.items():

        # selects the search form
        elem = driver.find_element_by_xpath('//*[@id="q"]')

        # selects form
        elem.click()

        # types in the dict values in the form
        elem.send_keys(key, ' ', value)

        # submits form
        elem.submit()

        # clicks the top song
        driver.find_element_by_xpath('/html/body/div[2]/div/div/div[1]/table/tbody/tr[1]/td/a').click()

        # selects the text
        txt = driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div[5]').text

        # replaces '\n' with '' so we get a cleaner text
        txt.replace('\n', '')

        # prints song title and artist name
        print('-------------------------------------------------------------')
        print(key, value)
        print()
        # prints the song text
        print(txt)

        # adds the txt to song_text array
        song_texts.append(txt)
    # takes the stopwords set and converts it to both upper and lower
    upper_stopwords = [x.upper() for x in STOPWORDS]
    lower_stopwords = [x.lower() for x in STOPWORDS]

    # combines the upper and lower stopwords
    combined_stopwords = upper_stopwords + lower_stopwords

    # create and generate a word cloud image

    # for each song text generate a wordcloud
    for x in song_texts:

        #collocations prevent duplicates
        #stopwords = combined_stopwords
        wordcloud = WordCloud(collocations=False, stopwords=combined_stopwords).generate(x)

        # interpolation makes the image appear smoother
        plt.imshow(wordcloud, interpolation='bilinear')

        # axis makes the words both horizontal and vertical
        plt.axis("off")

        # prints the generated image
        plt.show()
        print(wordcloud.words_.keys())