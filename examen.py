from csv import writer


trabajadores = [["isaac",500000],["mati",1500000]]    
sueldos = []    


def sueldos_():
    #print("generando sueldos a los 10 trabajadores de la lista... ")
    while True :
        nombre=input("ingrese el nombre del trabajador: ")
        sueldo=int(input("ingrese el sueldo: "))
        if sueldo<300000 or sueldo>2500000:
            print("Error, rangos de sueldo no valdos...")
            
        else:
            trabajadores.append([nombre,sueldo])
            #sueldos.append([nombre,sueldo])
            print(trabajadores)
            #print(sueldos)
            break

def guardar_csv(lista):
    try:
        open("archivo.csv","x")
    except:
        print("guardando datos csv..")

    w = open("archivo.csv","w",newline="")
    w_csv= writer(w)
    w_csv.writerow(["NOMBRE","SUELDO"])
    w_csv.writerows(lista)
    w.close()
        


def clsi():
    suelm=[]
    suelentre=[]
    sueldomayo=[]
    cont=1
    for i in trabajadores:
        print(f"{cont}) {i[0]} {i[1]}")
        cont +=1
        
        print(i[1])
    

      
        
   
def ver():
 
    alto=0
    bajo=0
    prom=0
    suma=0
    for i in trabajadores:
      sueldos.append(i[1])
      
    alto=max(sueldos)
    bajo=min(sueldos)
    #suma=sum[sueldos]
    prom=suma/len(trabajadores)
    print("sueldo mas alto",alto)
    print("sueld mas bajo",bajo)
    print("guardando info")
    guardar_csv(trabajadores)
    


def trabajador(lista):
    nombre = input("nombre:")
    apellido =input("apellido:")

    sueldo =int(input("sueldo:"))
    trabajadores.append([nombre,apellido,sueldo])
    return "Datos ingresados exitosamente!"





def ver_planilla(trabajadores):#funciona
    print("nombre\tbruto\tsalud\tafp\tliquido")
    for i in trabajadores:
        salud = round(i[1]*0.07)
        afp = round(i[1]*0.12)
        liquido = i[1]-salud-afp
        print(f"{i[0]}\t{i[1]}\t{salud}\t{afp}\t{liquido}")
while True:
    print("Prototipo en Python")
    opc=int(input("1.- Asignar sueldo\n2.-clasificar sueldos\n3.-ver estadisticas\n4.-reporte de sueldos\n5.-exit\n"))
    if opc==1:
        sueldos_()
    elif opc==2:
        clsi()
        print("clsif")
    elif opc==3:
        ver()
        print("ver stats")
    elif opc==4:
        ver_planilla(trabajadores)
        print("reporte")        
    elif opc==5:
        print("salir")
        break
    


