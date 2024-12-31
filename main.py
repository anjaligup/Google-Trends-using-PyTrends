import pandas as pd
# pytrends is an unofficial Google trend API
from pytrends.request import TrendReq
import matplotlib.pyplot as plt
import time

# connect to Google
Trending_topics = TrendReq(hl='en-US', tz=360)

# create a dataframe of the top 10 countries that use search the term "Computer Science"
kw = ["Computer Science"]

#build payload --> data you send to an API (application programming interface) 
Trending_topics.build_payload(kw, cat = 0, timeframe='today 12-m')
time.sleep(5)

# returns indexed data for when the specific phrase was most searched according to payload 
data = Trending_topics.interest_over_time()
data = data.sort_values(by="Computer Science", ascending=False)
print(data.head(10))

# return data by region ascending 
data2 = Trending_topics.interest_by_region()
data2 = data2.sort_values(by="Computer Science", ascending=False)
data2 = data2.head(10)
print(data2)

# get the top trending searches in the year 2023
topData = Trending_topics.top_charts(2023, hl='en-US', tz = 300, geo = 'GLOBAL')
topData = topData.head(10)
print(topData)

#
keywords = Trending_topics.suggestions(
  keyword='Computer Science')
df = pd.DataFrame(keywords)
filtered_df = df[['title', 'type']]
print(filtered_df)


#visualize data using bar graph using matplotlib 
data2.reset_index().plot(x = 'geoName', y ='Computer Science', figsize=(10,5), kind="bar")
plt.style.use('fivethirtyeight')  # use fivethirtyeight style (default/basic)
plt.show()


