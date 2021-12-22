## Profane Tweet Detection
### Assigning a degree of profanity to Twitter tweets.
<hr>
<b>Introduction</b><br>
Racial Slurs and profane tweets are becoming a serious problem these days on Twitter. The poeple doing these social media activities usually uses some sentences and words that trigger other poeple belong different communities those leading differences and eveuntally fights. During the COVID 19 pandemic this increased by many folds. In this repository, I have a uploaded a simple Python program which can be used to classify or assign a degree of profanity to the tweets on Twitter which can be used to regularize and filter the tweets that go out in the public.
<hr>
<b>Logic of the prorgam</b><br>
The program works by assigning a score and corresponding degree of profanity to a tweet depending on the number of profane words (racial slurs) the tweet has. The score is calculated by dividing the number of profane words in the tweet by the total number of words in the tweet. Higher the score higher is the degree of profanity of the tweet. The program reads two files one is the JSON containing the tweets and the other is Text File which consists of racial slurs. Following the range of scores and corresponding degree of profanity.

|    Score     |Degree of Profanity|
|--------------|-------------------|
|  0.0           | Not Proframe              |
| 0.0 - 0.019    | Sligthy Profane           |
| 0.019 - 0.045 | Highly Profane    |
| 0.045 & above | Extremely Profane |
<br>
