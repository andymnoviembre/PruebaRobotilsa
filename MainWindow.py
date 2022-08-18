from calendar import month
import json
import sys
from PyQt5.QtGui import*
from PyQt5.QtWidgets import QApplication, QMainWindow,QPushButton, QListWidgetItem, QMenu, QDialog, QLabel
from PyQt5 import uic, QtWidgets, QtGui, QtCore
import ctypes #Obener ancho y alto del escritorio
from PyQt5.QtCore import QTimer,QTime, QEvent
from os import path
import os
from datetime import date
import time
import requests

#Creamos clase heredad de QMainWindow(Constructor de ventanas)
class Ventana(QMainWindow):
    #Metodo constructor de la clase
    def __init__(self):
        #Iniciar el objeto
        QMainWindow.__init__(self)
        #cargamos la config del arhivo .uic
        uic.loadUi("PruebaRobotilsa.ui",self)  
        
        #Para mostrar la fecha actual 
        fecha = date.today()
        self.labelFecha.setText(str(fecha.day)+"/"+str(fecha.month)+"/"+ str(fecha.year))
    
        #Para poder actualizar constamente la hora
        timer= QTimer(self)
        timer.timeout.connect(self.horaActual)
        timer.start(1000) 
        
        i=1
        self.a=0
        self.lista=[]
        self.info =[]
        self.info2=[]
        self.info3 =[]
        self.info4 =[]
        self.info5 =[]
        self.info6 =[]
        self.info7 =[]
        for i in range(11):
            self.a+=1
            resp = requests.get('https://swapi.dev/api/people/'+str(i))
            diccionario=json.loads(resp.text)
            #self.nombre=diccionario['name']
            self.lista.append(diccionario)
        #print("tamaño:",len(self.lista))
        #print("a:",self.a)
        self.pushButton.setIcon(QIcon('check.ico'))
        self.pushButton.clicked.connect(self.contador)
        self.cont = 0

        #para poner en funcionamiento el boton request
        
        self.pushButton.clicked.connect(self.mosList)
        self.listWidget.itemSelectionChanged.connect(self.itemSel)

        self.listWidget.installEventFilter(self)


    def horaActual(self): #Funcion que permite mostra la hora 
        currentTime = QTime.currentTime()
        self.labelHora.setText(currentTime.toString('hh:mm:ss'))

    def contador(self):
        self.cont+= 1
        #print("numero de clicks:" ,self.cont)
        if self.cont>0:
            self.pushButton.clicked.connect(self.borrar)
            self.pushButton.clicked.connect(self.mosList)
        
    def mosList(self):
        
        for i in range(10):
            self.listWidget.addItem(self.lista[i+1]['name'])
            self.info.append(self.lista[i+1]['height'])
            self.info2.append(self.lista[i+1]['mass'])
            self.info3.append(self.lista[i+1]['hair_color'])
            self.info4.append(self.lista[i+1]['skin_color'])
            self.info5.append(self.lista[i+1]['eye_color'])
            self.info6.append(self.lista[i+1]['birth_year'])
            self.info7.append(self.lista[i+1]['gender'])

    def borrar(self):
        self.listWidget.clear()

    def itemSel(self):
        self.item= QListWidgetItem(self.listWidget.currentItem())
        #print("nombre seleccionado:", self.item.text()) 
        if self.item.text()=="Luke Skywalker":
            self.peso = self.lista[1]['height']
            self.mass = self.lista[1]['mass']
            self.hair = self.lista[1]['hair_color']
            self.skin = self.lista[1]['skin_color']
            self.eye = self.lista[1]['eye_color']
            self.birth= self.lista[1]['birth_year']
            self.gender = self.lista[1]['gender']

        if self.item.text()=="C-3PO":
            self.peso = self.lista[2]['height']
            self.mass = self.lista[2]['mass']
            self.hair = self.lista[2]['hair_color']
            self.skin = self.lista[2]['skin_color']
            self.eye = self.lista[2]['eye_color']
            self.birth= self.lista[2]['birth_year']
            self.gender = self.lista[2]['gender']

        if self.item.text()=="R2-D2":
            self.peso = self.lista[3]['height']
            self.mass = self.lista[3]['mass']
            self.hair = self.lista[3]['hair_color']
            self.skin = self.lista[3]['skin_color']
            self.eye = self.lista[3]['eye_color']
            self.birth= self.lista[3]['birth_year']
            self.gender = self.lista[3]['gender']

        if self.item.text()=="Darth Vader":
            self.peso = self.lista[4]['height']
            self.mass = self.lista[4]['mass']
            self.hair = self.lista[4]['hair_color']
            self.skin = self.lista[4]['skin_color']
            self.eye = self.lista[4]['eye_color']
            self.birth= self.lista[4]['birth_year']
            self.gender = self.lista[4]['gender']

        if self.item.text()=="Leia Organa":
            self.peso = self.lista[5]['height']
            self.mass = self.lista[5]['mass']
            self.hair = self.lista[5]['hair_color']
            self.skin = self.lista[5]['skin_color']
            self.eye = self.lista[5]['eye_color']
            self.birth= self.lista[5]['birth_year']
            self.gender = self.lista[5]['gender']

        if self.item.text()=="Owen Lars":
            self.peso = self.lista[6]['height']
            self.mass = self.lista[6]['mass']
            self.hair = self.lista[6]['hair_color']
            self.skin = self.lista[6]['skin_color']
            self.eye = self.lista[6]['eye_color']
            self.birth= self.lista[6]['birth_year']
            self.gender = self.lista[6]['gender']

        if self.item.text()=="Beru Whitesun lars":
            self.peso = self.lista[7]['height']
            self.mass = self.lista[7]['mass']
            self.hair = self.lista[7]['hair_color']
            self.skin = self.lista[7]['skin_color']
            self.eye = self.lista[7]['eye_color']
            self.birth= self.lista[7]['birth_year']
            self.gender = self.lista[7]['gender']

        if self.item.text()=="R5-D4":
            self.peso = self.lista[8]['height']
            self.mass = self.lista[8]['mass']
            self.hair = self.lista[8]['hair_color']
            self.skin = self.lista[8]['skin_color']
            self.eye = self.lista[8]['eye_color']
            self.birth= self.lista[8]['birth_year']
            self.gender = self.lista[8]['gender']

        if self.item.text()=="Biggs Darklighter":
            self.peso = self.lista[9]['height']
            self.mass = self.lista[9]['mass']
            self.hair = self.lista[9]['hair_color']
            self.skin = self.lista[9]['skin_color']
            self.eye = self.lista[9]['eye_color']
            self.birth= self.lista[9]['birth_year']
            self.gender = self.lista[9]['gender']
        
        if self.item.text()=="Obi-Wan Kenobi":
            self.peso = self.lista[10]['height']
            self.mass = self.lista[10]['mass']
            self.hair = self.lista[10]['hair_color']
            self.skin = self.lista[10]['skin_color']
            self.eye = self.lista[10]['eye_color']
            self.birth= self.lista[10]['birth_year']
            self.gender = self.lista[10]['gender']

        self.listWidget.setDropIndicatorShown(True)
        self.value = self.listWidget.dropIndicatorPosition()
        

    def eventFilter(self, source, event):
        if event.type()==QEvent.ContextMenu and source is self.listWidget:
            self.Menu = QMenu()
            self.Menu.addAction("Informacion del personaje")
            
            if self.Menu.exec_(event.globalPos()):
                item1 = source.itemAt(event.pos())
                print("Personaje seleccionado:   ",item1.text())
                print("Informacion del personaje:")
                print("Height:      ",self.peso)
                print("mass:        ",self.mass)
                print("hair_color:  ",self.hair)
                print("skin_color:  ",self.skin)
                print("eye_color:   ",self.eye)
                print("birth_year:  ",self.birth)
                print("gender:      ",self.gender)

            #print("valor:",self.value)

            return True
    
        return super().eventFilter(source, event)
        

    #Instancia para iniciar una app
app = QApplication(sys.argv)
    #Crear un objeto de la clase 
_ventana = Ventana()
    #Mostrar la ventana
_ventana.show()
   #Ejectuamos la app
sys.exit(app.exec())
