#merge two dictionaries
a = {"one":1,"two":2,"three":3}
b = {"three":33,"four":4,"five":5}
c = a | b       # or a.update(b)

print(c)