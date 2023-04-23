import unittest
import calc

class TestCalc(unittest.TestCase):

    def test_add(self):
        self.assertEquals(calc.add(10,5),15)
        self.assertEquals(calc.add(-1,1),0)
        self.assertEquals(calc.add(-1,-1),-2)

    def test_subtract(self):
        self.assertEquals(calc.subtract(10,5),5)
        self.assertEquals(calc.subtract(-1,1),-2)
        self.assertEquals(calc.subtract(-1,-1),0)


    def test_multyply(self):
        self.assertEquals(calc.multyply(10,5),50)
        self.assertEquals(calc.multyply(-1,1),-1)
        self.assertEquals(calc.multyply(-1,-1),1)


    def test_divide(self):
        self.assertEquals(calc.divide(10,5),2)
        self.assertEquals(calc.divide(-1,1),-1)
        self.assertEquals(calc.divide(-1,-1),1)
        self.assertEquals(calc.divide(5,2),2.5)

        self.assertRaises(ValueError,calc.divide, 10, 0)

        with self.assertRaises(ValueError):
            calc.divide(10,0)


if __name__ == "__main__":
    unittest.main()

