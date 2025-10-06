try:
    archivo = open('prueba.txt','w',encoding='utf-8')
    archivo.write('agregamos información al archivo \n')
    archivo.write('Adios')
except Exception as e:
    print(e)
finally:
    archivo.close()
    print('fin del archivo')
