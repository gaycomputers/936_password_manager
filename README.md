# 936_password_manager
## NOTE:  
This is not intended to be a secure way to generate passwords. In fact, it is probably extremely insecure, I am pretty sure someone smarter than me might be able to take 2 generated passwords and deduce their shared salt.

It is a pretty fun way to learn new words though.
</pre>
### Known issues:  
If nltk.corpus changes the order or size of the words dictionary, this program will not generate the same password it used to, and will be proven useless as a password MANAGER. So, probably save any passwords generated to a keychain or something, or snapshot the words list at the time of generation and use that forever.

### How to install: 
<pre>
    $ pipenv run python3
    >>>import nltk
    >>> nltk.download() 
    NLTK Downloader
    ---------------------------------------------------------------------------
         d) Download   l) List    u) Update   c) Config   h) Help   q) Quit
    ---------------------------------------------------------------------------
    Downloader> d
    
    Download which package (l=list; x=cancel)?
      Identifier> words
        Downloading package words to /home/trisimix/nltk_data...
          Package words is already up-to-date!
    
    ---------------------------------------------------------------------------
        d) Download   l) List    u) Update   c) Config   h) Help   q) Quit
    ---------------------------------------------------------------------------
    Downloader> q
    True
    >>> exit()
</pre>

### Usage:
<pre>
    $ pipenv run python3 936.py
</pre>
