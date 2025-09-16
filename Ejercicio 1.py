#Calcule el aumento del sueldo para un grupo de N empleados de una empresa teniendo en 
#cuenta el siguiente criterio:  
#Si el sueldo es inferior a $1000000 → AUMENTO 15%  
#Si el sueldo es mayor o igual a $ 1000000 → AUMENTO 12%  
#Imprima el sueldo nuevo del trabajador y el total de nómina de la empresa, considerando este  nuevo aumento  

#Fase I

#Datos de entrada
#Sueldos de los empleados

#Proceso
#Calcular el aumento del 15 para los sueldos correspondientes
#Calcular el aumento del 12 para los sueldos correspondientes


#Datos de salida
#Sueldo del nuevo trabajador
#Total de la nomina de la empresa con el aumento incluido

#Diseño del algoritmo

sueldos=0;
aumento15=0;
aumento12=0;
mayor=0;
inferior=0;
sueldossin=0;
nomina_total=0;
i=0;
cantidad_empleados=0;
numero=0;


cantidad_empleados= int(input("Por favor ingresar la cantidad de empleados ", ))

while i<cantidad_empleados:
    sueldos=int(input(f"Por favor, ingrese el sueldo del empleado {i+1} "))
    sueldossin=sueldos + sueldossin
    if sueldossin<1000000:
        inferior=sueldos
        numero= i+1
        aumento15= (sueldos*0.15)+sueldos
        nomina_total=nomina_total+aumento15
        print("El sueldo del trabajador es ", aumento15)
    if sueldossin>=1000000:
        mayor=sueldos
        numero= i+1
        aumento12= (sueldos*0.12)+sueldos
        nomina_total=nomina_total+aumento12
        print("El sueldo del trabajador es ", aumento12)

print("La nomina total es ", nomina_total)

