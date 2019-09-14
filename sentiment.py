import tweepy
from textblob import TextBlob
import pandas as pd

Access_token="1088749854774517760-cRbYAgEMeUeuwhVR6s8oHaXrKBRh32"
Access_token_secret="llBKfHQqgKEM1WqAadrLjYuuNFJIS3sgDElwiHTRXLRs3"
Consumer_key="EazL5W6t9GOMpZj243UEEKyvI"
Consumer_secret_key="SSP33bWsIyQTRA17Lnb36oBL8YoWbZbJfYjGWmtQxTpP4XqtxO"

auth=tweepy.OAuthHandler(Consumer_key,Consumer_secret_key)
auth.set_access_token(Access_token,Access_token_secret)
api=tweepy.API(auth,wait_on_rate_limit=True)

search_list=['Boeing CO','General Electric Company','Honeywell International','Jardine Matheson Holdings','Jardine Strategic Holdings','Worldpay INC','Experian PLC','CRH PLC','Rolls-Royce Holdings PLC','Bae Systems PLC']
for n in search_list:
    positive_tweet = []
    negative_tweet = []
    neutral_tweet = []
    Final_list = []
    new_list = []
    tweets=tweepy.Cursor(api.search,q=str(n)+'-filter:retweets',lang='en',since='2018-01-01').items(30000)
    for tweet in tweets:
        print(tweet.text)
        analysis=TextBlob(tweet.text)
        if (analysis.sentiment.polarity)>0:
            positive_tweet.append(analysis.sentiment.polarity)
        elif analysis.sentiment.polarity<0:
            negative_tweet.append(analysis.sentiment.polarity)
        elif analysis.sentiment.polarity==0:
            neutral_tweet.append(analysis.sentiment.polarity)
        else:
            print('Emotionless & No Opinion regarding tweet')
    #print(positive_tweet)
    total = len(positive_tweet) + len(negative_tweet) + len(neutral_tweet)
    percentage_of_postive_review = float(len(positive_tweet) / (total) * 100)
    #print('Positive Review is ' + str(percentage_of_postive_review) + '%')
    Review = float(percentage_of_postive_review / 10)
    #print('Review is' + str(Review))
    new_list.append(n)
    new_list.append(Review)
    #print(new_list)
    if new_list!=[]:
        label=['Company Name','Review']
        i=0
        j=2
        while i < j and j <= len(new_list):
            Final_list.append(new_list[i:j])
            i = i + 2
            j = j + 2
        df = pd.DataFrame.from_records(Final_list, columns=label)
        #print(df)
        df.to_csv('D:/Review_Rating/Company Review'+str(n)+'.csv', index=False)

a=pd.read_csv('D:/Review_Rating/Company ReviewBoeing CO.csv')
b=pd.read_csv('D:/Review_Rating/Company ReviewGeneral Electric Company.csv')
c=pd.read_csv('D:/Review_Rating/Company ReviewHoneywell International.csv')
d=pd.read_csv('D:/Review_Rating/Company ReviewJardine Matheson Holdings.csv')
e=pd.read_csv('D:/Review_Rating/Company ReviewJardine Strategic Holdings.csv')
f=pd.read_csv('D:/Review_Rating/Company ReviewWorldpay INC.csv')
g=pd.read_csv('D:/Review_Rating/Company ReviewExperian PLC.csv')
h=pd.read_csv('D:/Review_Rating/Company ReviewCRH PLC.csv')
i=pd.read_csv('D:/Review_Rating/Company ReviewRolls-Royce Holdings PLC.csv')
j=pd.read_csv('D:/Review_Rating/Company ReviewBae Systems PLC.csv')

df1=pd.concat([a,b,c,d,e,f,g,h,i,j])
print(df1)
df1.to_csv('D:/Review_Rating/Merged_file.csv',index=False)