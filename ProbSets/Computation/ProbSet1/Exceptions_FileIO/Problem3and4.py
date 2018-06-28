import ContentFilter as cf

cf1 = cf.ContentFilter("file.txt")
cf2 = cf.ContentFilter("cf_example1.txt")
print(cf2.filename)
print(cf2.content)
cf2.uniform("uniform.txt")
cf2.uniform("uniform.txt", mode = 'a', case = 'lower')
cf2.reverse("reverse.txt", unit = 'word')
cf2.reverse("reverse.txt", mode = 'a', unit = 'line')
cf2.transpose("transpose.txt")
