# nude-finder

A command line tool to recursively search images with nudity. `nude-finder` is a simple client for [nudepy](https://github.com/hhatto/nude.py) that allows you to make recursive searchs in a given directory. Images that has some nudity will be printed in the console with their path relative to the current working directory. 

Since *nudepy* is an outdated port of [nude.js](https://github.com/pa7/nude.js) to Python, I have to say that `nudepy` is not a reliable tool for nudity check. It's results are very poor and you cannot use latest versions of Python 3 (like Python 3.5).

## How to Use

Clone this repository or download it's zip, open the Terminal and then install this package using `pip`: 

```
# Assuming you're using Python 2.7
sudo pip install .
```

Now close this Terminal and open a new one to update the PATH. In order to run `nude-finder` you have the following alternatives:

```
# Run for the current working directory.
nude-finder

# Will make a recursive search inside 'somefolder/path/'.
nude-finder somefolder/path/

```

That's all, folks.

## About

Created by (a drunk) Fernando Paladini in one hour or so.
