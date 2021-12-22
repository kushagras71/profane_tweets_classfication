#Importing the required libraries
import json


#opening and reading the slurs words file and the sample tweets json file.
with open("racial_slurs.txt",'r') as slur_words, open('smaple_tweets.json','r') as sample_tweets:
    words = slur_words.read().splitlines()
    tweets = json.load(sample_tweets)


#empty list for stroing the tweets with racial slurs
profane_tweets = []


#finding racial slurs in the sample tweets
for j in tweets['sampleTweets']:
    profane_count = (sum(j.lower().count(i) for i in words))
    profane_tweets.append([j, profane_count])


#Cacluting the degree of profanity
# degree pf profanity = no. of racial slurs found in the tweet /s word count of the tweet
for i in profane_tweets:
    score = (i[1]/len(i[0]))
    if score == 0.0:
        degree_of_profanity = "Not Profane"
    elif score > 0.0  and score < 0.019:
        degree_of_profanity = 'Slightly Profane'
    elif score > 0.019 and score < 0.045:
        degree_of_profanity = 'Highly Profane'
    else:
        degree_of_profanity = 'Exteremely Profane'
    print("Tweet:",i[0],": \n Score of profanity: ",score,"\n","Degree of Profanity: ",degree_of_profanity)
    print("\n\n")
