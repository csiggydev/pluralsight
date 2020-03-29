#!/usr/bin/venv python3

# Modules

# functions tutorial using code from the previous lesson

#import the urlopen method from the urllib library

import urllib

def fetch_words():
    
        story = urlopen('http://sixty-north.com/c/t.txt')
        story_words = []
        for line in story:
            line_words = line.decode('utf8').split()
            for word in line_words:
                story_words.append(word)
        story.close()

        for word in story_words:
            print(word)


