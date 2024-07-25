many1 = {"762.3227.21.8", "231.31231.32.912", "3213.42.5321.08"}

req = input("Enter coordinates: ")
many1.add(req)
if req in many1:
    print("This coordinates has already been added.")
else:
    print("Added succesfully.")
