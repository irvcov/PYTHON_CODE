#!/usr/bin/env python

import fingerprint
import requests

class checkEmployee():
    """
    #Add new Finger
    sens.collect_fing() #put finger
    sens.generate_char_file(0x1)
    sens.collect_fing()
    sens.generate_char_file(0x2)
    sens.generate_template()
    sens.store_template(1,1)

    #Check Finger if exists
    sens.collect_fing()
    sens.generate_char_file(0x1)
    sens.search_finger(1,0,255)
    """
    
    def __init__(self, divece_address=0xFFFFFFFF, uart_port=0):
        self.sens = fingerprint.FingSens(divece_address,uart_port)
        self.sens.handshake()
        
    def signInEmployee(self, idEmployee):
        raw_input("Coloque su dedo en el lector y de click!")
        self.sens.collect_fing()
        self.sens.generate_char_file(0x1)
        raw_input("Coloque su dedo en el lector para confirmar y de click!")
        self.sens.collect_fing()
        self.sens.generate_char_file(0x2)
        self.sens.generate_template()
        self.sens.store_template(1,idEmployee)
        print "Listo!"
        
    def checkIfExists(self):
        raw_input("Coloque su dedo en el lector y de click!")
        self.sens.collect_fing()
        self.sens.generate_char_file(0x1)
        r, code = self.sens.search_finger(1,0,255)
        
        if r:
            code = code.encode('hex')
            payload = {'name':code}

            print payload
            res = requests.post('http://www.irvsoft.com.mx/scanner_employee/templates/update_text_finger.php', data=payload)
            print res.text 
        else:
            print "No registrado"
        
if __name__ == "__main__":

    chk = checkEmployee()

    print "\n\n **** Bienbenido al Firmware del Lector de huella digital *****\n"
    print "\n\n Que opcion desea hacer? \n"
    print " 1- ciclar lectura de huella digital? "
    print " 2- Registrar nuevo Usuario "
    print " 3- Registrar Entrada de Usuario "
    print " 4- Salir"
    
    while True:
        
        print "\n\n **** Bienbenido al Firmware del Lector de huella digital *****\n"
        print "\n\n Que opcion desea hacer? \n"
        print " 1- ciclar lectura de huella digital? "
        print " 2- Registrar nuevo Usuario "
        print " 3- Registrar Entrada de Usuario "
        print " 4- Salir\n\n"
        input = raw_input("")
        
        if input == '1':
            print "Para salir presiones cualquier tecla"
            while True:
                #if raw_input() == None:
                chk.checkIfExists()
                    
        elif input == '2':
            print "Registrar Usuario"
            id = raw_input("Cual es el Id del Usuario (1 - 255)")
            chk.signInEmployee(int(id))
            
        elif input == '3':
            chk.checkIfExists()
            
        else:
            break
        
            
        
    
   
    
        
        