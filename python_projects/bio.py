bio = {"Height" : "200",
       "Weight" : "80",
       "Hair" : "Brown"
}

q = input("Чтобы вы хотели знать о себе?")
if q in bio:
    result = bio[q]
    print (result)
else:
    print("Такого параетра нет в списке")
