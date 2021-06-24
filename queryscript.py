import re

'''
  Description: Automatic documentation code scraper for the N1QL QUERY SCRAPING.
  
  I/O:-
  .adoc document having any N1QL QUERY.
  
  dummy.adoc as the input

  Extracted as
   example.n1.ql
   
'''

i = 1
with open("dummy.adoc") as f1:
    ft = f1.read().replace('\n',' ')
    x = re.findall('---- [A-Z].*?;.*? ----', ft)
    for line in x:
        filename = "subquery-"+str(i)+".n1ql"
        i += 1
        print(i)
        with open(filename,'a') as f2:
            f2.write(re.sub(' +', ' ', line).replace('----',' ')+'\n')