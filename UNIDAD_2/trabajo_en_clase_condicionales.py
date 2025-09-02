#programa para instituto de ingles

#ingreso del dia,numero y mes

print("bienvenido/a al sistema!!!")
dia_str=input("porfavor ingrese la fecha que desea buscar dia, dd/mm: ").lower()
dia= dia_str.split(",")
dia_semana=dia[0]
dd, mm = dia[1].strip().split('/')
dd=int(dd)
mm=int(mm)
print(f"{dia}, {dd}/{mm}")

if dia_semana =="lunes"or dia_semana=="martes"or dia_semana== "miercoles"or dia_semana=="jueves"or dia_semana=="viernes":
    if dd<31 and dd>0:
         if  mm<12 and mm>0:

#ahora vamos a indicar a el nivel de aprendizaje que corresponde el dia ingresado

            if dia_semana=="lunes":   
                print("este dia es del nivel inicial\n")
            elif dia_semana=="martes":
                print("este dia pertenece al nivel intermedio \n") 
            elif dia_semana=="miercoles":
                print("este dia pertenece al nivel avanzado \n") 
            elif dia_semana=="jueves":
                print("este dia pertenece al clases de voz \n")
            elif dia_semana=="viernes":
                print("este dia pertenece a ingles viajero \n")  

#ahora el usuario indicara dependiendo el dia si hubo examenes o no    
if dia_semana =="lunes"or dia_semana=="martes"or dia_semana== "miercoles":
    examen=input("hubo examen ese dia? si/no : ")    
    if examen=="si":
        asistencia=int(input("cuantos alumnos asistieron ese dia?: "))
        nota=int(input("cuantos alumnos aprobaron?: "))
        print(f"si asistieron {asistencia} alumnos y aprobaron {nota} entoces aprobo un ",(nota/asistencia)*100,"%"" de alumnos")

#ahora indicara el caso si el dia seleccionado fue "jueves"
if dia_semana=="jueves":
    total_alumnos=int(input("cuantos alumnos son en total en las clases de voz: "))
    asistencia=int(input("cuantos alumnos asistieron ese dia: "))
    if (asistencia/total_alumnos)*100 > 50 :
        print("asistio mas del 50% de la clase")
    else:
        print("asistio menos del 50% de la clase")

if dia_semana=="viernes" and dd == 1 and mm==1 or dd==1 and mm==7:
       print("COMIENZO DE NUEVO CICLO!!!")
       nuevos_alumnos=int(input("ingrese la cantidad de alumnos del nuevo ciclo: "))
       arancel=float(input("ingrese la cuota mensual que debera abonar cada almuno: "))

       print(f"la totalidad de almunos del nuevo ciclo es de {nuevos_alumnos} alumnos, los cuales deberan abonar por mes una cuota de ${arancel}, dando un ingreso total mensual de ${arancel*nuevos_alumnos}")
       
else:
        alumnos=int(input("ingrese la cantidad actual de alumnos: "))
        arancel=float(input("ingrese la cuota mensual definida de este ciclo: "))
        print(f"la totalidad de almunos de este ciclo es de {alumnos} alumnos, los cuales deberan abonar por mes una cuota de ${arancel}, dando un ingreso total mensual de ${arancel*alumnos}")