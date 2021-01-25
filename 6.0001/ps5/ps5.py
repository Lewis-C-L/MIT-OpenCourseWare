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
    def __init__(self, guid, title, description, link, pubdate):
        """
        Initializes a NewsStory object
                
               guid (string): Global unique identifier.
              title (string): The news story's headline.
        description (string): A paragraph or so summarizing the news story.
               link (string): A link to a website with the entire story.
          pubdate (datetime): Date the news was published.

        a NewsStory object has five attributes:
            self.guid (string, determined by input text)
            self.title (string, determined by input text)
            self.desciption (string, determined by input text)
            self.link (string, determined by input text)
            self.pubdate (datetime, determined by input)          
        """
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





# TODO: NewsStory


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
# TODO: PhraseTrigger
class PhraseTrigger(Trigger):
    def __init__(self,phrase):
        '''
        
        '''
        self.phrase = phrase
        
    def get_phrase(self):
        return self.phrase
    
    def is_phrase_in (self,text):
        '''
        '''
        ## convert text into a easy to compare format ##
        text = text.lower()                      # all lower case     
        punct = [x for x in string.punctuation]  # punctuations as a list    
        for ch in punct:                         # replace punctuations with spaces
            if ch in text:
                text = text.replace(ch,' ')               
        text = re.sub(' '+'{2,}',' ',text)       # convert multiple spaces into single space 
         
        ## is phrase in text##
        return self.get_phrase().lower() +' ' in text +' ' 
        # the added space at the end of phrase removes cases where phrase is contained within another word. eg car and cars
        # the added space at the end of the text deals with the case that the text ends with the phrase. ie searching for 'car ' but text would be 'car'
        
        
        
# Problem 3
# TODO: TitleTrigger
class TitleTrigger(PhraseTrigger):
    '''
    Return True if phrase is found in story's title. False otherwise
    '''
    def __init__(self, phrase):
        PhraseTrigger.__init__(self, phrase)
    
    def evaluate(self, story):
        return self.is_phrase_in(story.get_title())
    

            

# Problem 4
# TODO: DescriptionTrigger
class DescriptionTrigger(PhraseTrigger):
    '''
    Return True if phrase is found in story's description. False otherwise
    '''
    def __init__(self, phrase):
        PhraseTrigger.__init__(self, phrase)
    
    def evaluate(self, story):
        return self.is_phrase_in(story.get_description())

# TIME TRIGGERS

# Problem 5
# TODO: TimeTrigger
# Constructor:
#        Input: Time has to be in EST and in the format of "%d %b %Y %H:%M:%S".
#        Convert time from string to a datetime before saving it as an attribute.
class TimeTrigger(Trigger):
    '''
    Input: Time has to be in EST and in the format of "%d %b %Y %H:%M:%S".
    Convert time from string to a datetime before saving it as an attribute.
    '''
    def __init__(self,datetime_string):
        self.datetime = datetime.strptime(datetime_string,"%d %b %Y %H:%M:%S").replace(tzinfo=pytz.timezone("EST"))
        
    def get_datetime(self):
        return self.datetime
    
# Problem 6
# TODO: BeforeTrigger and AfterTrigger
class BeforeTrigger(TimeTrigger):
    def __init__(self, datetime_string):
        TimeTrigger.__init__(self,datetime_string)
   
    def evaluate(self, story):
        return self.datetime > story.get_pubdate().replace(tzinfo=pytz.timezone("EST"))
        


class AfterTrigger(TimeTrigger):
    def __init__(self, datetime_string):
        TimeTrigger.__init__(self,datetime_string)
    
    def evaluate(self, story):
        return self.datetime < story.get_pubdate().replace(tzinfo=pytz.timezone("EST"))

# COMPOSITE TRIGGERS

# Problem 7
# TODO: NotTrigger
class NotTrigger(Trigger):
    def __init__(self,trigger):
        self.trigger = trigger
        
    def get_trigger(self):
        return self.trigger
    
    def evaluate(self, story):
        return not self.get_trigger().evaluate(story)
# Problem 8
# TODO: AndTrigger
class AndTrigger(Trigger):
    def __init__(self, trigger1, trigger2):
        self.trigger1 = trigger1
        self.trigger2 = trigger2
    
    def get_trigger1(self):
        return self.trigger1
    def get_trigger2(self):
        return self.trigger2
    
    def evaluate(self, story):
        return self.get_trigger1().evaluate(story) and self.get_trigger2().evaluate(story)

# Problem 9
# TODO: OrTrigger

class OrTrigger(Trigger):
    def __init__(self, trigger1, trigger2):
        self.trigger1 = trigger1
        self.trigger2 = trigger2
    
    def get_trigger1(self):
        return self.trigger1
    def get_trigger2(self):
        return self.trigger2
    
    def evaluate(self, story):
        return self.get_trigger1().evaluate(story) or self.get_trigger2().evaluate(story)


#======================
# Filtering
#======================

# Problem 10
def filter_stories(stories, triggerlist):
    """
    Takes in a list of NewsStory instances.

    Returns: a list of only the stories for which a trigger in triggerlist fires.
    """
    # TODO: Problem 10
    # This is a placeholder
    # (we're just returning all the stories, with no filtering)
    list1 = [[x.evaluate(y) for x in triggerlist] for y in stories]
    list2 = map(any,list1)
    return [x[0] for x in zip(stories,list2) if x[1] == True]


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

    # TODO: Problem 11
    # line is the list of lines that you need to parse and for which you need
    # to build triggers

    print(lines) # for now, print it so you see what it contains!



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
            stories.extend(process("http://news.yahoo.com/rss/topstories"))

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

