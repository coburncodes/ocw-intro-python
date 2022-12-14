# 6.0001/6.00 Problem Set 5 - RSS Feed Filter
# Name:
# Collaborators:
# Time:

import feedparser
import string
import time
import threading
from project_util import translate_html
from mtTkinter import *
from datetime import datetime
import pytz
import re


#-----------------------------------------------------------------------

#======================
# Code for retrieving and parsing
# Google and Yahoo News feeds
# Do not change this code
#======================

def process(url):
    """
    Fetches news items from the rss url and parses them.
    Returns a list of NewsStory-s.
    """
    feed = feedparser.parse(url)
    entries = feed.entries
    ret = []
    for entry in entries:
        guid = entry.guid
        title = translate_html(entry.title)
        link = entry.link
        description = translate_html(entry.description)
        pubdate = translate_html(entry.published)

        try:
            pubdate = datetime.strptime(pubdate, "%a, %d %b %Y %H:%M:%S %Z")
            pubdate.replace(tzinfo=pytz.timezone("GMT"))
          #  pubdate = pubdate.astimezone(pytz.timezone('EST'))
          #  pubdate.replace(tzinfo=None)
        except ValueError:
            pubdate = datetime.strptime(pubdate, "%a, %d %b %Y %H:%M:%S %z")

        newsStory = NewsStory(guid, title, description, link, pubdate)
        ret.append(newsStory)
    return ret

#======================
# Data structure design
#======================

# Problem 1

class NewsStory(object):
    '''
    Initializes a NewsStory object
            
    guid (string): the story's globally unique identifier
    title (string): the story's title
    description (string): the story's description
    link (string): story's link to more content
    pubdate (datetime): story's publication date

    A NewsStory object has five attributes:
        self.guid 
        self.title
        self.description
        self.link
        self.pubdate
    '''
    def __init__(self, guid, title, description, link, pubdate):
        self.guid = guid
        self.title = title
        self.description = description
        self.link = link
        self.pubdate = pubdate

    def get_guid(self):
        '''
        Used to safely access self.guid outside of the class
        
        Returns: self.guid
        '''
        return self.guid

    def get_title(self):
        '''
        Used to safely access self.title outside of the class
        
        Returns: self.title
        '''
        return self.title

    def get_description(self):
        '''
        Used to safely access self.description outside of the class
        
        Returns: self.description
        '''
        return self.description

    def get_link(self):
        '''
        Used to safely access self.link outside of the class
        
        Returns: self.link
        '''
        return self.link

    def get_pubdate(self):
        '''
        Used to safely access self.pubdate outside of the class
        
        Returns: self.pubdate
        '''
        return self.pubdate

    


#======================
# Triggers
#======================

class Trigger(object):
    def evaluate(self, story):
        """
        Returns True if an alert should be generated
        for the given news item, or False otherwise.
        """
        # DO NOT CHANGE THIS!
        raise NotImplementedError

# PHRASE TRIGGERS

# Problem 2
class PhraseTrigger(Trigger):
    def __init__(self, phrase):
        self.phrase = phrase.lower()

    def is_phrase_in(self, text):
        text_no_punctuation = []
        phrase_no_punctuation = []
        text = text.lower()
        text = [*text]

        # create list of text without punctuation or spaces
        for char in text:
            if char not in string.punctuation:
                text_no_punctuation.append(char)
            else:
                text_no_punctuation.append(' ')
        text_no_punctuation = ' '.join(''.join(text_no_punctuation).split())
        # text_stripped = 


        # create list of phrase without punctuation or spaces
        for char in self.phrase:
            if char not in string.punctuation:
                phrase_no_punctuation.append(char)
            else:
                phrase_no_punctuation.append(' ')
        phrase_no_punctuation = ' '.join(''.join(phrase_no_punctuation).split())


        # Check if text contains phrase
        return re.search(r"\b{}\b".format(phrase_no_punctuation), text_no_punctuation, re.IGNORECASE) is not None


# Problem 3
class TitleTrigger(PhraseTrigger):
    def evaluate(self, story):
        return self.is_phrase_in(story.get_title())

# Problem 4
class DescriptionTrigger(PhraseTrigger):
    def evaluate(self, story):
        return self.is_phrase_in(story.get_description())

# TIME TRIGGERS

# Problem 5
# Constructor:
#        Input: Time has to be in EST and in the format of "%d %b %Y %H:%M:%S".
#        Convert time from string to a datetime before saving it as an attribute.
class TimeTrigger(Trigger):
    def __init__(self, time_str):
        time = datetime.strptime(time_str, "%d %b %Y %H:%M:%S")
        self.time = time

# Problem 6
class BeforeTrigger(TimeTrigger):
    def evaluate(self, story):
        return (story.get_pubdate() < self.time)

class AfterTrigger(TimeTrigger):
    def evaluate(self, story):
        return (story.get_pubdate() > self.time)


# COMPOSITE TRIGGERS

# Problem 7
# TODO: NotTrigger
class NotTrigger(Trigger):
    def __init__(self, T):
        self.T = T

    def evaluate(self, story):
        return not self.T.evaluate(story)

# Problem 8
class AndTrigger(Trigger):
    def __init__(self, T, U):
        self.T = T
        self.U = U
    
    def evaluate(self, story):
        return self.T.evaluate(story) and self.U.evaluate(story)

# Problem 9
class OrTrigger(Trigger):
    def __init__(self, T, U):
        self.T = T
        self.U = U
    
    def evaluate(self, story):
        return self.T.evaluate(story) or self.U.evaluate(story)


#======================
# Filtering
#======================

# Problem 10
def filter_stories(stories, triggerlist):
    """
    Takes in a list of NewsStory instances.

    Returns: a list of only the stories for which a trigger in triggerlist fires.
    """
    filtered = []

    for story in stories:
        for item in triggerlist:
            if item.evaluate(story):
                filtered.append(story)
                break

    return filtered



#======================
# User-Specified Triggers
#======================
# Problem 11
def read_trigger_config(filename):
    """
    filename: the name of a trigger configuration file

    Returns: a list of trigger objects specified by the trigger configuration
        file.
    """
    # We give you the code to read in the file and eliminate blank lines and
    # comments. You don't need to know how it works for now!
    trigger_file = open(filename, 'r')
    lines = []
    for line in trigger_file:
        line = line.rstrip()
        if not (len(line) == 0 or line.startswith('//')):
            lines.append(line)

    # line is the list of lines that you need to parse and for which you need
    # to build triggers

    trigger_mapping = {
        "TITLE": TitleTrigger,
        "DESCRIPTION": DescriptionTrigger,
        "AFTER": AfterTrigger,
        "BEFORE": BeforeTrigger,
        "NOT": NotTrigger,
        "AND": AndTrigger,
        "OR": OrTrigger
    }

    trigger_dict = {}
    trigger_list = []

    # TODO:
    # Finish implementing problem 11

        

    # print(lines) # for now, print it so you see what it contains!



SLEEPTIME = 120 #seconds -- how often we poll

def main_thread(master):
    # A sample trigger list - you might need to change the phrases to correspond
    # to what is currently in the news
    try:
        t1 = TitleTrigger("election")
        t2 = DescriptionTrigger("Trump")
        t3 = DescriptionTrigger("Clinton")
        t4 = AndTrigger(t2, t3)
        triggerlist = [t1, t4]

        # Problem 11
        # TODO: After implementing read_trigger_config, uncomment this line 
        # triggerlist = read_trigger_config('triggers.txt')
        
        # HELPER CODE - you don't need to understand this!
        # Draws the popup window that displays the filtered stories
        # Retrieves and filters the stories from the RSS feeds
        frame = Frame(master)
        frame.pack(side=BOTTOM)
        scrollbar = Scrollbar(master)
        scrollbar.pack(side=RIGHT,fill=Y)

        t = "Google & Yahoo Top News"
        title = StringVar()
        title.set(t)
        ttl = Label(master, textvariable=title, font=("Helvetica", 18))
        ttl.pack(side=TOP)
        cont = Text(master, font=("Helvetica",14), yscrollcommand=scrollbar.set)
        cont.pack(side=BOTTOM)
        cont.tag_config("title", justify='center')
        button = Button(frame, text="Exit", command=root.destroy)
        button.pack(side=BOTTOM)
        guidShown = []
        def get_cont(newstory):
            if newstory.get_guid() not in guidShown:
                cont.insert(END, newstory.get_title()+"\n", "title")
                cont.insert(END, "\n---------------------------------------------------------------\n", "title")
                cont.insert(END, newstory.get_description())
                cont.insert(END, "\n*********************************************************************\n", "title")
                guidShown.append(newstory.get_guid())

        while True:

            print("Polling . . .", end=' ')
            # Get stories from Google's Top Stories RSS news feed
            stories = process("http://news.google.com/news?output=rss")

            # Get stories from Yahoo's Top Stories RSS news feed
            # stories.extend(process("http://news.yahoo.com/rss/topstories"))

            stories = filter_stories(stories, triggerlist)

            list(map(get_cont, stories))
            scrollbar.config(command=cont.yview)


            print("Sleeping...")
            time.sleep(SLEEPTIME)

    except Exception as e:
        print(e)


if __name__ == '__main__':
    root = Tk()
    root.title("Some RSS parser")
    t = threading.Thread(target=main_thread, args=(root,))
    t.start()
    root.mainloop()

