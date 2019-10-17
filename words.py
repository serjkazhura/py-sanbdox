#!/usr/bin/env python3
"""Retrieve and print documents from the url.

Usage:
  python words.py <URL>
"""

import sys
from urllib.request import urlopen

def fetch_words(url):
  """Fetch a list of words from a url.

  Args:
    url: The url of a UTF-8 resource

  Returns:
    A list of string containing words from the document.
  """
  with urlopen(url) as story:
    story_words = []
    for line in story:
      line_words = line.decode('utf-8').split()
      for word in line_words:
        story_words.append(word)
  return story_words


def print_items(items):
  """Print items one per line.
  
  Args: 
    An iterable series of printable items.
  """
  for item in items:
    print(item)


def main(url):
  """Print each word from a text document

  Args:
    url: the url of a UTF-8 resource
  """
  words = fetch_words(url)
  print_items(words)


if __name__ == '__main__':
  main(sys.argv[1]) # args[0] is the module name itself.