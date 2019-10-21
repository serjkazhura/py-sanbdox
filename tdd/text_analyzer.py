import os
import unittest

def analyze_text(filename):
  """Calculate the number of lines and characters in the file.

  Args:
    filename: The name of the fileto analyze.

  Raises: 
    IOError: if the file does not exist.

  Returns: A tuple where the first element is the number of lines in
    the file and the second element is the number of characters.
    
  """
  lines = 0
  chars = 0
  with open(filename, mode='r', encoding='utf-8') as f:
    for line in f:
      lines += 1
      chars += len(line)
  return (lines, chars)


class TextAnalysisTests(unittest.TestCase):
  """Tests for the ``analyze_text()`` function
  """

  def setUp(self):
    """Fixture that creates a file for the text method to use.
    """
    self.filename = 'text_analysis_test_file.txt'
    with open(self.filename, mode='w', encoding='utf-8') as f:
      f.write('Now we are engaged in a great civil war.\n'
              'testing whether that nation,\n'
              'or any nation so conceived and so dedicated,\n'
              'can long endure.')
  
  def tearDown(self):
    """Fixture that deletes the files used by the test methods.
    """
    try:
      os.remove(self.filename)
    except:
      pass

  def test_function_runs(self):
    """Basic smoke test: does the function run at all.
    """
    analyze_text(self.filename)

  def test_line_count(self):
    """Check that the line count is correct."""
    self.assertEqual(analyze_text(self.filename)[0], 4)

  def test_character_count(self):
    """Check the number of characters in the file."""
    self.assertEqual(analyze_text(self.filename)[1], 131)

  def test_no_such_file(self):
    """Check the proper exception is thrown for a missing file."""
    with self.assertRaises(IOError):
      analyze_text('fizzbuzz')

  def test_no_deletion(self):
    """Check that the function does not delete the input file."""
    analyze_text(self.filename)
    self.assertTrue(os.path.exists(self.filename))


if __name__ == '__main__':
  unittest.main()