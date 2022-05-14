#!/usr/bin/env python
# coding: utf-8

# In[39]:


import nltk
#nltk.download()


# In[43]:


class accessing_text:
    def web_method(self):
        from urllib.request import urlopen
        import os
        url="http://www.gutenburg.org/files/2554/2554.txt"
        raw=urlopen(url).read()
        print("Web technique good")
        #return raw
    def html_method():
        html="http://news.bbc.co.uk/2/hi/health/2284783.stm"
        data=urlopen(html).read()
        raw-nltk.clean_html(data)
        return raw
    def rss_method(self):
        import feedparser
        feed=feedparser.parse("http://languagelog.ldc.upenn.edu/nll/?feed=atom")
        feed['feed','title']
        post=feed.entries[2]
        raw=post.content[0].value
        return raw
    def nltk_Files_method(self):
        import nltk
        path=nltk.data.find('corpora/gutenberg/melville-moby_dick.txt')
        raw=open(path, 'rU').read()
    def localFiles_method(self):
        import os
        try:
            os.listdir('.')
            file=open("filename.txt")
            raw=file.read()
        except:
            file.close()
    def pdf_method(self):
        # use Pypdf and PyWin32
        print("Iko sawa")
        pass
class tokenize_text:
    def ___init___():
        import nltk
        raw_text=raw
    def text_tokenization():
        text_tokens=nltk.tokenize(raw_text)


# In[46]:


a=accessing_text()
a.pdf_method()
#print(a)


# In[ ]:


class Machine:
    def __init__():
        print("Init started")
    def identify():
        print("Now identifying")
Machine
a=Machine.identify()


# In[ ]:




