import unittest


import unittest

import display

class DisplayTest(unittest.TestCase):

    def test_conversion(self):
        self.assertEqual(display.convert_number(0),
    """ _ 
| |
|_|""")
        self.assertEqual(display.convert_number(1),
     """   
  |
  |""")
        self.assertEqual(display.convert_number(2),
     """ _ 
 _|
|_ """)
        self.assertEqual(display.convert_number(3),
     """ _ 
 _|
 _|""")
        self.assertEqual(display.convert_number(4),
     """   
|_|
  |""")
        self.assertEqual(display.convert_number(5),
     """ _ 
|_ 
 _|""")
        self.assertEqual(display.convert_number(6),
     """ _ 
|_ 
|_|""")
        self.assertEqual(display.convert_number(7),
     """ _ 
  |
  |""")
        self.assertEqual(display.convert_number(8),
     """ _ 
|_|
|_|""")
        self.assertEqual(display.convert_number(9),
     """ _ 
|_|
 _|""")
        self.assertEqual(display.convert_number(), "")
        self.assertEqual(display.convert_number(1978),
     """    _  _  _ 
  ||_|  ||_|
  | _|  ||_|""")
        self.assertEqual(display.convert_number(7616016985426318),
     """ _  _     _  _     _  _  _  _     _  _  _     _ 
  ||_   ||_ | |  ||_ |_||_||_ |_| _||_  _|  ||_|
  ||_|  ||_||_|  ||_| _||_| _|  ||_ |_| _|  ||_|""")