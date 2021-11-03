import re

'''
  Description: Automatic documentation code scraper for the N1QL QUERY SCRAPING.
  
  I/O:-
  .adoc document having any N1QL QUERY.
  
  dummy.adoc as the input

  Extracted as
   example.n1.ql
'''
file_name= "subquery"
with open("subqueries.adoc") as f1:
    x = [re.sub(r'\s+(?!$)', ' ', match) for match in re.findall(r'\[source[^,]*,n1ql\]\n----\n([A-Z].*?\n)(?=----)', "".join(f1.readlines()), re.DOTALL)]

for i, query in enumerate(x, start=1):
    filename = file_name+f"-{str(i)}.n1ql"
    print(i)
    with open(filename, 'a') as f2:
        f2.write(query)
