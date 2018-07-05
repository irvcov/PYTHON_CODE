#!/usr/bin/python
import string   as _string
import sys      as _sys
import os       as _os

usage = """
    --------------------------------------------------------
    Este script puede convertir codigo ASM del Mips
    a un valor hexadecimal o binario, y soporta las
    siguientes instrucciones:
     - TIPO R:
        add, sub, and, xor, srl, sll
     - TIPO I
        addi, lw, sw, beq
     - TIPO J
        j
    El codigo debe estar ecrito bajo las siguientes
    reglas:
    TAGS: deben ir antes  de un  bloque de codigo y 
          seguidas de ":".
        main:
             addi $t0, $zero, 0x0F
             lw   $t1, 0($t0)
    REG: se deben escribir  despues del  signo "$" y 
         se pueden usar los nombres de los registros
         o numeros de los registros,  en el caso  de 
         lw y sw se debe  escribir primero el  offset 
         en decimal y luego entre parentesis el reg.
         main: 
             lw   $t1, 50($t0)
             sw   $s2, 0($t3)
    NOTA: 1.- Para cero utiliza el registro $zero, y 
          para valores de constantes utiliza formato 
          hex.
          2.- despues de cada palabra debe a ver un
          espacion: $t0, $t1
          3.- el script tiene un bug, se come la primer 
          linea  del archivo  asm, el  workaround  es
          comenzar a escribir en la segunda linea.
    
    CODIGO DE EJEMPLO:
        main:
            addi $t0, $zero, 32         # comments
            addi $t1, $zero, 0x0F       # comments
        L1: 
            and  $s0, $t2, $30          # comments
            srl  $s1, $30, 31           # comments
            beq  $s1, $t1, CASE         # comments
            j    L1                     # comments
            
    Contacto: irrealex@hotmail.com
    --------------------------------------------------------
"""

out_file = r"MyCode.txt"
file_bin = open(out_file, 'w')
dic_tags = {}
counter_line = 0
counter  = 1    
debug = True
format_to_file = 0
dic_i_type = {"addi":8 , "sw":43, "lw":35}
dic_r_type = {"add":32 , "sub":34, "and":36, "xor":38, "srl":2, "sll":0}
list_inst  = ["add", "sub", "and", "xor", "srl", "sll", "addi", "sw", "lw", "beq", "j"]
dic_reg = {
           "zero":0, "r0":0,  "at":1,  "v0":2,  "v1":3,  "a0":4,  "a1":5,  "a2":6, "a3":7, 
           "t0":8,   "t1":9,  "t2":10, "t3":11, "t4":12, "t5":13, "t6":14, "t7":15, 
           "s0":16,  "s1":17, "s2":18, "s3":19, "s4":20, "s5":21, "s6":22, "s7":23, 
           "t8":24,  "t9":25, "k0":26, "k1":27, "gp":28, "sp":29, "s8":30, "ra":31
          }
r_type = {"OPCODE": 0x0,
          "RS": 0X0,
          "RT": 0X0,
          "RD": 0X0,
          "SHAMT": 0X0,
          "FUNCT": 0X0
          }
i_type = {"OPCODE": 0x0,
          "RS": 0X0,
          "RT": 0X0,          
          "ADDRESS": 0x00
          }           
j_type = {"OPCODE": 0x0,         
          "ADDRESS": 0x00
          }  
          
def ASMMips(file_name):
    global counter_line
    
    with open(file_name) as file_asm:
        try:
            header = next(file_asm)
        except StopIteration as e:
            print "File is empty"
        for line in file_asm:                       
            pos = line.find("#")
            new_line = line[:pos]
            findTags( new_line )
    
    counter_line = 0
    with open(file_name) as file_asm:
        try:
            header = next(file_asm)
        except StopIteration as e:
            print "File is empty"
        for line in file_asm:
            pos = line.find("#")
            new_line = line[:pos]
            decode(new_line)
    
        
def findTags( line ):
    global counter_line
    global counter
    counter += 1
    is_tag = line.find(":")
    if(is_tag != -1):
        dic_tags[line[:is_tag]] = counter_line
    else:
        words = _string.split(line)        
        if( len(words) > 1 ):
            w_lower = words[0].lower()
            if( w_lower ==  list_inst[0] or w_lower ==  list_inst[1] or w_lower ==  list_inst[2] or w_lower ==  list_inst[3]):                
                counter_line += 1
            elif( w_lower ==  list_inst[4] or w_lower ==  list_inst[5] ):                
                counter_line += 1
            elif( w_lower ==  list_inst[6] or w_lower ==  list_inst[7] or w_lower ==  list_inst[8]):
                counter_line += 1
            elif( w_lower ==  list_inst[9] ):
                counter_line += 1
            elif( w_lower ==  list_inst[10] ):
                counter_line += 1
            else:
                w_lower = words[1].lower()
                if ( w_lower[0] == "$"):
                    print "bad instruction:" + line + "  LINE: " + str(counter) 
                    raw_input('Press "Enter" to close windows :( ')
                    _sys.exit(0)
        
def decode( line ):
    global counter_line
    is_tag = line.find(":")
    if(is_tag != -1):
        print ' '*26 + line[:is_tag]
    else:
        words = _string.split(line)        
        if( len(words) > 1 ):
            w_lower = words[0].lower()
            if( w_lower ==  list_inst[0] or w_lower ==  list_inst[1] or w_lower ==  list_inst[2] or w_lower ==  list_inst[3]):
                decodeRType(words, counter_line, line)
                counter_line += 1
            elif( w_lower ==  list_inst[4] or w_lower ==  list_inst[5] ):
                decodeRType_s(words, counter_line, line)
                counter_line += 1
            elif( w_lower ==  list_inst[6] or w_lower ==  list_inst[7] or w_lower ==  list_inst[8]):
                decodeIType(words, counter_line, line)
                counter_line += 1
            elif( w_lower ==  list_inst[9] ):
                decodeBranch(words, counter_line, line)
                counter_line += 1
            elif( w_lower ==  list_inst[10] ):
                decodeJump(words, counter_line, line)    
                counter_line += 1
            else:
                w_lower = words[1].lower()
                if ( w_lower[0] == "$"):
                    print "bad instruction: " + line
                    
def decodeRType(words, line_num, line):
    """
        Syntax              operation
        add $d, $s, $t      $d = $s + $t
        sub $d, $s, $t      $d = $s + $t
        and $d, $s, $t      $d = $s + $t
        xor $d, $s, $t      $d = $s + $t
    """

    RS = 0
    RT = 0
    RD = 0
    SHAMT = 0
    FUNCT = 0
    if( verifySymbol(words[1]) ):
        if( dic_reg.has_key(words[1][1:-1]) ):
            RD = dic_reg[ words[1][1:-1] ]
        else:
            try: RD = int( words[1][1:-1] )
            except: print "bad instruction: " + line
    if( verifySymbol(words[2]) ):
        if( dic_reg.has_key(words[2][1:-1]) ):
            RS = dic_reg[ words[2][1:-1] ]
        else:
            try: RS = int( words[2][1:-1] )
            except: print "bad instruction: " + line
    if( verifySymbol(words[3]) ):
        if( dic_reg.has_key(words[3][1:]) ):
            RT = dic_reg[ words[3][1:] ]
        else:
            try: RT = int( words[3][1:] )
            except: print "bad instruction: " + line

    r_type["OPCODE"] = 0
    r_type["RS"] = RS
    r_type["RT"] = RT
    r_type["RD"] = RD
    r_type["SHAMT"] = SHAMT
    r_type["FUNCT"] = dic_r_type[ words[0] ]
    hex_mif = 0x00000000
    hex_mif = r_type["OPCODE"]
    hex_mif = hex_mif | (RS << 21)
    hex_mif = hex_mif | (RT << 16)
    hex_mif = hex_mif | (RD << 11)
    hex_mif = hex_mif | (SHAMT << 6 )
    hex_mif = hex_mif |  dic_r_type[ words[0] ]
    if(debug):
        print '0x{0:08X}'.format(line_num), "   ", '0x{0:08X}'.format(hex_mif), "  ", line
        
    op_b   = str( bin( r_type["OPCODE"] ))[2:].zfill(6)
    rs_b   = str( bin( r_type["RS"] ))[2:].zfill(5)
    rt_b   = str( bin( r_type["RT"] ))[2:].zfill(5)
    rd_b   = str( bin( r_type["RD"] ))[2:].zfill(5)
    shamt   = str( bin( r_type["SHAMT"] ))[2:].zfill(5)
    funct = str( bin( r_type["FUNCT"] ))[2:].zfill(6)
    bin_mif = op_b + rs_b + rt_b + rd_b + shamt + funct
    if(debug):   
        if( format_to_file ):
            file_bin.write(str('{0:08X}'.format(hex_mif)))
        else:
            file_bin.write(bin_mif)
        file_bin.write('\n')        
    
def decodeRType_s(words, line_num, line):
    """
        Syntax                  operation
        sll $d, $t, amount      $d = $t << amount
        srl $d, $t, amount      $d = $t >> amount
    """
    RS = 0
    RT = 0
    RD = 0
    SHAMT = 0
    FUNCT = 0

    if( verifySymbol(words[1]) ):       
        if( dic_reg.has_key(words[1][1:-1]) ):
            RD = dic_reg[ words[1][1:-1] ]
        else:
            try: RD = int( words[1][1:-1] )
            except: print "bad instruction: " + line
    if( verifySymbol(words[2]) ):
        if( dic_reg.has_key(words[2][1:-1]) ):
            RT = dic_reg[ words[2][1:-1] ]
        else:
            try: RT = int( words[2][1:-1] ) 
            except: print "bad instruction: " + line                
        try: SHAMT = int( words[3] ) 
        except: print "bad instruction: " + line
        
    r_type["OPCODE"] = 0
    r_type["RS"] = RS
    r_type["RT"] = RT
    r_type["RD"] = RD
    r_type["SHAMT"] = SHAMT
    r_type["FUNCT"] = dic_r_type[ words[0] ]
    hex_mif = 0x00000000
    hex_mif = r_type["OPCODE"] << 26
    hex_mif = hex_mif | (r_type["RS"] << 21)
    hex_mif = hex_mif | (r_type["RT"] << 16)
    hex_mif = hex_mif | (r_type["RD"] << 11)
    hex_mif = hex_mif | (r_type["SHAMT"] << 6 )
    hex_mif = hex_mif | r_type["FUNCT"]
    if(debug):
        print '0x{0:08X}'.format(line_num), "   ", '0x{0:08X}'.format(hex_mif), "  ", line
    
    op_b   = str( bin( r_type["OPCODE"] ))[2:].zfill(6)
    rs_b   = str( bin( r_type["RS"] ))[2:].zfill(5)
    rt_b   = str( bin( r_type["RT"] ))[2:].zfill(5)
    rd_b   = str( bin( r_type["RD"] ))[2:].zfill(5)
    shamt   = str( bin( r_type["SHAMT"] ))[2:].zfill(5)
    funct = str( bin( r_type["FUNCT"] ))[2:].zfill(6)
    bin_mif = op_b + rs_b + rt_b + rd_b + shamt + funct
    if(debug):   
        if( format_to_file ):
            file_bin.write(str('{0:08X}'.format(hex_mif)))
        else:
            file_bin.write(bin_mif)
        file_bin.write('\n')       
        
def decodeIType(words, line_num, line):
    """
        Syntax                  operation
        addi $t, $s, address    $t = $s + address; advance PC 4
        lw   $t, offset($s)     $t = MEM[$s + offset]; advance PC 4
        sw   $t, offset($s)     MEM[$s + offset] = $t; advance PC 4
    """
    RS = 0
    RT = 0
    ADDRESS = 0
    if( verifySymbol(words[1]) ):
        if( dic_reg.has_key(words[1][1:-1]) ):
            RT = dic_reg[ words[1][1:-1] ]
        else:
            try: RT = int( words[1][1:-1] )
            except: print "bad instruction: " + line                                       
    if( list_inst[6] == words[0] ):
        if( verifySymbol(words[2]) ):
            if( dic_reg.has_key(words[2][1:-1]) ):
                RS = dic_reg[ words[2][1:-1] ]
            else:
                try: RS = int( words[2][1:-1] )
                except: print "bad instruction: " + line
            try: ADDRESS = int( words[3] ) 
            except: ADDRESS = int( words[3], 16)    
    
    else:
        sym1 = words[2].find( "(" )
        sym2 = words[2].find( ")" )
        reg = words[2][sym1+1:sym2]
        if( verifySymbol( reg ) ):
            if( dic_reg.has_key( reg[1:] ) ):
                RS = dic_reg[ reg[1:] ]
            else:
                try: RS = int( reg[1:] )                    
                except: print "bad instruction: " + line            
            try: ADDRESS = int( words[2][:sym1] )
            except: print "bad instruction: " + line 
            
    i_type["OPCODE"]  = dic_i_type[ words[0] ]
    i_type["RS"]      = RS
    i_type["RT"]      = RT
    i_type["ADDRESS"] = ADDRESS
    hex_mif = 0x00000000
    hex_mif = i_type["OPCODE"] << 26
    hex_mif = hex_mif | (i_type["RS"] << 21)
    hex_mif = hex_mif | (i_type["RT"] << 16)
    hex_mif = hex_mif |  i_type["ADDRESS"]
    
    if(debug):
        print '0x{0:08X}'.format(line_num), "   ", '0x{0:08X}'.format(hex_mif), "  ", line
        
    op_b   = str( bin( i_type["OPCODE"] ))[2:].zfill(6)
    rs_b   = str( bin( i_type["RS"] ))[2:].zfill(5)
    rt_b   = str( bin( i_type["RT"] ))[2:].zfill(5)
    addr_b = str( bin( i_type["ADDRESS"] ))[2:].zfill(16)
    bin_mif = op_b + rs_b + rt_b + addr_b      
    if(debug):   
        if( format_to_file ):
            file_bin.write(str('{0:08X}'.format(hex_mif)))
        else:
            file_bin.write(bin_mif)
        file_bin.write('\n') 

def decodeBranch(words, line_num, line):
    """
        Syntax                  operation
        beq $s, $t, offset      if   $s == $t: advance_pc(offset << 2)); 
                                else: advance_pc (4);
    """    
    RS = 0
    RT = 0
    ADDRESS = 0
    if( verifySymbol(words[1]) ):
        if( dic_reg.has_key(words[1][1:-1]) ):
            RS = dic_reg[ words[1][1:-1] ]
        else:
            try: RS = int( words[1][1:-1] )
            except: print "bad instruction: " + line
    if( verifySymbol(words[2]) ):
        if( dic_reg.has_key(words[2][1:-1]) ):
            RT = dic_reg[ words[2][1:-1] ]
        else:
            try: RT = int( words[2][1:-1] )                
            except: print "bad instruction: " + line    
    if( dic_tags.has_key(words[3]) ):
        if( line_num > dic_tags[words[3]] ):
            ADDRESS = int(str(( (dic_tags[words[3]]- line_num-1) ^ 0xffff) +1)[1:])
        else:
            ADDRESS = dic_tags[words[3]] - line_num-1
    else:
        print "Invalid TAG: " + line  
    
    i_type["OPCODE"]  = 4
    i_type["RS"]      = RS
    i_type["RT"]      = RT
    i_type["ADDRESS"] = ADDRESS
    hex_mif = 0x00000000
    hex_mif = i_type["OPCODE"] << 26
    hex_mif = hex_mif | (i_type["RS"] << 21)
    hex_mif = hex_mif | (i_type["RT"] << 16)
    hex_mif = hex_mif |  i_type["ADDRESS"]
    if(debug):
        print '0x{0:08X}'.format(line_num), "   ", '0x{0:08X}'.format(hex_mif), "  ", line
    
    op_b   = str( bin( i_type["OPCODE"] ))[2:].zfill(6)
    rs_b   = str( bin( i_type["RS"] ))[2:].zfill(5)
    rt_b   = str( bin( i_type["RT"] ))[2:].zfill(5)
    addr_b = str( bin( i_type["ADDRESS"] ))[2:].zfill(16)
    bin_mif = op_b + rs_b + rt_b + addr_b      
    if(debug):   
        if( format_to_file ):
            file_bin.write(str('{0:08X}'.format(hex_mif)))
        else:
            file_bin.write(bin_mif)
        file_bin.write('\n') 
    
def decodeJump(words, line_num, line):
    """
        Syntax                  operation
        j address               PC = (PC & 0xf0000000) | (address << 2);
    """   
    ADDRESS = 0
    if( dic_tags.has_key(words[1]) ):
        ADDRESS = dic_tags[words[1]]
    else:
        print "Invalid TAG: " + line 
    j_type["OPCODE"]  = 2
    j_type["ADDRESS"] = ADDRESS
    hex_mif = 0x00000000
    hex_mif = j_type["OPCODE"] << 26
    hex_mif = hex_mif |  j_type["ADDRESS"]
    if(debug):
        print '0x{0:08X}'.format(line_num), "   ", '0x{0:08X}'.format(hex_mif), "  ", line

    op_b   = str( bin( j_type["OPCODE"] ))[2:].zfill(6)
    addr_b = str( bin( j_type["ADDRESS"] ))[2:].zfill(26)
    bin_mif = op_b + addr_b
    if(debug):   
        if( format_to_file ):
            file_bin.write(str('{0:08X}'.format(hex_mif)))
        else:
            file_bin.write(bin_mif)
        file_bin.write('\n') 
            
def verifySymbol(word):
    if( word[0] != "$" ):
        _sys.exit(0)
        return 0
    else:
        return 1
                
def main():
    global format_to_file
    global counter_line
    message = 0
    if(debug):
        try:
            message = int(raw_input('Type 1 if you want to see the help or Press "Enter" to continuo: '))
        except ValueError:
            message = 0
        if( message == 1):
            print usage
            raw_input('Press "Enter" to close windows')
            _sys.exit(0)
        
    file_name = raw_input("File name: ")
    if(debug):
        file_format = raw_input("0) Binary"+
                                "\n1) Hex"+
                                "\nSelect Format: ")
        format_to_file = int(file_format)
    print "    PC            HEX       TAG         ASM"
    print "-"*53
    ASMMips(file_name)
    if( format_to_file ):
        for idx in range(256-counter_line):
            file_bin.write("00000000")
            file_bin.write('\n') 
    else:
        for idx in range(256-counter_line):
            file_bin.write("00000000000000000000000000000000")
            file_bin.write('\n')     
    file_bin.close()
    _os.startfile(out_file)
    raw_input('Press "Enter" to close windows')
    
if __name__ == '__main__':
    main()