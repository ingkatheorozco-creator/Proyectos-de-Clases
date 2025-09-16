#De una empresa de N empleados, necesitamos obtener él numero de empleado
#y sueldo del trabajador con el mayor sueldo de la empresa. Realice el programa

#FASE I

#Datos de entrada
#Cantidad de empleados
#Sueldos de los trabajadores

#Proceso
#Determinar el trabajador con el mayor sueldo
#Determinar el numero del empleado

#Datos de salida
#El numero de trabajador con el mayor sueldo de la empresa
#Sueldo del trabajador con mayor sueldo

#Diseño del Algoritmo
#Ingresar cantidad de empleados
#Ingresar los sueldos de los trabajadores
#Calcular el trabajador con el mayor sueldo
#Determinar el numero del empleado
#Imprimir el numero del trabajador con el mayor sueldo
#Imprimir el sueldo del trabajador con el mayor sueldo


N=0; #cantidad_empleados
i=0;
mayor=0;
sumasueldos=0;
numero=0;

N = int(input("Por favor ingrese el número de empleados "))

while i<N:
    sueldos=int(input(f"Por favor, ingrese el sueldo del trabajador {i+1} "))
    sumasueldos= sueldos + sumasueldos
    
    if(sueldos > mayor):
        mayor= sueldos
        numero= i+1
    i=i+1
    
print("El numero del trabajador es " , numero)
print("El sueldo del trabajador mayor es ", mayor )

    
