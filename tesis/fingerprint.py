#!/usr/bin/env python

import mraa


DEFAULT_BAUDRATE = 57600
HEADER = 0xEF01
# COMMANDS = {
            # 'handshake': {'header': HEADER << (11 * 8)},
            # 'GenImg': {},
            # 'Img2Tz': {},
            # 'RegModel': {},
            # 'Store': {},
            # 'Search': {}

           # }
          
class FingSens():
    def __init__(self, device_address, uart_port):
        self.address = device_address
        #Configure uart port.
        self.uart = mraa.Uart(uart_port)
        self.uart.setBaudRate(DEFAULT_BAUDRATE)
        self.uart.setMode(8, mraa.UART_PARITY_NONE, 1)
        self.uart.setFlowcontrol(False, False)

    def handshake(self):
        cmd = (HEADER << (11 * 8)) | (self.address << (7 * 8)) | (0x1 << (6 * 8)) | (0x4 << (4*8)) | (0x17 << (3*8)) | 0x1C
        print '%x' % cmd        
        self.send_command(cmd)
        response = self.check_acknowledge()
        if response[9] == '\x00':
            print "handshake : SUCCESS"
        else:
            print "handshake : FAIL"
            
    def collect_fing(self):
        self.check_acknowledge()
        cmd = (HEADER << (10 * 8)) | (self.address << (6 * 8)) | (0x1 << (5 * 8)) | (0x3 << (3*8)) | (0x1 << (2*8)) | 0x5
        print '%x' % cmd        
        self.send_command(cmd)
        response = self.check_acknowledge()
        if response[9] == '\x00':
            print "finger collect : SUCCESS"
            return True
        else:
            print "finger collect : FAIL"
            return False
        
    def generate_char_file(self, buffer_id):
        cmd = (HEADER << (11 * 8)) | (self.address << (7 * 8)) | (0x1 << (6 * 8)) | (0x4 << (4*8)) | (0x2 << (3*8)) | (buffer_id << (2*8)) | ((0x1 + 0x4 + 0x2 + buffer_id) & 0xFFFF)
        print '%x' % cmd        
        self.send_command(cmd)
        response = self.check_acknowledge()
        if response[9] == '\x00':
            print "char generation : SUCCESS"
        else:
            print "char generation : FAIL"
    
    def store_template(self, buffer_id, page_id):
        cmd = (HEADER << (13 * 8)) | (self.address << (9 * 8)) | (0x1 << (8 * 8)) | (0x6 << (6*8)) | (0x6 << (5*8)) | (buffer_id << (4*8)) | (page_id << (2*8)) | ((0x1 + 0x6 + 0x6 + buffer_id + page_id) & 0xFFFF)
        print '%x' % cmd        
        self.send_command(cmd)
        response = self.check_acknowledge()
        if response[9] == '\x00':
            print "template : SUCCESS"
        else:
            print "template : FAIL"
    
    def generate_template(self):
        cmd = (HEADER << (10 * 8)) | (self.address << (6 * 8)) | (0x1 << (5 * 8)) | (0x3 << (3*8)) | (0x5 << (2*8)) | 0x9
        print '%x' % cmd        
        self.send_command(cmd)
        response = self.check_acknowledge()
        if response[9] == '\x00':
            print "store : SUCCESS"
        else:
            print "store : FAIL"
    
    def search_finger(self, buffer_id, start_page, stop_counter):
        cmd = (HEADER << (15 * 8)) | (self.address << (11 * 8)) | (0x1 << (10 * 8)) | (0x8 << (8*8)) | (0x4 << (7*8)) | (buffer_id << (6*8)) | (start_page << 4) | (stop_counter << (2*8)) | ((0x1 + 0x8 + 0x4 + buffer_id + start_page + stop_counter) & 0xFFFF)
        print '%x' % cmd        
        self.send_command(cmd)
        response = self.check_acknowledge()
        if response[9] == '\x00':
            print "Search : SUCCESS"
            return True, response[10] + response[11]
        else:
            print "Search : FAIL"
            return False, "FAIL"
            
    def check_acknowledge(self):
        data_byte = []
        while True:
            if self.uart.dataAvailable(1000):
                # We are doing 1-byte reads here
                data_byte.append(self.uart.readStr(1))
            else:
                break
        print data_byte
        return data_byte
        
    def send_command(self, cmd):
        msg = '%x' % cmd
        if len(msg)%2:
            msg = '0' + msg
        print "SENDING"
        print msg
        self.uart.write(bytearray.fromhex(msg))
