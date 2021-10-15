
>>>>>>>>>>>>>>>>Quick summary:
This is a simple program that aims to retrieve most of the cryptocurrency mentions of the last hour (as from the beginning of the execution of the program) from old.reddit/Cryptocurrency subreddit, count them, and display the 10 most mentionned as a list and a word cloud. The results are displayed using the streamlit python package.





>>>>>>>>>>>>>>>>Requirements:
Python3 (tested with Python 3.9.7)

>>>>Packages:
Requests
BeautifulSoup4
Streamlit
Datetime 
Matplotlib
Wordcloud



>>>>>>>>>>>>>>>>Run the code using:
streamlit run scrapping_reddit.py




>>>>>>>>>>>>>>>>Detail:

1) Constitute the list of cryptocurrency names:

A list of ~ 1000 cryptocurrency prices has been imported from https://coinmarketcap.com/ into an xls file. Then, using pandas I extracted names and abbreviations of each coin into a txt file. Names that contain spaces has been ignored. Names and abbreviations that could be mistaken for most common words (e.g "like", "super", "quick") has been arbitrarily weeded out by hand.

The list_cc_names.dat contains a single column of names and then abbreviation of cryptocoins. The main program imports the file as a dictionary, where the keys are the names from this file, and values are counts of mention of a given string on reddit, set initially to zero.   



2) Search the mentions from /Cryptocurrency subreddit:
The program looks at all posts in the last 5 hours and get all of the text from posts and comments posted in the last hour. Each word of the text is then compared to the dictionary of crypto coin names. If the word correspond to a name of a crypto coin, the corresponding value in the dictionnary is incremented.
We then use streamlit and wordcloud packages to display the results. Streamlit generates a webpage where a list of ten most popular mentions is displayed, and includes a word cloud image.

