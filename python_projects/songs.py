album1 = ["Song1",
          "Song2",
          "Song3"]

album2 = ["Song4",
          "Song5",
          "Song6"]
         
singers = {"singer1" : [album1],
           "singer2" : [album2]}
          

r = input("Введите вашего исполнителя: ")
if r in singers:
    result = singers[r]
    print (result)
else: print ("Такого исполнителя нет в списке: ")
