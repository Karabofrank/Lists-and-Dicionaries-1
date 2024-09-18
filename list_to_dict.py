'''
Write a program that takes a list as input and returns a dictionary whose keys are the Authors name and values are books that they wrote
'''
print('*******These are the authors')
a = [{"Title":"Book1",
      "Author":"Sizo",
      "Year":2020}, 
      {"Title":"Book2",
       "Author":"Ace",
       "Year":2001},
       {"Title":"Book3",
        "Author":"Sizo",
        "Year":2000},
        {"Title":"Book4",
         "Author":"Bless",
         "Year":2009},
         {"Title":"BookAce",
          "Author":"Ace",
          "Year":2010}]

def list_to_dict(x):
    authors = []
    books = {}

    for i in x:
        if i["Author"] not in authors:
            authors.append(i["Author"])
#
    for n in authors:
        b = []
        for book in x:
            if book["Author"] == n:
                b.append(book["Title"])
        # n is the author name
        books[n] = b   
    
    return books
    
print(list_to_dict(a))