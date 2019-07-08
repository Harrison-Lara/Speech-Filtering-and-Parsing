##################################################################################################################################################################
##
## CS 101
## Program # 5
## Name: Harrison Lara
## Email: hrlwwd@mail.umkc.edu
##
## PROBLEM: For this program you will be given the text of 4 different political speeches. You are also given the text of 4 “unknown” speeches;
##          your task is to report which of the known speeches the unknown texts most closely resemble.  You will use 2 different measures of similarity:
##          word commonality and word frequency. 
##
## ALGORITHM :
##  •   Import math and string
##  •   Set each speech variable to an empty string
##  •   Greet User
##  •	Create function for...
##      o   strip all punctuation
##      o   remove stop words, open file and use punctuation function
##      o   word count 
##      o   word commonality
##      o   Relative Frequency
##  •	Only look at single words, not whole pieces
##  •	Open files and use clean function to remove excess punct. and stop words 
##  •	Find the word commonality (only print the one with the highest match)
##      o   Count how often a word appears (100 times, 51 times, etc)
##      o   Use for loop to count +1 for common words
##      o   take length of speech + myster speech - common words
##      o   round off to four decimal places with formatting
##  •	Find he highest word frequency (only print the highest one)
##      o   Create empty dictionary
##      o   use for loop to with mystery then if statement with speech
##      o   append word from mystery to speech if present in both speeches
##      o   make sum = 0
##      o   variable1 = take speech of dict. word and divide by speech length
##      o   variable2 = take mystery of dict. word and divide by mystery length
##      o   use sum and add variable 1 and 2
##      o   take total = sum divide by length of distinct words
##      o   use square root
##      o   Use ‘root mean square’
##          	 Find all words that the 2 documents have in common (that is, words that appear in both). 
##          	 For each such word: Find the difference in relative frequency between the two documents 
##          	 Square that difference 
##          	 Keep a running total of the sum of the squares 
##          	 When the sum of the squares for all words is known: Divide the sum by the number of distinct words the documents have in common 
##          	 Find the square root of that quotient
##      o   open files for reading and apply functions to strip them of excess
##      o   apply each word common and frequency funtion to two speeches (do this for all 16 resuts)
##      o   see all results and print max and min for the common and freq, then print the ones that match best
##
## ERROR HANDLING:
##     None.
##
## OTHER COMMENTS:
##      None. 
##
#####################################################################################################################################################################

# imports
import math
import string

# set variables
romney = ''

# greet user
print('Greetings Speech Analyst')
print()

# functions
def exclude(speech):
    """strip all punctuation"""
    for c in string.punctuation:
        speech = speech.replace(c,'')
    return speech
    
def clean(filename, stop_words):
    """open speeches, clear punctuation and make lower case"""
    speech = exclude(open(filename, 'r').read())
    speech = speech.lower().split()
    speech = [x for x in speech if x not in stop_words]
    return speech
    
def word_count(speech):
    """Count the frequency of a word"""
    word_count_dict = {}

    for word in speech:
        if word in word_count_dict:
            word_count_dict[word] += 1
        else:
            word_count_dict[word] = 1

    return(word_count_dict)

def word_commonality(speech, mystery):
    '''Finds how often a word is used in the speech'''
    common_words = 0
    for word in mystery:
        if word in speech:
            common_words += 1
    
    total_distinct_words = (len(speech)+len(mystery) - common_words)
    wordCommonality = "{:.4f}%".format(float(common_words)/float(total_distinct_words)*100)
    return wordCommonality
   
def relative_frequency(speech, mystery):
    '''Finds how often a word appears in the speech'''
    distinct_words = []
    for word in mystery:
        if word in speech:
           distinct_words.append(word)
    running_sum = 0
    for word in distinct_words:
        rel_freq1 = float(speech[word])/float(len(speech))
        rel_freq2 = float (mystery[word])/float(len(mystery))
        running_sum += abs(rel_freq1 - rel_freq2)**2

    sum_quote = running_sum/float(len(distinct_words))
    relative_freq = math.sqrt(sum_quote)
    
    return '{:.4f}'.format(relative_freq)

##################################################

## main
stop_words = open('stopWords.txt', 'r').read().lower().split()
mystery1 = clean('mystery1.txt',stop_words)
mystery2 = clean('mystery2.txt',stop_words)
mystery3 = clean('mystery3.txt',stop_words)
mystery4 = clean('mystery4.txt',stop_words)
romney = clean('romney.txt',stop_words)
clinton = clean('clinton.txt', stop_words)
obama = clean('obama.txt', stop_words)
trump = clean('trump.txt', stop_words)
mystery1_freq_dict = word_count(mystery1)
mystery2_freq_dict = word_count(mystery2)
mystery3_freq_dict = word_count(mystery3)
mystery4_freq_dict = word_count(mystery4)
romney_freq_dict = word_count(romney)
clinton_freq_dict = word_count(clinton)
obama_freq_dict = word_count(obama)
trump_freq_dict = word_count(trump)

# output
wordCommonality = word_commonality(romney_freq_dict, mystery1_freq_dict)
relative_freq = relative_frequency(trump_freq_dict, mystery1_freq_dict)
print('The text mystery1 has the highest word commonality with Romney ',wordCommonality)
print('The text mystery1 has the highest frequency similarity with Trump ',relative_freq)
print()
print()
            
wordCommonality = word_commonality(romney_freq_dict, mystery2_freq_dict)
relative_freq = relative_frequency(obama_freq_dict, mystery2_freq_dict)
print('The text mystery2 has the highest word commonality with Romney', wordCommonality)
print('The text mystery2 has the highest frequency similarity with Obama ',relative_freq)
print()
print()
          
      
wordCommonality = word_commonality(romney_freq_dict, mystery3_freq_dict)
relative_freq = relative_frequency(obama_freq_dict, mystery3_freq_dict)
print('The text mystery3 has the highest word commonality with Romney ',wordCommonality)
print('The text mystery3 has the highest frequency similarity with Obama ',relative_freq)
print()
print()
      

wordCommonality = word_commonality(obama_freq_dict, mystery4_freq_dict)
relative_freq = relative_frequency(clinton_freq_dict, mystery4_freq_dict)
print('The text mystery4 has the highest word commonality with Obama ' ,wordCommonality)
print('The text mystery4 has the highest frequency similarity with Clinton ',relative_freq)

