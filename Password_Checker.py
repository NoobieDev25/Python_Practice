#Input que almacenara el password cuando los datos sean introduccidos.
Entrada_Password =(input("Introduzca su password: "))

#Caracteristicas importantes en un password en las que influiran si el password es seguro o podria ser mejor.
longitud = len(Entrada_Password) >= 8
tiene_num = any(c.isdigit() for c in Entrada_Password)
tiene_simbolo = any(c in "!@#$*()#" for c in Entrada_Password)

#Los puntos representan cuanto cumple el password ccon las carateristicas

puntos =  longitud + tiene_num + tiene_simbolo

#If que se encargara de la entrada de los datos, le mencionara al usuario si el password es seguro o es mejorable en diferentes niveles.
if puntos == 3:
    print("Su password es fuerte.")
elif puntos == 2:
    print("Su password no es tan fuerte.")
elif puntos == 1:
    print("Su password es debil")
else:
    print("Su password es muy debil")