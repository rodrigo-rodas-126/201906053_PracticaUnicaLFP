import json
import webbrowser

#CARGAR archivo1.json, archivo2.json
lista = []
memoria = []
edades = []
promedios = []
nombres = []
edades = []
estados = []

def datos_edades():
    for e in memoria:
        ename = e["edad"]
        edades.append(ename)
    

def datos_promedios():
    for e in memoria:
        ename = e["promedio"]
        promedios.append(ename)
    

def datos_nombres():
    for e in memoria:
        ename = e["nombre"]
        nombres.append(ename)
    

def datos_estados():
    for e in memoria:
        ename = e["activo"]
        estados.append(ename)
    

def tamaño(lista):
    contador = 0
    for elemento in lista:
        contador+=1
    return contador


def leerJson(direccion):
    file = open(direccion)
    data = json.load(file)
    file.close()
    #for registro in data:
    #    print(registro)
    #print('caragado con exito')
    return(data)

while(True):
    cont=0
    entrada = input('Comando: ')
    entrada = entrada.replace(",", "")


    if 'CARGAR' in entrada:
        memoria.clear()
        lista = entrada.split()
        for elemnt in lista:
            if elemnt.endswith('.json'):                
                dat = leerJson(elemnt)
                for regis in dat:
                    memoria.append(regis)
                    cont +=1
                    #print(regis)
        print("Cargado con exito")

    if 'MAXIMO' in entrada and 'edad' in entrada:
        for e in memoria:
            ename = e["edad"]
            edades.append(ename)
        edades.sort()
        posicion = tamaño(edades)
        print("Edad maxima: ", edades[posicion - 1])
        edades.clear()

    if 'MAXIMO' in entrada and 'promedio' in entrada:
        for e in memoria:
            ename = e["promedio"]
            promedios.append(ename)
        promedios.sort()
        posicion = tamaño(promedios)
        print("Promedio maximo: ", promedios[posicion - 1])
        promedios.clear()
    
    if 'MINIMO' in entrada and 'edad' in entrada:
        for e in memoria:
            ename = e["edad"]
            edades.append(ename)
        edades.sort()
        print("Edad minima: ", edades[0])
        edades.clear()

    if 'MINIMO' in entrada and 'promedio' in entrada:
        for e in memoria:
            ename = e["promedio"]
            promedios.append(ename)
        promedios.sort()
        print("Promedio minimo: ", promedios[0])
        promedios.clear()
        
    if 'SUMA' in entrada and 'edad' in entrada:
        suma = 0
        for e in memoria:
            ename = e["edad"]
            suma = suma + int(ename)
        print('Suma de edades: ', suma)

    if 'SUMA' in entrada and 'promedio' in entrada:
        suma = 0
        for e in memoria:
            ename = e["promedio"]
            suma = suma + float(ename)
        print('Suma de promedios: ', round(suma,2))
                
    if 'CUENTA' in entrada:
        print('Numero de registros: ', tamaño(memoria))

    if 'SELECCIONAR' in entrada and '*' in entrada:
        for ele in memoria:
            print(ele)

    if 'SELECCIONAR' in entrada and 'DONDE nombre =' in entrada:
        cahrl = entrada.split()
        atributo = cahrl[tamaño(cahrl) - 1]
        #print(atributo)
        if atributo.endswith('"'):
            atributo = atributo.replace('"', '')
    
            if entrada.startswith('SELECCIONAR nombre') and 'edad' in entrada and 'promedio' in entrada and 'activo' in entrada:
                for e in memoria:
                    ename = e["nombre"]
                    if ename == atributo:
                        print('Nombre: ', e["nombre"])
                        print('Edad: ', e["edad"])
                        print("Promedio: ", e["promedio"])
                        print("Activo: ", e["activo"])

            elif 'edad' in entrada and 'promedio' in entrada and 'activo' in entrada:
                for e in memoria:
                    ename = e["nombre"]
                    if ename == atributo:
                        print('Edad: ', e["edad"])
                        print("Promedio: ", e["promedio"])
                        print("Activo: ", e["activo"])
            
            elif 'nombre' in entrada and 'promedio' in entrada and 'activo' in entrada:
                for e in memoria:
                    ename = e["nombre"]
                    if ename == atributo:
                        print('Nombre: ', e["nombre"])
                        print("Promedio: ", e["promedio"])
                        print("Activo: ", e["activo"])

            elif 'nombre' in entrada and 'edad' in entrada and 'activo' in entrada:
                for e in memoria:
                    ename = e["nombre"]
                    if ename == atributo:
                        print('Nombre: ', e["nombre"])
                        print("Edad: ", e["edad"])
                        print("Activo: ", e["activo"])

            elif 'nombre' in entrada and 'edad' in entrada and 'promedio' in entrada:
                for e in memoria:
                    ename = e["nombre"]
                    if ename == atributo:
                        print('Nombre: ', e["nombre"])
                        print("Edad: ", e["edad"])
                        print("Promedio: ", e["promedio"])

            elif entrada.startswith('SELECCIONAR promedio') in entrada and 'activo' in entrada:
                for e in memoria:
                    ename = e["nombre"]
                    if ename == atributo:
                        print("Promedio: ", e["promedio"])
                        print("Activo: ", e["activo"])
            
            elif 'activo' in entrada:
                for e in memoria:
                    ename = e["nombre"]
                    if ename == atributo:
                        print("Activo: ", e["activo"])
            
            elif 'promedio' in entrada:
                for e in memoria:
                    ename = e["nombre"]
                    if ename == atributo:
                        print("Promedio: ", e["promedio"])
            
            elif 'edad' in entrada:
                for e in memoria:
                    ename = e["nombre"]
                    if ename == atributo:
                        print("Edad: ", e["edad"])
              
    if 'SELECCIONAR' in entrada and 'DONDE promedio =' in entrada:

        if 'nombre' in entrada and 'edad' in entrada and 'promedio' in entrada and 'activo' in entrada:
            for e in memoria:
                ename = e["promedio"]
                if ename == atributo:
                    print('Nombre: ', e["nombre"])
                    print(e['Edad: ', "edad"])
                    print(e['Promedio: ', "promedio"])
                    print(e['Activo: ', "activo"])
        elif 'edad' in entrada and 'promedio' in entrada and 'activo' in entrada:
            for e in memoria:
                ename = e["promedio"]
                if ename == atributo:
                    print('Edad: ', e["edad"])
                    print("Promedio: ", e["promedio"])
                    print("Activo: ", e["activo"])
            
        elif 'nombre' in entrada and 'promedio' in entrada and 'activo' in entrada:
            for e in memoria:
                ename = e["promedio"]
                if ename == atributo:
                    print('Nombre: ', e["nombre"])
                    print("Promedio: ", e["promedio"])
                    print("Activo: ", e["activo"])

        elif 'nombre' in entrada and 'edad' in entrada and 'activo' in entrada:
            for e in memoria:
                ename = e["promedio"]
                if ename == atributo:
                    print('Nombre: ', e["nombre"])
                    print("Edad: ", e["edad"])
                    print("Activo: ", e["activo"])

        elif 'nombre' in entrada and 'edad' in entrada and 'promedio' in entrada:
            for e in memoria:
                ename = e["promedio"]
                if ename == atributo:
                    print('Nombre: ', e["nombre"])
                    print("Edad: ", e["edad"])
                    print("Promedio: ", e["promedio"])

        elif entrada.startswith('SELECCIONAR promedio') in entrada and 'activo' in entrada:
            for e in memoria:
                ename = e["promedio"]
                if ename == atributo:
                    print("Promedio: ", e["promedio"])
                    print("Activo: ", e["activo"])
            
        elif 'activo' in entrada:
            for e in memoria:
                ename = e["promedio"]
                if ename == atributo:
                    print("Activo: ", e["activo"])
            
        elif 'promedio' in entrada:
            for e in memoria:
                ename = e["promedio"]
                if ename == atributo:
                    print("Promedio: ", e["promedio"])
            
        elif 'edad' in entrada:
            for e in memoria:
                ename = e["promedio"]
                if ename == atributo:
                    print("Edad: ", e["edad"])
        
    
    if 'REPORTE' in entrada:
       lis = entrada.split()
       N = 0
       N = int(lis[tamaño(lis) - 1])
       #print(N)
       datos_edades()
       datos_estados()
       datos_nombres()
       datos_promedios()

       
       with open('reporte.html', 'w') as reporte:
            reporte.write('<html>')
            reporte.write('<head>')
            reporte.write('<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/css/bootstrap.min.css">')
            reporte.write('<body>')
            reporte.write('<center>')

            reporte.write('<table class="table table-hover">')

            reporte.write('<thead>')
            reporte.write('<tr>')
            reporte.write('<th scope="col">No.</th>')
            reporte.write('<th scope="col">Nombre</th>')
            reporte.write('<th scope="col">Edad</th>')
            reporte.write('<th scope="col">Activo</th>')
            reporte.write('<th scope="col">Promedio</th>')
            reporte.write('</tr>')
            reporte.write('</thead>')

            reporte.write('<tbody>')
            for ie in range(int(N)):
                valor = str(ie)
                #print(promedios[ie])
                reporte.write('<tr>')
                reporte.write('<th>' + str(ie + 1) + '</th>')
                reporte.write('<td class="active">' + str(nombres[ie]) + '</td>')
                reporte.write('<td class="success">' + str(edades[ie]) + '</td>')
                reporte.write('<td class="warning">' + str(estados[ie]) + '</td>')
                reporte.write('<td class="danger">' + str(promedios[ie]) + '</td>')
                reporte.write('</tr>')
            reporte.write('</tbody>')

            reporte.write('</table>')
            reporte.write('</center>')
            reporte.write('</body>')
            reporte.write('</html>')

            webbrowser.open('reporte.html')
        
    if 'SALIR' in entrada:
        exit()

       