#!/usr/bin/python
import serial


#used port by raspberry
COMPORT="/dev/ttyACM0"
COMBAUD=9600
ALLOWSERIAL1="A9A23D59"
ALLOWSERIAL2="A9A63A8E"
'''
one shot read request
'''
def serialRead():
    rtn_str=""
        
    ser=serial.Serial(port=COMPORT,baudrate=COMBAUD,parity=serial.PARITY_NONE,stopbits=serial.STOPBITS_ONE,bytesize=serial.EIGHTBITS,timeout=0)
    print ("Connected to serial port")
    seq=[]
    rpc=True
    while (rpc):
        for c in ser.read():
            seq.append(c)
            if (c == '\n'):
                print(seq)
                for l in seq:
                    if( (l=='\n') or (l=='\r')):
                        pass
                    else:
                        rtn_str=rtn_str+l
                print(rtn_str)
                seq=[]
                rpc=False
                break
    return rtn_str
                

'''
#test part

if __name__ == "__main__":
    strint=serialRead()
    print(strint)
'''

    
