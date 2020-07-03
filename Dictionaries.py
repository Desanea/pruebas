students = ["Bob", 12, "Rachel", 13, "Emily", 15 ]
print(students)
students = {"Bob":12, "Rachel":13, "Emily":15}
print(students)
print(students["Rachel"])
print(students["Emily"])
print(students["Bob"])
#Update de la edad de Rachel
students["Rachel"]=15
print(students)
#Delete one element from dictionary
del students["Emily"]
print(students)
#Length function permite saber la cantidad de elementos en el dictionary
print(len(students))
