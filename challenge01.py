icecream = ["indentation", "spaces"]
tlgstudents= ["Bryan", "Colin", "Erik", "Gregory", "John", "Kishor", "Leia", "Maria", "Monte", "Jarrad", "Pemba", "Don", "Tim", "Travis", "Trung"]
icecream.append(4)
studentid= int(input("Enter a number from 0 - 14: "))
selection= tlgstudents[int(studentid)]
# <s
print(selection + "always uses" + str(icecream[2]) + icecream[1] + "to indent.")



# F-STRING
print(f"{selection} always uses {icecream[2]} {icecream[1]} to indent.")


