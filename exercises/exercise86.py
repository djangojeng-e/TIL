even_list = [2, 4, 6, 8]
for i in even_list:
    assert i % 2 ==0

# assert methods
# assertAlmostEqual(a, b)   checks that round(a-b, 7) == 0
# assertNotAlmostEqual(a, b) checks that round(a-b, 7) != 0
# assertGreater(a,b) checks that a > b
# assertGreaterEqual(a, b) checks that a >= b
# assertLess(a, b)        checks a < b
# assertLessEqual(a, b)   checks a <= b
# assertRegex(s, r)       checks r.search(s)
# assertNotRegex(s, r)    cheks not r.search(s)
# assertCountEqual(a, b)  checks a and b have the same elements in the same number, regardless of their order.