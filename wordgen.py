import random
from bs4 import BeautifulSoup as bs
import requests
# import pandas as pd

def get_test_wordlist():
    url = 'https://en.wikipedia.org/wiki/List_of_ancient_Egyptians'
    src = requests.get(url).content
    soup = bs(src, 'lxml')
    tables = soup.find_all('table', attrs = {'class' : 'wikitable'})
    
    full_namelist = []
    for t in tables:
        rows = t.find_all('tr')
        for r in rows:
            d_ls =[d.text for d in r.find_all('td')]
            if len(d_ls) > 0:
                full_namelist.append((d_ls[0]).split(' ')[0])
    
    for name in full_namelist:
        if '(' in name:
            del name
    return list(set(full_namelist))


def select_weighted(d):
   offset = random.randint(0, sum(d.values())-1)
   for k, v in d.items():
      if offset < v:
         return k
      offset -= v


def add_subchunk(freq_dict, subchunk):   
    if subchunk in freq_dict.keys():
        freq_dict[subchunk] += 1
    else:
        freq_dict[subchunk] = 1    


def train(wordlist, depth):
    assert depth > 0
    dict_start = {}    
    dict_general = {}
    dict_end = {}
    for word in wordlist:
        #print(word)
        # Count for dict_start, [0:3] avoids consonant jumbles at start
        add_subchunk(dict_start, word[0:3])
        # Count for dict_end
        add_subchunk(dict_end, word[-2:]) 
        # Count for dict_general
        for i in range(1, len(word)):
            subchunk = word[i-1:i+depth]
            add_subchunk(dict_general, subchunk)
    # print(dict_general)
    return (dict_start, dict_general, dict_end)
            

class Builder():
    def __init__(self):
        pass
        
    def build(self, model, wordlen):
        endlen = 2
        # Get a starting block from the starting frequency table
        word = select_weighted(model[0])
        # Continuously add letters based on our general frequency table
        while len(word) < wordlen-endlen:
            try:
                # Filter to chunks with overlap
                newDict = {k: v for k, v in model[1].items() if k[0] == word[-1]}
                # Add chunk (minus overlapping letter)
                chunk = select_weighted(newDict)[1:]
                word += chunk
                
            except:
                word = select_weighted(model[0])
        # Add an ending chunk, lots of fuckey edge cases here. Room for improvement
        finished = False
        while not finished:
            try:
                newDict = {k: v for k, v in model[2].items() if k[0] == word[-1]}
                word += select_weighted(newDict)[1:]
                finished = True
            except:
                try:
                    # Filter to chunks with overlap
                    newDict = {k: v for k, v in model[1].items() if k[0] == word[-1]}
                    # Add chunk (minus overlapping letter)
                    word += select_weighted(newDict)[1:]
                    
                    # Non-alpha character management
                    if not word[-2].isalpha():
                        finished = False
                        continue
                    else:
                        break
                    
                    break
                # Non-alpha character management
                except:
                    if not word[-2].isalpha():
                        finished = False
                        continue
                    else:
                        break
                
            if not word[-2].isalpha():
                finished = False

        
        # Trim hanging "'" and "-" characters
        if not word[-1].isalpha():
            word = word[:-1]
        
        
        # Triplicate letter removal
        for i in range(0, len(word)):
            # Try/except for index out of range
            try:
                if word[i] == word[i+1] == word[i+2]:
                    #print(f'TRIPLICATE LETTER: {word[i]}')
                    word = word[:i] + word[i+1:]
            except:
                break
        return word



if __name__ == '__main__':
    print('Scraping word list')
    
    with open('lkos_demon_names.txt', 'r') as f:
        wordlist = f.readlines()
        wordlist = [word[:-1] for word in wordlist]
    
    print('Training model')
    model = train(wordlist, 3)
    #print(model[1])
    
    builder = Builder()
    print('Training model')
    print()

    for i in range(0, 50):
        print(builder.build(model, random.randint(5, 8)))