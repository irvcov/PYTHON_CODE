
# import signal
import wx
# import wx.lib.sheet as sheet
# import binascii
import os
import time
import shutil
import sys
import serial
import PROYECTO_FINAL_MD.excel_class as exc

# pathweek = ""

class MyApp(wx.App):

    def OnInit(self):
        # image = wx.Image('TRACTOR5V1.jpeg', wx.BITMAP_TYPE_JPEG)
        frame = MyFrame("Sistema Administrativo de Personal", (80, 60), (1450, 1050))
        frame.Show()
        return True
        
class MyFrame(wx.Frame,wx.Dialog):    #MAIN FRAME.... Pagina principal

    def __init__(self, title, pos, size):
        wx.Frame.__init__(self, None, -1, title, pos, size)
        menuFile = wx.Menu()                                #objet menu file to configuraciones.
        menuBar = wx.MenuBar()
        menuBar.Append(menuFile, "&Configuraciones") #.........
        menuFile.Append(10, "&Cambiar Confirugaciones")
        menuFile.AppendSeparator()
        # menuFile.Append(2, "&Ver Archivo Semanal")
        menuFile2 = wx.Menu()                                #objet menu file to Proyecto
        menuBar.Append(menuFile2, "&Archivo") #.........
        menuFile2.Append(1, "&Guardar Archivo")
        menuFile2.AppendSeparator()
        menuFile2.Append(2, "&Ver Archivo Semanal")
        menuFile2.AppendSeparator()
        menuFile2.Append(3, "&Selecciona Semana")
        menuFile2.AppendSeparator()
        menuFile2.Append(5, "&Salir")

        btn1 = wx.Button(self,  6, '** Crear Archivo Semanal ***', (25,50))
        btn2 = wx.Button(self,  7, '** Agregar Persona ********', (25,100))
        btn3 = wx.Button(self,  8, '** Chequeo de Entrada ******', (25,150))
        btn4 = wx.Button(self,  9, '** Chequeo de Salida ******', (25,200))
        # btn5 = wx.Button(self,  10, ' ** Archivo Semanal *******', (25,300))
        
        image = wx.Image('arrollo.jpg', wx.BITMAP_TYPE_JPEG)
        temp = image.ConvertToBitmap()                        #with this object you converter one image to bit map
        self.bmp = wx.StaticBitmap(parent=self, bitmap=temp)#create an object static to bit map
        
        self.SetMenuBar(menuBar)
        self.CreateStatusBar()
        self.SetStatusText("Bienvenido a nivelar!")
        self.Bind(wx.EVT_MENU, self.save_file, id=1)
        self.Bind(wx.EVT_MENU, self.see_week_file, id=2)
        self.Bind(wx.EVT_MENU, self.select_week, id=3)
        #self.Bind(wx.EVT_MENU, self.abrir_proyecto, id=4)
        self.Bind(wx.EVT_MENU, self.OnQuit, id=5)
        wx.EVT_BUTTON(self, 6, self.make_week_file)
        wx.EVT_BUTTON(self, 7, self.add_person)
        wx.EVT_BUTTON(self, 8, self.Time_check_in)
        wx.EVT_BUTTON(self, 9, self.Time_check_out)
        wx.EVT_BUTTON(self, 10, self.change_config)
        
    def save_file(self,event):
        pass
        
    def see_week_file(self,event):
        try:
            mf = manage_files()
            mf.open_excel(pathweek)
        except:
            print "No se a seleccionado o abierto ningun archivo semanal"
        
    def select_week(self,event,path=None):
        global pathweek
        if path == None:
            dlg = wx.FileDialog(self, "Choose a folder", r"C:\SystemSAP\personal", "", "*.*", wx.OPEN)
            if dlg.ShowModal() == wx.ID_OK:
                pathweek = dlg.GetPath()
                mypathweek = os.path.basename(pathweek)
            dlg.Destroy()
        else:
            pathweek=path
        print pathweek
        # print pathweek
        # mf = manage_files()
        # dlg = wx.TextEntryDialog(self, 'Semana de trabajo','Elija semana de trabajo?')  # you display a dialog entry
        # dlg.SetValue("Semana0")
        # if dlg.ShowModal() == wx.ID_OK:
            # pathweek = dlg.GetValue()
            # print pathweek
        # dlg.Destroy()
        
    def OnQuit(self,event):
        self.Destroy()
        
    def make_week_file(self,event):
        dlg = wx.TextEntryDialog(self, 'Numbre de la Carpeta','Nombre de la carpeta semanal?')  # you display a dialog entry
        dlg.SetValue("Semana0")
        if dlg.ShowModal() == wx.ID_OK:
            nameFolder = dlg.GetValue()
            print nameFolder
        dlg.Destroy()
        nameFolder = nameFolder + "_" + time.strftime('%d_%b_%Y')
        self.mf = manage_files(nameFolder)
        self.mf.copy_excel_file()
        pathweek = "C:\SystemSAP\personal\\" + nameFolder + "\\Administracion_DELpersonal.xls"
        self.select_week(event,path=pathweek)
        
    def add_person(self,event):
        mf = manage_files()
        dlg = wx.TextEntryDialog(self, 'Agregar Personal','Cual es el nombre de la Persona?')  # you display a dialog entry
        dlg.SetValue("")
        if dlg.ShowModal() == wx.ID_OK:
            nombrePersona = dlg.GetValue()
            print nombrePersona
        dlg.Destroy()
        dlg = wx.TextEntryDialog(self, 'Agregar Numero de Identificacion','Cual es el numero de ID?')  # you display a dialog entry
        dlg.SetValue("0")
        if dlg.ShowModal() == wx.ID_OK:
            IDnum = dlg.GetValue()
            print IDnum
        dlg.Destroy()
        mf.add_personal(nombrePersona,IDnum)
        
    def Time_check_in(self,event):
        dlg = wx.TextEntryDialog(self, 'Cual es el nombre de la Persona?','Hora de Entrada Personal')  # you display a dialog entry
        dlg.SetValue("")
        if dlg.ShowModal() == wx.ID_OK:
            nombrePersona = dlg.GetValue()
            print nombrePersona
        dlg.Destroy()
        dlg = wx.TextEntryDialog(self, 'Cual es el numero de ID?','Hora de Entrada Personal')  # you display a dialog entry
        dlg.SetValue("0")
        if dlg.ShowModal() == wx.ID_OK:
            IDnum = dlg.GetValue()
            print IDnum
        dlg.Destroy()
        mf = manage_files()
        print pathweek
        mf.find_personal_timein(nombrePersona,IDnum,pathweek) 
        
    def Time_check_out(self,event):
        dlg = wx.TextEntryDialog(self, 'Cual es el nombre de la Persona?','Hora de Entrada Personal')  # you display a dialog entry
        dlg.SetValue("")
        if dlg.ShowModal() == wx.ID_OK:
            nombrePersona = dlg.GetValue()
            print nombrePersona
        dlg.Destroy()
        dlg = wx.TextEntryDialog(self, 'Cual es el numero de ID?','Hora de Salida Personal')  # you display a dialog entry
        dlg.SetValue("0")
        if dlg.ShowModal() == wx.ID_OK:
            IDnum = dlg.GetValue()
            print IDnum
        dlg.Destroy()
        mf = manage_files()
        print pathweek
        mf.find_personal_timeout(nombrePersona,IDnum,pathweek)
        
    def change_config(self,event):
        pass
        
    
############################################## CREATE FILES IN EXCEL CLASS #############################################################
class manage_files():

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

    def copy_excel_file(self):
        test_name = "Sistema Administrativo de Personal"
        folder = True # Used to create folders.  
        # Check for logs directories.
        log_path = r'C:\SystemSAP'
        self.check_path(log_path, folder)
        log_path = r'C:\SystemSAP\personal'
        self.check_path(log_path, folder)
        # self.currenttime = time.strftime('%d_%b_%Y_%Hh%Mm%Ss')
        log_path = r"C:\SystemSAP\personal" + "\\" + self.namefolder
        self.check_path(log_path, folder)   
        try:
            wd = os.open(r"C:\SystemSAP\personal\Personal_template.xlsx", os.O_RDONLY)
            os.close(wd)
            fatal_error = True
        except:
            print("*"*50)
            print("Fatal Error, template not found on the rute" + r"C:\SystemSAP\personal\Personal_template.xlsx")
            fatal_error = False
        
        if fatal_error == True:
            shutil.copyfile(r"C:\SystemSAP\personal\Personal_template.xlsx",r"C:\SystemSAP\personal" + "\\" + self.namefolder + "\\" + "Administracion_DELpersonal.xls")
        else:
            print("*"*50)
            
    def add_personal(self, NombrePersona=None, IDnum=None, path = "C:\SystemSAP\personal\Personal_template.xlsx", sheet='Sheet1'):
        excel = exc.Excel(r"%s"%path)
        row = 0
        totalpersons = 50
        for row in range(3,totalpersons,1): 
            if (excel.get_cell(sheet,row,2) == None):
                excel.set_cell(sheet,row,2,NombrePersona)
                excel.set_cell(sheet,row,3,IDnum)
                break
        excel.save()
            
    def find_personal_timein(self, nombre=None, IDnum=None, path=None, sheet='Sheet1'):
        if path == None :
            path = "C:\SystemSAP\personal" + "\\" + self.namefolder + "\\" + "Administracion_DELpersonal.xls"
        else:
            path=path
        print path
        excel = exc.Excel(r"%s"%path)
        currenttime = time.strftime('%d_%b_%Y_%Hh%Mm%Ss')
        justone = False
        row = 0 
        col = 0
        totalcol = 17
        totalpersons = 50
        for row in range(3,totalpersons,1): 
            if (excel.get_cell(sheet, row, 2) is not None):
                if (excel.get_cell(sheet, row, 2) == nombre):
                    justone = False
                    for col in range(4,totalcol,2):
                        # print col
                        if (excel.get_cell(sheet,row,col) == None and justone == False):
                            excel.set_cell(sheet, row, col, currenttime)
                            justone = True
                            # pass
                    pass
                elif (excel.get_cell(sheet, row, 3) == IDnum ):
                    justone = False
                    for col in range(4,totalcol,2):
                        if (excel.get_cell(sheet,row,col) == None and justone == False):
                            excel.set_cell(sheet, row, col, currenttime)
                            justone = True
                    pass
                else:
                    pass
        excel.save()
        excel.show()
        
    def find_personal_timeout(self, nombre=None, IDnum=None, path=None, sheet='Sheet1'):
        if path == None :
            path = "C:\SystemSAP\personal" + "\\" + self.namefolder + "\\" + "Administracion_DELpersonal.xls"
        else:
            path=path
        print path
        excel = exc.Excel(r"%s"%path)
        currenttime = time.strftime('%d_%b_%Y_%Hh%Mm%Ss')
        justone = False
        row = 0 
        col = 0
        totalcol = 18
        totalpersons = 50
        for row in range(3,totalpersons,1): 
            if (excel.get_cell(sheet, row, 2) is not None):
                if (excel.get_cell(sheet, row, 2) == nombre):
                    justone = False
                    for col in range(5,totalcol,2):
                        # print col
                        if (excel.get_cell(sheet,row,col) == None and justone == False):
                            excel.set_cell(sheet, row, col, currenttime)
                            justone = True
                            # pass
                    pass
                elif (excel.get_cell(sheet, row, 3) == IDnum ):
                    justone = False
                    for col in range(5,totalcol,2):
                        if (excel.get_cell(sheet,row,col) == None and justone == False):
                            excel.set_cell(sheet, row, col, currenttime)
                            justone = True
                    pass
                else:
                    pass
        excel.save()
        excel.show()
                
    def open_excel(self,path=None, sheet_name='Sheet1'):
        if path == None :
            path = "C:\SystemSAP\personal" + "\\" + "Personal_template.xlsx"
        else:
            path=path
        excel = exc.Excel(r"%s"%path)
        excel.show()
    
    def open_excel_file(self):
        os.system("start excel.exe C:\SystemSAP\personal" + "\\" + self.namefolder + "\\" + "Administracion_DELpersonal.xls")
        
# class calculos():
################################################### SERIAL ###############################################
    # def pendientes_naturales(self):
# mastil=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
# receptor=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    
# class serial_x():

    # def __init__(self,puerto=commNumber,xbaudrate = 9600):
        # self.ser =  serial.Serial(puerto,9600,timeout=1)
        # print self.ser.portstr
        # self.ser.puerto = puerto
        # self.ser.baudrate = xbaudrate # may be different

    # def Run_row(self):
        # #self.ser.write("r") #ask for data of the row.
        # self.mastil=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        # self.receptor=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        # inc=0
        # while(inc<20):
            # self.mastil[inc] = self.ser.read(2)
            # self.mastil[inc] = int(self.mastil[inc],16)
            # self.receptor[inc] = self.ser.read(2)
            # self.receptor[inc] = int(self.receptor[inc],16)
            # self.calculo_altura(inc)
            # inc=inc+1
        # print self.mastil
        # print self.receptor
        # print altura2
            
    # def calculo_altura(self,index):
        # altura[index]=self.mastil[index] + ((self.receptor[index]-128)*0.1176)
        # altura[index]=int(altura[index])
        # altura2[index]=str(altura[index])
 
    # def read(self,numdata=1):
        # return self.ser.read(numdata)
          
    # def write(self,data=1):
        # return self.ser.write(data)
        
        
if __name__ == '__main__':
    # create = create_files(currenttime)
    # create.excel_file()
    app = MyApp(False)
    app.MainLoop()
 
def main(): 
    app = MyApp(False)
    app.MainLoop()




