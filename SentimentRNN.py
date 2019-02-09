#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import numpy as np

# read data from text files
with open('data/reviews.txt', 'r') as f:
    reviews = f.read()
with open('data/labels.txt', 'r') as f:
    labels = f.read()


# In[ ]:


print(reviews[:2000])
print()
print(labels[:20])


# In[ ]:


from string import punctuation

print(punctuation)

# get rid of punctuation
reviews = reviews.lower() # lowercase, standardize
all_text = ''.join([c for c in reviews if c not in punctuation])


# In[ ]:


# split by new lines and spaces
reviews_split = all_text.split('\n')
all_text = ' '.join(reviews_split)

# create a list of words
words = all_text.split()


# In[ ]:


words[:30]


# In[ ]:


# feel free to use this import 
from collections import Counter

## Build a dictionary that maps words to integers
vocab_to_int = None

## use the dict to tokenize each review in reviews_split
## store the tokenized reviews in reviews_ints
reviews_ints = []


# In[ ]:


# stats about vocabulary
print('Unique words: ', len((vocab_to_int)))  # should ~ 74000+
print()

# print tokens in first review
print('Tokenized review: \n', reviews_ints[:1])


# In[ ]:


# 1=positive, 0=negative label conversion
encoded_labels = None


# In[ ]:


# outlier review stats
review_lens = Counter([len(x) for x in reviews_ints])
print("Zero-length reviews: {}".format(review_lens[0]))
print("Maximum review length: {}".format(max(review_lens)))


# In[ ]:


print('Number of reviews before removing outliers: ', len(reviews_ints))

## remove any reviews/labels with zero length from the reviews_ints list.

reviews_ints = 
encoded_labels = 

print('Number of reviews after removing outliers: ', len(reviews_ints))


# In[ ]:


def pad_features(reviews_ints, seq_length):
    ''' Return features of review_ints, where each review is padded with 0's 
        or truncated to the input seq_length.
    '''
    ## implement function
    
    features=None
    
    return features


# In[ ]:


# Test your implementation!

seq_length = 200

features = pad_features(reviews_ints, seq_length=seq_length)

## test statements - do not change - ##
assert len(features)==len(reviews_ints), "Your features should have as many rows as reviews."
assert len(features[0])==seq_length, "Each feature row should contain seq_length values."

# print first 10 values of the first 30 batches 
print(features[:30,:10])


# In[ ]:


split_frac = 0.8

## split data into training, validation, and test data (features and labels, x and y)


## print out the shapes of your resultant feature data


# In[ ]:




