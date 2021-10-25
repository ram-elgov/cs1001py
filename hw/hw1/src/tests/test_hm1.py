import unittest
import hw1_206867517
import max_even_seq


class TestHm1(unittest.TestCase):

    def test_4a(self):
        self.assertEqual(hw1_206867517.num_different_letters(""), 0)
        self.assertEqual(hw1_206867517.num_different_letters("aaaaaaaaaaa"), 1)
        self.assertEqual(hw1_206867517.num_different_letters("aaaaaaaaa1"), 1)
        self.assertEqual(hw1_206867517.num_different_letters("aaa bbb ccc aaa bbb ccc d 1 "), 4)
        self.assertEqual(hw1_206867517.num_different_letters("123456 789456"), 0)
        self.assertEqual(hw1_206867517.num_different_letters("abcdefghijklmnopqrstuvwxyz"), 26)
        self.assertEqual(hw1_206867517.num_different_letters("123456789123456789"), 0)
        self.assertEqual(hw1_206867517.num_different_letters(" "), 0)
        self.assertEqual(hw1_206867517.num_different_letters("                1a"), 1)
        self.assertEqual(hw1_206867517.num_different_letters("aaaaaaaaaaaaabaaaaaaaaaaaaaa"), 2)
        self.assertEqual(hw1_206867517.num_different_letters("aaa98765432100000000"), 1)

    def test_4b(self):
        self.assertEqual(hw1_206867517.replace_char("", 'a', 'b'), "")
        self.assertEqual(hw1_206867517.replace_char("a", 'a', 'b'), "b")
        self.assertEqual(hw1_206867517.replace_char("123", 'a', 'b'), "123")
        self.assertEqual(hw1_206867517.replace_char("123bbcc", 'a', 'b'), "123bbcc")
        self.assertEqual(hw1_206867517.replace_char("axaxaxaxaxaxa", 'a', 'b'), "bxbxbxbxbxbxb")
        self.assertEqual(hw1_206867517.replace_char("axxaxxaxxaxxaaaa", 'a', 'b'), "bxxbxxbxxbxxbbbb")
        self.assertEqual(hw1_206867517.replace_char("sdfghjkl", 'a', 'b'), "sdfghjkl")
        self.assertEqual(hw1_206867517.replace_char("bbbbb", 'a', 'b'), "bbbbb")

    def test_4c(self):
        self.assertEqual(hw1_206867517.longest_word("123456789"), 9)
        self.assertEqual(hw1_206867517.longest_word("123456789 10101010101010101010"), 20)
        self.assertEqual(hw1_206867517.longest_word(""), 0)
        self.assertEqual(hw1_206867517.longest_word("       "), 0)
        self.assertEqual(hw1_206867517.longest_word("abababa abababab vbvbv 1212121212"), 10)
        self.assertEqual(hw1_206867517.longest_word("0"), 1)
        self.assertEqual(hw1_206867517.longest_word("0  00   000   0000"), 4)
        self.assertEqual(hw1_206867517.longest_word("1 2 3 4 5 6 7 8 9 0"), 1)

    def test_4d(self):
        self.assertEqual(hw1_206867517.to_upper("123456789"), "123456789")
        self.assertEqual(hw1_206867517.to_upper(""), "")
        self.assertEqual(hw1_206867517.to_upper("ABCD"), "ABCD")
        self.assertEqual(hw1_206867517.to_upper("abcd"), "ABCD")
        self.assertEqual(hw1_206867517.to_upper("abcd ABCD"), "ABCD ABCD")
        self.assertEqual(hw1_206867517.to_upper("     "), "     ")
        self.assertEqual(hw1_206867517.to_upper("aaaaaaa bbbbbb cccccc dddddd"), "AAAAAAA BBBBBB CCCCCC DDDDDD")
        self.assertEqual(hw1_206867517.to_upper("aaaaaaa 123456 cccccc DDDDDD"), "AAAAAAA 123456 CCCCCC DDDDDD")
        self.assertEqual(hw1_206867517.to_upper(" 123456 cccccc DDDDDD"), " 123456 CCCCCC DDDDDD")

    def test_5(self):
        self.assertEqual(hw1_206867517.calc(""), "")
        self.assertEqual(hw1_206867517.calc("''"), "")
        self.assertEqual(hw1_206867517.calc("'a'"), "a")
        self.assertEqual(hw1_206867517.calc("'a'+'b'"), "ab")
        self.assertEqual(hw1_206867517.calc("'a'*'3'"), "aaa")
        self.assertEqual(hw1_206867517.calc("'123'"), "123")
        self.assertEqual(hw1_206867517.calc("'123'+'abc'*'2'"), "123abc123abc")
        self.assertEqual(hw1_206867517.calc("'123'+' abc'*'2'"), "123 abc123 abc")
        self.assertEqual(hw1_206867517.calc("'123 '+'abc '*'2'"), "123 abc 123 abc ")
        self.assertEqual(hw1_206867517.calc("'123 '+'abc '*'2'+'123'"), "123 abc 123 abc 123")
        self.assertEqual(hw1_206867517.calc("'123+'+'123'"), "123+123")
        self.assertEqual(hw1_206867517.calc("'123*'*'2'"), "123*123*")
        self.assertEqual(hw1_206867517.calc("''+'123'"), "123")
        self.assertEqual(hw1_206867517.calc("''*'5'"), "")
        self.assertEqual(hw1_206867517.calc("''*'5'+'3'"), "3")
        self.assertEqual(hw1_206867517.calc("''+'3'*'3'"), "333")
        self.assertEqual(hw1_206867517.calc("'*'*'5'"), "*****")
        self.assertEqual(hw1_206867517.calc("'+'+'aaa'"), "+aaa")
        self.assertEqual(hw1_206867517.calc("'123321'*'2'"), "123321123321")
        self.assertEqual(hw1_206867517.calc("'Hi there '*'3'+'you2'"), "Hi there Hi there Hi there you2")
        self.assertEqual(hw1_206867517.calc("'hi+fi'*'2'*'2'"), "hi+fihi+fihi+fihi+fi")

    def test_max_even_seq(self):
        self.assertEqual(max_even_seq.max_even_seq(0), 1)
        self.assertEqual(max_even_seq.max_even_seq(22), 2)
        self.assertEqual(max_even_seq.max_even_seq(22220), 5)
        self.assertEqual(max_even_seq.max_even_seq(100000), 5)
        self.assertEqual(max_even_seq.max_even_seq(2200366882), 5)
        self.assertEqual(max_even_seq.max_even_seq(220056688), 4)
        self.assertEqual(max_even_seq.max_even_seq(11111111111), 0)
        self.assertEqual(max_even_seq.max_even_seq(13579), 0)
        self.assertEqual(max_even_seq.max_even_seq(24680), 5)
        self.assertEqual(max_even_seq.max_even_seq(11111221212121218888), 4)
        self.assertEqual(max_even_seq.max_even_seq(23300247524689), 4)
        self.assertEqual(max_even_seq.max_even_seq(10020003000040000050000060000000700000000800000000090000000000), 18)
        self.assertEqual(max_even_seq.max_even_seq(1111222223333334444444555555566666666777777777888888888899999999999),
                         10)
        self.assertEqual(max_even_seq.max_even_seq(7777777777777777), 0)


if __name__ == '__main__':
    unittest.main()
