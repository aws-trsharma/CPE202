import unittest
import filecmp
from huffman_coding import cnt_freq, create_huff_tree, create_code, huffman_encode
from min_pq import MinPQ
class TestList(unittest.TestCase):

   def test_pq(self):
      pq = MinPQ()
      self.assertTrue(pq.is_empty())
      for i in reversed(range(5)):
         print("pq.insert(", i, ")")
         pq.insert(i)
      self.assertEqual(pq.size(), 5)
      self.assertFalse(pq.is_empty())
      self.assertEqual(pq.min(), 0)
      self.assertEqual(pq.del_min(), 0)
      self.assertEqual(pq.del_min(), 1)
      self.assertEqual(pq.del_min(), 2)
      self.assertEqual(pq.del_min(), 3)
      self.assertEqual(pq.del_min(), 4)
      self.assertTrue(pq.is_empty())
      self.assertEqual(pq.size(), 0)
      arr = [5, 4, 3, 2, 1]
      print(arr)
      pq = MinPQ()
      print("pq.heapify(", arr, ")")
      pq.heapify(arr)
      self.assertEqual(pq.size(), 5)
      self.assertEqual(pq.capacity, 5)
      self.assertFalse(pq.is_empty())
      self.assertEqual(pq.min(), 1)

   def test_cnt_freq(self):
      freqlist = cnt_freq("test1.txt")
      anslist = [0] * 256
      anslist[97:104] = [2, 4, 8, 16, 0, 2, 0]
      self.assertListEqual(freqlist[97:104], anslist[97:104])


   def test_create_huff_tree(self):
      freqlist = cnt_freq("test1.txt")
      hufftree = create_huff_tree(freqlist)
      numchars = 32
      charforroot = "a"
      self.assertEqual(hufftree.freq, 32)
      self.assertEqual(hufftree.char, 'a')
      left = hufftree.left
      self.assertEqual(left.freq, 16)
      self.assertEqual(left.char, 'a')
      right = hufftree.right
      self.assertEqual(right.freq, 16)
      self.assertEqual(right.char, 'd')


def test_create_code(self):
   freqlist = cnt_freq(CURRDIR + "test1.txt")
   hufftree = create_huff_tree(freqlist)
   codes = create_code(hufftree)
   self.assertEqual(codes[ord('d')], '1')
   self.assertEqual(codes[ord('a')], '0000')
   self.assertEqual(codes[ord('f')], '0001')


def test_create_code2(self):
   freqlist = cnt_freq(CURRDIR + "test2.txt")
   hufftree = create_huff_tree(freqlist)
   codes = create_code(hufftree)
   print(codes[ord('g')])
   print(codes[ord('o')])
   print(codes[ord('\n')])
   self.assertEqual(codes[ord('g')], '00')
   self.assertEqual(codes[ord('o')], '01')
   self.assertEqual(codes[ord('\n')], '1000')


def test_create_code3(self):
   freqlist = cnt_freq(CURRDIR + "test3.txt")
   hufftree = create_huff_tree(freqlist)
   codes = create_code(hufftree)
   print(codes[ord('s')])
   print(codes[ord('t')])
   print(codes[ord('\n')])
   self.assertEqual(codes[ord('s')], '111')
   self.assertEqual(codes[ord('t')], '00')
   self.assertEqual(codes[ord('\n')], '10010')


def test_01_encodefile(self):
   huffman_encode(CURRDIR + "test1.txt", "encodetest1.txt")
   # capture errors by running 'filecmp' on your encoded file
   # with a *known* solution file
   self.assertTrue(filecmp.cmp("encodetest1.txt", CURRDIR + "test1.out"))


def test_02_encodefile(self):
   huffman_encode(CURRDIR + "test2.txt", "encodetest2.txt")
   # capture errors by running 'filecmp' on your encoded file
   # with a *known* solution file
   self.assertTrue(filecmp.cmp("encodetest2.txt", CURRDIR + "test2.out"))


def test_03_encodefile(self):
   huffman_encode(CURRDIR + "test3.txt", "encodetest3.txt")
   # capture errors by running 'filecmp' on your encoded file
   # with a *known* solution file
   self.assertTrue(filecmp.cmp("encodetest3.txt", CURRDIR + "test3.out"))


if __name__ == '__main__': 
   unittest.main()
