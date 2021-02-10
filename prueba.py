mi_lista=[["123", "Ana", "Torres", "23", 30000], ["456", "Pablo", "Perez", "32", 35000], ["789", "Andres", "Molina", "56", 43000]]

var_id=input("Ingrese el id que desea agregar: ")

validacion=True

for i in range(0,3):
	if mi_lista[i][0] == var_id:
		print("Empleado encontrado no se puede ingresar nuevamente.")
		print(var_id)
		validacion=False


	
if validacion:
	var_nom=input("ingrese nombre de el empleado: ")
	var_ape=input("ingrese apellido de el empleado: ")
	var_edad=input("ingrese edad de el empleado: ")
	var_sal=float(input("ingrese el salario de el empleado: "))

	mi_lista2=[var_id, var_nom, var_ape, var_edad, var_sal]

	mi_lista+=mi_lista2

	print(mi_lista)
