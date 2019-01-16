#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan  8 13:35:42 2019

@author: benjaminwasserman
"""

import glob
import random

path = "/Users/benjaminwasserman/Desktop/Chapman University/Junior/Machine Learning/markov_models/"

words = []
word_list = []

# open all files and read in contents
for files in glob.glob(path + "*.txt"):
    infile = open(files, 'rb')
    a = infile.readlines()
    for i in a:
        new_line = i.decode("utf-8", "ignore")
        word_list += new_line.split()

# list of words without some punctuation
all_words = []

#strip list of words of punctuation
for word in word_list:
    no_question = word.replace("?", "")
    no_exclamation = no_question.replace("!", "")
    all_words.append(no_question)
    
# unique words in all scripts    
unique = set(word_list)
unique_count = len(unique)
unique_onedim = list(unique)


num_words= 2000
count = 0


dictionary = {}
starting_words = []        
starting_possibilities = 0

# create list of possible first words
for j in range(len(word_list)):
    if word_list[j-1][-1] is "." or word_list[j-1][-1] is "?" or word_list[j-1][-1] is "!":
        starting_possibilities += 1
        if word_list[j-2] is not "." and word_list[j] is not "-":
            starting_words.append(word_list[j])
        
  
# create dictionary that has a reference from every word to a list of next words      
for i in range(len(all_words)):
    key = all_words[i - 1]
    if key in dictionary:
        dictionary[key].append(all_words[i])
    else:
        dictionary[key] = [all_words[i]]
    
  
# Generate a starting word
curr_word = random.choice(starting_words)


# Final string to generate
final_string = ""
prev_word = "sample_word"


# use each word to find the next
while (True):
    next_words = dictionary[curr_word]
    chosen_word = random.choice(next_words)
    if (chosen_word[0].isupper() and chosen_word[-1].isupper() and len(chosen_word) > 2):
       if (prev_word[0].islower() or prev_word[-1].islower() or len(prev_word) < 2): 
        curr_word = "\n\n" + chosen_word + "\n\n"
    else:
        curr_word = chosen_word
    final_string += " " + curr_word
    curr_word = chosen_word
    prev_word = curr_word
    count += 1
    if (count > num_words and (curr_word[-1] is "." or curr_word[-1] is "?" or curr_word[-1] is "!")):
        break
        

# write to a file
file = open("script.txt", "w")
file.write(final_string) 
file.close()  

    

    
    








        
        



