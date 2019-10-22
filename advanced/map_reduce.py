from functools import reduce

def count_words(doc):
  normalised_doc = ''.join(c.lower() if c.isalpha() else ' ' for c in doc)
  frequencies = {}
  for word in normalised_doc.split():
    frequencies[word] = frequencies.get(word, 0) + 1
  return frequencies

documents = [
  'It was the best of times, it was the worst of times',
  'I went to the woods because i wished to live deliberately',
  'Friends, Romans, countrymen, lend me your ears;'
  'I don\'t like green eggs and ham. I don\'t like them, Sam-I-Am.'
]

def combine_counts(d1, d2):
  d = d1.copy()
  for word, count in d2.items():
    d[word] = d.get(word, 0) + count
  return d

if __name__ == "__main__":
  total_counts = reduce(combine_counts, map(count_words, documents))
  print(total_counts)
  