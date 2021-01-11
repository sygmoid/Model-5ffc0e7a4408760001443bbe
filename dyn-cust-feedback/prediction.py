from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

def predict(comment):
  """
  input: text comment for which sentiment needs to be analyzed
  output: scores of pos,neg, neutral (percentages) and compound ([-1,1])
  
  The Compound score is a metric that calculates the sum of all the lexicon 
  ratings which have been normalized between -1(most extreme negative) and 
  +1 (most extreme positive)
  
  #ex: {'neg': 0.737, 'neu': 0.263, 'pos': 0.0, 'compound': -0.4215}
  """
  analyzer = SentimentIntensityAnalyzer()
  return analyzer.polarity_scores(comment)