import unittest

class Testing(unittest.TestCase):
    def test_IsPrime(self):
        from SimpleStuff.math import IsPrime
        tst_ans =[2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97]
        ans=[]
        for i in range(1,101):
            if IsPrime(i):
                ans.append(i)
        self.assertEqual(ans,tst_ans)


    def test_gcd(self):
        from SimpleStuff.math import gcd
        cases = [   (10, 12, 2), 
                    (10, 13, 1),
                    (20, 40, 20),
                    (24, 24, 24),
                    (24, 8, 8),
                    (11571, 1767, 57)
                ]
        for case in cases:
            a, b, ans = case
            self.assertEqual(gcd([a,b]), ans )

        self.assertEqual(gcd([40,440,44]), 4 )

    def test_lcm(self):
        from SimpleStuff.math import lcm
        cases = [   (10, 12, 60),
                    (10, 13, 130),
                    (20, 40, 40),
                    (24, 24, 24),
                    (24, 8, 24)
                ]

        for case in cases:
            a, b, ans = case
            self.assertEqual(lcm([a,b]), ans )

if __name__=='__main__':
    unittest.main()
