#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:       GUI, landing leveling.
#
# Author:      iacovarr
#
# Created:     05/09/2012 modify 12/01/12
# Copyright:   (c) Mario Borjas Zepeda, Irving Covarrubias Martin del Campo. 2012
# Licence:     <your licence>
#-------------------------------------------------------------------------------

#!/usr/bin/env python

import signal
import wx
import wx.lib.sheet as sheet
import binascii
import os
import time
import shutil
import sys
import xlrd
from xlrd import open_workbook
import xlwt
from xlwt import Workbook
import serial

commNumber = 4
currenttime = time.strftime('%d_%b_%Y_%Hh%Mm%Ss')
name_folder = ''
change_name = False
promedio = '9'
idx=0
altura=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
altura2=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
MatrizValue = [
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],]

# automatico=True

class MyApp(wx.App):

    def OnInit(self):
        image = wx.Image('TRACTOR5V1.jpg', wx.BITMAP_TYPE_JPEG)
        frame = MyFrame(image, "Control Laser y Posicion GPS", (80, 60), (1450, 1050))
        frame.Show()
        #self.SetTopWindow(frame)
        return True

class MyFrame(wx.Frame,wx.Dialog):    #MAIN FRAME.... Pagina principal

    def __init__(self, image, title, pos, size):
        wx.Frame.__init__(self, None, -1, title, pos, size)
        menuFile = wx.Menu()                                #objet menu file to configuraciones.
        menuBar = wx.MenuBar()
        menuBar.Append(menuFile, "&Configuraciones") #.........
        menuFile.Append(1, "&tipo de Unidades")
        menuFile.AppendSeparator()
        menuFile.Append(2, "&Preferencias")

        menuFile2 = wx.Menu()                                #objet menu file to Proyecto
        menuBar.Append(menuFile2, "&Proyecto") #.........
        menuFile2.Append(3, "&Insertar Topografia")
        menuFile2.AppendSeparator()
        menuFile2.Append(5, "&Salir")

        # menuFile3 = wx.Menu()                                #objet menu file to abrir proyecto
        # menuBar.Append(menuFile3, "&Abrir Proyecto") #.........
        # menuFile3.Append(4, "&Abrir Topografia")
        # menuFile3.AppendSeparator()
        # menuFile3.Append(5, "&Salir")

        btn1 = wx.Button(self,  6, 'Promedio Total', (25,50))
        btn2 = wx.Button(self,  7, 'Ver Datos.', (25,100))
        btn3 = wx.Button(self,  8, 'Quienes Somos', (25,150))
        btn4 = wx.Button(self,  9, 'MODO TOPOGRAFIA', (25,250))
        btn5 = wx.Button(self,  10, 'MODO NIVELACION', (25,300))
        temp = image.ConvertToBitmap()                        #with this object you converter one image to bit map
        self.bmp = wx.StaticBitmap(parent=self, bitmap=temp)#create an object static to bit map
        self.SetMenuBar(menuBar)
        self.CreateStatusBar()
        self.SetStatusText("Bienvenido a nivelar!")
        self.Bind(wx.EVT_MENU, self.tipo_unidades, id=1)
        self.Bind(wx.EVT_MENU, self.Preferencias, id=2)
        self.Bind(wx.EVT_MENU, self.nuevo_proyecto, id=3)
        #self.Bind(wx.EVT_MENU, self.abrir_proyecto, id=4)
        self.Bind(wx.EVT_MENU, self.OnQuit, id=5)
        wx.EVT_BUTTON(self, 6, self.avarage)
        wx.EVT_BUTTON(self, 7, self.VerDatos)
        wx.EVT_BUTTON(self, 9, self.topografia_mode)
        wx.EVT_BUTTON(self, 10, self.nivelacion_mode)

    def OnQuit(self, event):
        self.Close()

    def tipo_unidades(self, event):
        wx.MessageBox("This is a wxPython Hello world sample","About Hello World", wx.OK | wx.ICON_INFORMATION, self)

    def Preferencias(self, event):
        dlg = wx.PageSetupDialog(self)
        if dlg.ShowModal() == wx.ID_OK:
            data = dlg.GetPageSetupData()
            tl = data.GetMarginTopLeft()
            br = data.GetMarginBottomRight()
            self.SetStatusText('Margins are: %s %s' % (str(tl), str(br)))
        dlg.Destroy()

    def nuevo_proyecto(self, event):
        #here we call the notebook.
        frame = Notebook(None, -1, 'notebook.py')
        frame.Show(True)
        frame.Centre()
        return True
        
    def VerDatos(self, event):        ####----------------- estoy chechando el serial ---------------------####
        print "HOLA"
        serial = serial_x(commNumber)
        serial.Run_row()
        
    def topografia_mode(self,event):
        print "MODE TOPOGRAFIA"
        serial = serial_x(commNumber)
        serial.write('r')
        print(serial.read(2))

    def nivelacion_mode(self,event):
        print "MODO NIVELACION"
        serial = serial_x(commNumber)
        serial.write('N')
        # serial.write(promedio)
        print(serial.read(1))
        # serial.write('N')
        #print serial.read(4)
        
    def avarage(self,event):
        prom=0x01
        dlg = wx.TextEntryDialog(self, 'Cual es el Promedio?:','PROMEDIO')  # you display a dialog entry
        dlg.SetValue("0")
        if dlg.ShowModal() == wx.ID_OK:
            promedio=int(dlg.GetValue())
            print "PROMEDIO %i"%promedio
        dlg.Destroy()
        serial = serial_x(commNumber)
        serial.write('P')
        serial.write(promedio)
        print(serial.read(2))
        prom=serial.read(1)
        print prom

########################################################### IN THIS CLASS I CREATED THE NOTEBOOK######################################
        
class MySheet(sheet.CSheet):
    def __init__(self, parent):
        sheet.CSheet.__init__(self, parent)

        self.SetLabelBackgroundColour('#DBD4D4')
        self.SetNumberRows(50)
        self.SetNumberCols(50)

class Notebook(wx.Frame):
    def __init__(self, parent, id, title):
        wx.Frame.__init__(self, parent, id, title, size=(600, 500))
        menubar = wx.MenuBar()
        file = wx.Menu()
        file.Append(105, 'Nueva Topografia Automatica', 'x' )
        file.Append(104, 'Nueva Topografia Manual', 'x' )
        file.Append(103, 'Abrir Topografia', '' )
        file.Append(102, 'Guardar Topografia', '' )
        file.Append(101, 'Salir', '' )
        menubar.Append(file, "&Archivo")
        self.SetMenuBar(menubar)
        wx.EVT_MENU(self, 105, self.init_sheet_fill_auto)
        wx.EVT_MENU(self, 104, self.init_sheet_newtop)
        wx.EVT_MENU(self, 103, self.OnOpen)
        wx.EVT_MENU(self, 102, self.OnSave)
        wx.EVT_MENU(self, 101, self.OnQuit)
        nb = wx.Notebook(self, -1, style=wx.NB_BOTTOM)
        self.sheet1 = MySheet(nb)
        self.sheet2 = MySheet(nb)
        self.sheet3 = MySheet(nb)
        nb.AddPage(self.sheet1, "Hoja1")
        nb.AddPage(self.sheet2, "Hoja2")
        nb.AddPage(self.sheet3, "Hoja3")
        self.sheet1.SetFocus()
        self.StatusBar()
        self.init_sheet_newtop(True,False)

    def StatusBar(self):
        self.statusbar = self.CreateStatusBar()
        
    def init_sheet_newtop(self,event,x=True):
        inc1 = 0
        inc2 = 0
        while(inc1 < 3):
            inc2 = 0
            while(inc2 < 3):
                value= self.sheet1.GetCellValue(inc1,inc2)  # with this method you set a value from the sheet.
                inc2 = inc2+1
            inc1 = inc1+1
        inc1 = 0
        inc2 = 0
        # self.sheet1.SetCellValue(0,0,'0')
        while(inc1 < 50):
            inc2 = 0
            while(inc2 < 50):
                if(x==True):
                    self.sheet1.SetCellValue(inc1,inc2,'0')  # with this method you set a value from the sheet.
                else:
                    self.sheet1.SetCellValue(inc1,inc2,'x')
                inc2 = inc2+1
            inc1 = inc1+1
        if(x==True):
            dlg = wx.TextEntryDialog(self, 'Nombre del Proyecto','Escriva el Nombre')  # you display a dialog entry
            dlg.SetValue("Default")
            if dlg.ShowModal() == wx.ID_OK:
                # if (dlg.GetValue=="Default"):
                    # self.SetStatusText('Nombre del Proyecto: %s\n' % currenttime)
                # else:
                self.SetStatusText('Nombre del Proyecto: %s\n' % dlg.GetValue())
                name_folder = dlg.GetValue()
                self.name_folder = name_folder
                print name_folder
            dlg.Destroy()
         
    def OnOpen(self, event):
        print 'Abrir'      #no me borress!!!!.
        dlg = wx.FileDialog(self, "Choose a file", r"C:\SystemF\Flatland", "", "*.*", wx.OPEN)
        if dlg.ShowModal() == wx.ID_OK:
                path = dlg.GetPath()
                mypath = os.path.basename(path)
                self.SetStatusText("You selected: %s" % path)
                print path
                try:
                    create = create_files()
                    create.open_excel(r"%s"%path)
                except:
                    wx.MessageBox("Intente abrir solo los archivos .xls","ERROR! al abrir archivo", wx.OK | wx.ICON_INFORMATION, self)
        dlg.Destroy()
        inc1 = 0
        inc2 = 0
        while(inc1 < 49):
            inc2 = 0
            while(inc2 < 49):
                # value = MatrizValue[inc1][inc2]
                cell = sheet1.cell(inc1,inc2).value
                strcell = str(cell)
                self.sheet1.SetCellValue(inc1,inc2,strcell)  # with this method you set a value from the sheet.
                inc2 = inc2+1
            inc1 = inc1+1
            
    # def openfile(self, event):


    def OnSave(self, event):
        print 'Guardar'
        # self.zeros
        inc1 = 0
        inc2 = 0
        while(inc1 < 50):
            inc2 = 0
            while(inc2 < 50):
                value = self.sheet1.GetCellValue(inc1,inc2)  # with this function you get a value from the sheet.
                intvalue = int(value)
                MatrizValue[inc1][inc2] = intvalue
                inc2 = inc2+1
            inc1 = inc1+1
        try:
            if(self.name_folder=="Default"):
                create = create_files(currenttime)
            else:
                create = create_files(self.name_folder)
            create.excel_file()
            wx.MessageBox(" Archivo guardado", "Guardar", wx.OK | wx.ICON_INFORMATION, self)
        except:
            wx.MessageBox(" Cierre los archivos de Excel y vuelva a guardar", "ERROR!!", wx.OK | wx.ICON_INFORMATION, self)
            
#######-------------------------------------------------OBTENCION DE TOPOGRAFIA PARTE AUTOMATICA---------------------------------#####
            
    def init_sheet_fill_auto(self,event,x=True):
        self.init_sheet_newtop(True,True)
        print 'Abrir'      #no me borress!!!!.
        idx=0
        # MatrizValue[0][0] = 1
        automatico=True
        serial = serial_x(commNumber)
        fila=0
        numfilas=20
        # dlg = wx.TextEntryDialog(self, 'Longitud del terreno','Numero de filas?')  # you display a dialog entry
        # dlg.SetValue("1")
        # if dlg.ShowModal() == wx.ID_OK:
            # numfilas=int(dlg.GetValue())
            # print "NUM FILAS %i"%numfilas
        # dlg.Destroy()
        
        while(fila < numfilas):
            serial.Run_row()
            self.fill_matriz(fila)
            fila = fila+1
            # if fila < numfilas :
                # automatico=False
        print MatrizValue
                
        # inc1 = 0             #------------------------this part i used to fill the matriz-------------
        # inc2 = 0
        # while(inc1 < 50):
            # inc2 = 0
            # while(inc2 < 50):
                # value = MatrizValue[inc1][inc2]
                # #value = int(value)
                # #print value
                # strvalue = str(value)
                # self.sheet1.SetCellValue(inc1,inc2,strvalue)  # with this method you set a value from the sheet.
                # inc2 = inc2+1
            # inc1 = inc1+1   #-----------------------this part i used to fill the matriz-------------
                
        # self.sheet1.SetCellValue(1,1,"500") 
    
    def fill_matriz(self,fila):
        inc1=0
        der_izq = fila%2
        print der_izq
        # MatrizValue[fila][inc1] = altura2[fila][inc1]
        while(inc1<30):        #while(inc1<20):
            if (der_izq == 0):
                if(altura2[inc1]!=0):
                    MatrizValue[fila][inc1] = altura2[inc1]    #MatrizValue[fila][inc1] = altura2[inc1]
                    value = MatrizValue[fila][inc1]
                    strvalue = str(value)
                    self.sheet1.SetCellValue(fila,inc1,strvalue)
                else:
                    break
            if (der_izq != 0):
                if(altura2[inc1]!=0):
                    MatrizValue[fila][19-inc1] = altura2[19-inc1]    #MatrizValue[fila][19-inc1] = altura2[19-inc1]
                    value = MatrizValue[fila][19-inc1]
                    strvalue = str(value)
                    self.sheet1.SetCellValue(fila,19-inc1,strvalue)
                else:
                    break
            inc1 = inc1+1
            # time.sleep(0.5)
        inc1=0
            
            
    def OnQuit(self, event):
        self.Close()

############################################## CREATE FILES IN EXCEL CLASS #############################################################
class create_files():

    def __init__(self,namefolder='folder1'):
        # self.excel_file()
        self.namefolder = namefolder
        
    def check_path(self,path, folder):
        if not os.path.exists(path):
            if folder == True:
                os.mkdir(path)
            else:
                return True
            #print(path + " directory created")

        else:
            #print(path + " directory checked")
            # Excel file found.
            return False

    def excel_file(self):
        test_name = "Macro de Nivelacion"
        folder = True # Used to create folders.  
        # Check for logs directories.
        log_path = r'C:\SystemF'
        self.check_path(log_path, folder)
        log_path = r'C:\SystemF\Flatland'
        self.check_path(log_path, folder)
        # self.currenttime = time.strftime('%d_%b_%Y_%Hh%Mm%Ss')
        log_path = r"C:\SystemF\Flatland" + "\\" + self.namefolder
        self.check_path(log_path, folder)   
        try:
            wd = os.open(r"C:\SystemF\Flatland\Nivelacion_laser.xlsm", os.O_RDONLY)
            os.close(wd)
            fatal_error = True
        except:
            print("*"*50)
            print("Fatal Error, template not found on the rute" + log_path)
            fatal_error = False
        
        if fatal_error == True:
            shutil.copyfile(r"C:\SystemF\Flatland\Nivelacion_laser.xlsm",r"C:\SystemF\Flatland" + "\\" + self.namefolder + "\\" + "Nivelacion_laser.xlsm")
            wb = xlwt.Workbook()
            ws = wb.add_sheet('Sheet1')
            for i in range(49):
                for j in range(49):
                    ws.write(i, j, MatrizValue[i][j]) 
            wb.save("C:\SystemF\Flatland" + "\\" + self.namefolder + "\\" + "book.xls")         
            os.system("start excel.exe C:\SystemF\Flatland" + "\\" + self.namefolder + "\\" + "book.xls C:\SystemF\Flatland" + "\\" + self.namefolder + "\\" + "Nivelacion_laser.xlsm")
            #raw_input("Presione enter para cerrar")
        else:
            print("*"*50)
            
    def open_excel(self,path="C:\SystemF\Flatland\01_Dec_2012_15h17m37s\book.xls", sheet_name='Sheet1'):
        global sheet1
        book = open_workbook(path)
        sheet1 = book.sheet_by_name(sheet_name)
        # sheet0 = book.sheet_by_index(0)
        # sheet1 = book.sheet_by_index(1)
        # cell = sheet1.cell(0,0).value
        # print cell
        
# class calculos():
################################################### SERIAL ###############################################
    # def pendientes_naturales(self):
# mastil=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
# receptor=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    
class serial_x():

    def __init__(self,puerto=commNumber,xbaudrate = 9600):
        self.ser =  serial.Serial(puerto,9600,timeout=1)
        print self.ser.portstr
        self.ser.puerto = puerto
        self.ser.baudrate = xbaudrate # may be different

    def Run_row(self):
        # self.ser.write("r") #ask for data of the row.
        self.mastil=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        self.receptor=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        inc=0
        while(inc<20):
            self.mastil[inc] = self.ser.read(2)
            self.mastil[inc] = int(self.mastil[inc],16)
            self.receptor[inc] = self.ser.read(2)
            self.receptor[inc] = int(self.receptor[inc],16)
            self.calculo_altura(inc)
            inc=inc+1
        print self.mastil
        print self.receptor
        print altura2
            
    def calculo_altura(self,index):
        altura[index]=self.mastil[index] + ((self.receptor[index]-128)*0.1176)
        altura[index]=int(altura[index])
        altura2[index]=str(altura[index])
 
    def read(self,numdata=1):
        return self.ser.read(numdata)
          
    def write(self,data=1):
        return self.ser.write(data)
        
################################################## MAIN ###################################################
        
if __name__ == '__main__':
    # create = create_files(currenttime)
    # create.excel_file()
    app = MyApp(False)
    app.MainLoop()
    # while(1):
        # serial = serial_x(4)
        # print serial.read(1)
    #raw_input()

# def main():
    # app = MyApp(False)
    # app.MainLoop()

