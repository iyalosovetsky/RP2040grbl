from machine import UART, Pin
import time

# for communicate with usb keybord module
# keyboard module set keycode like this:
#  0x1 byte1 byte2 byte3 !byte1 !byte2 !byte3 0x2
#  for example 
#  0x1 0x1 0x0 0xa 0xfe 0xff 0xf5 0x2
#  where 
#    byte1 is ctrl 
#    byte2 is alt(0x04),ralt(0x40),ctrl(0x01),rctrl(0x10),shit(0x02),rctrl(0x20) , opt(0x08) , ropt(0x80) 
#    byte3 keycode - 'g' button

DEBUG = False

uartKBD = UART(1, baudrate=9600, bits=8, parity=None, stop=1, tx=Pin(4), rx=Pin(5))
uartMPG = UART(0, baudrate=115200, bits=8, parity=None, stop=1, tx=Pin(0), rx=Pin(1))
txData = b'RS485 send test...\r\n'
print('RS485 send test...')

HID_KEYCODE_TO_ASCII =[
    [b'\x00', b'\x00'], # 0x00 
    [b'\x00', b'\x00'], # 0x01  
    [b'\x00', b'\x00'], # 0x02  
    [b'g'   , b'G'    ], # 0x03  
    [b'a'   , b'A'    ], # 0x04 
    [b'b'   , b'B'    ], # 0x05 
    [b'c'   , b'C'    ], # 0x06 
    [b'd'   , b'D'    ], # 0x07 
    [b'e'   , b'E'    ], # 0x08 
    [b'f'   , b'F'    ], # 0x09 
    [b'g'   , b'G'    ], # 0x0a 
    [b'h'   , b'H'    ], # 0x0b 
    [b'i'   , b'I'    ], # 0x0c 
    [b'j'   , b'J'    ], # 0x0d 
    [b'k'   , b'K'    ], # 0x0e 
    [b'l'   , b'L'    ], # 0x0f 
    [b'm'   , b'M'    ], # 0x10 
    [b'n'   , b'N'    ], # 0x11 
    [b'o'   , b'O'    ], # 0x12 
    [b'p'   , b'P'    ], # 0x13 
    [b'q'   , b'Q'    ], # 0x14 
    [b'r'   , b'R'    ], # 0x15 
    [b's'   , b'S'    ], # 0x16 
    [b't'   , b'T'    ], # 0x17 
    [b'u'   , b'U'    ], # 0x18 
    [b'v'   , b'V'    ], # 0x19 
    [b'w'   , b'W'    ], # 0x1a 
    [b'x'   , b'X'    ], # 0x1b 
    [b'y'   , b'Y'    ], # 0x1c 
    [b'z'   , b'Z'    ], # 0x1d 
    [b'1'   , b'!'    ], # 0x1e 
    [b'2'   , b'@'    ], # 0x1f 
    [b'3'   , b'#'    ], # 0x20 
    [b'4'   , b'$'    ], # 0x21 
    [b'5'   , b'%'    ], # 0x22 
    [b'6'   , b'^'    ], # 0x23 
    [b'7'   , b'&'    ], # 0x24 
    [b'8'   , b'*'    ], # 0x25 
    [b'9'   , b'('    ], # 0x26 
    [b'0'   , b')'    ], # 0x27 
    [b'\r'  , b'\r'   ], # 0x28 
    [b'esc', b'esc' ], # 0x29 esc
    [b'backspace'  , b'shift backspace'   ], # 0x2a 
    [b'\t'  , b'\t'   ], # 0x2b 
    [b'space'   , b'shift space'    ], # 0x2c 
    [b'-'   , b'_'    ], # 0x2d 
    [b'='   , b'+'    ], # 0x2e 
    [b'['   , b'{'    ], # 0x2f 
    [b']'   , b'}'    ], # 0x30 
    [b'\\'  , b'|'    ], # 0x31 
    [b'#'   , b'~'    ], # 0x32 
    [b';'   , b':'    ], # 0x33 
    [b"'"   , b'"'    ], # 0x34 
    [b'`'   , b'~'    ], # 0x35 
    [b','   , b'<'    ], # 0x36 
    [b'.'   , b'>'    ], # 0x37 
    [b'/'   , b'?'    ], # 0x38 
    [b'\x00', b'\x00'], # 0x39 
    [b'f1', b'f1'], # 0x3a 
    [b'f2', b'f2'], # 0x3b 
    [b'f3', b'f3'], # 0x3c 
    [b'f4', b'f4'], # 0x3d 
    [b'f5', b'f5'], # 0x3e 
    [b'f6', b'f6'], # 0x3f 
    [b'f7', b'f7'], # 0x40 
    [b'f8', b'f8'], # 0x41 
    [b'f9', b'f9'], # 0x42 
    [b'f10', b'f10'], # 0x43 
    [b'f11', b'f11'], # 0x44 
    [b'f12', b'f12'], # 0x45 
    [b'prtScr', b'prtScr'], # 0x46 
    [b'scrollLock', b'scrollLock'], # 0x47 
    [b'pause', b'pause'], # 0x48 
    [b'insert', b'shift insert'], # 0x49 
    [b'home', b'shift home'], # 0x4a 
    [b'pageUp', b'shift pageUp'], # 0x4b 
    [b'del', b'shift del'], # 0x4c 
    [b'end', b'shift end'], # 0x4d 
    [b'pageDown', b'shift pageDown'], # 0x4e 
    [b'\x00', b'\x00'], # 0x4f 
    [b'\x00', b'\x00'], # 0x50 
    [b'\x00', b'\x00'], # 0x51 
    [b'\x00', b'\x00'], # 0x52 
    [b'\x00', b'\x00'], # 0x53 
    [b'/'   , b'/'    ], # 0x54 
    [b'*'   , b'*'    ], # 0x55 
    [b'-'   , b'-'    ], # 0x56 
    [b'+'   , b'+'    ], # 0x57 
    [b'\r'  , b'\r'   ], # 0x58 
    [b'1'   , b'!'], # 0x59 
    [b'2'   , b'@'], # 0x5a 
    [b'3'   , b'#'], # 0x5b 
    [b'4'   , b'$'], # 0x5c 
    [b'5'   , b'%'], # 0x5d 
    [b'6'   , b'^'], # 0x5e 
    [b'7'   , b'&'], # 0x5f 
    [b'8'   , b'*'], # 0x60 
    [b'9'   , b'('], # 0x61 
    [b'0'   , b')'], # 0x62 
    [b'.'   , b'%'], # 0x63 
    [b'\x00', b'\x00'], # 0x64 
    [b'\x00', b'\x00'], # 0x65 
    [b'\x00', b'\x00'], # 0x66 
    [b'='   , b'='   ] # 0x67  
]


time.sleep(1)

start_time=time.time()-1000
ii=0

def getKeyName(kbdData):
    l_char=''
    l_shift=0
    l_ctrl=0
    l_caps=0
    if not(kbdData[0]==1 and len(kbdData)%8==0 and len(kbdData)>=8 and kbdData[7]==2):
       return l_char, l_shift,-1,-1
    if not(kbdData[1]|kbdData[4]==255 and kbdData[2]|kbdData[5]==255 and kbdData[3]|kbdData[6]==255):    
       return l_char, l_shift,-1,-2
    l_ctrl=kbdData[2]
    l_caps=kbdData[1]
    l_scan=kbdData[3]
    l_numlockOff = (l_caps & 1 == 0)
    if (l_scan==0x50 or (l_scan==0x5c and l_numlockOff)): #left 
        l_char='left'     
    elif (l_scan==0x4f or (l_scan==0x5e and l_numlockOff)): #rigth
        l_char='rigth'     
    elif (l_scan==0x52 or (l_scan==0x60 and l_numlockOff)): #up
        l_char='up'     
    elif ((l_scan==0x61 and l_numlockOff)): #pageUp
        l_char='pageUp'     
    elif ((l_scan==0x5b and l_numlockOff)): #pageDown
        l_char='pageDown'     
    elif ((l_scan==0x5f and l_numlockOff)): #home
        l_char='home'     
    elif ((l_scan==0x59 and l_numlockOff)): #end
        l_char='end'     
    elif ((l_scan==0x62 and l_numlockOff)): #end
        l_char='insert'     
    elif ((l_scan==0x63 and l_numlockOff)): #del
        l_char='del'     
    elif (l_scan==0x51 or (l_scan==0x5a and l_numlockOff)): #down
        l_char='down'     
    elif (l_scan==0x28 or (l_scan==0x58 and l_numlockOff)): #enter
        l_char='enter'     
    else: 
        if (l_ctrl & 0xdd)==0: ## no shift noalt 
            if not(l_scan>=0x59 and l_scan<=0x63):
                l_shift= 1 if ((l_ctrl & 0x22)>0) else 0
                if (l_caps & 0x02):
                    l_shift ^=1 
            l_char=HID_KEYCODE_TO_ASCII[l_scan][l_shift].decode()        
        else:    
            l_char +=('r' if (l_ctrl & 0x40) else '')+('alt-' if (l_ctrl & 0x44) else '')
            l_char +=('r' if (l_ctrl & 0x10) else '')+('ctrl-' if (l_ctrl & 0x11) else '')
            l_char +=('r' if (l_ctrl & 0x20) else '')+('shift-' if (l_ctrl & 0x22) else '')
            l_char +=('r' if (l_ctrl & 0x80) else '')+('opt-' if (l_ctrl & 0x88) else '')
            l_char +=HID_KEYCODE_TO_ASCII[l_scan][0].decode() 
    return l_char, l_shift, l_ctrl, l_caps

def flashKbdLeds(p_leds_mask: int , p_macro_n: int):
    # kk=0x17     #7 - 3 leds       # 1 - macro1
    #print ("flashKbdLeds:", p_leds_mask , p_macro_n)
    kk=(p_macro_n&15)*16 | (p_leds_mask&15)
    cmd[1]=kk
    cmd[2]=255-kk
    uartKBD.write(cmd)
    # print("sended 0 ->"," ".join(hex(n) for n in cmd))


LED_SCROLLLOCK =  0x04
LED_CAPSLOCK = 0x02
LED_NUMLOCK = 0x01
LED_ALL = LED_SCROLLLOCK + LED_CAPSLOCK + LED_NUMLOCK

BLINK_2 = 1
BLINK_5 = 2
BLINK_INFINITE = 3
NOBLINK = 4

g_state = 'idle'
g_state_old = 'idle'


g_mpg_state = False
g_mpg_state_old = False
g_feedrate = 1000.0
g_step = 5.0
g_step_z = 1.0
C_STEP_MAX = 100
C_STEP_MIN = 0.1

C_STEP_Z_MAX = 20
C_STEP_Z_MIN = 0.1

C_FEED_MAX = 8000
C_FEED_MIN = 200




#jog $J=G91 X0 Y-5 F600
#$J=G91 X1 F100000
#MPG -> <Idle|MPos:30.000,0.000,0.000|Bf:35,1023|FS:0,0,0|Pn:HS|WCO:0.000,0.000,0.000|WCS:G54|A:|Sc:|MPG:1|H:0|T:0|TLR:0|Sl:0.0|FW:grblHAL>
def parseState(grblState:str):
    l_state:str = None
    l_mpg_state:bool = None
    if grblState is None:
      return None, None
    if grblState.startswith('error:'):
      return 'error', None

    if not (grblState.startswith('<') and grblState.endswith('>')):
      return None, None
            
    for ii,token in enumerate(grblState.replace('<','').replace('>','').lower().split('|')):
        if ii==0 :
          l_state = token
        else:
            elem = token.split(':')
            if len(elem)>1 and elem[0]=='mpg' and elem[1] is not None:
                    l_mpg_state=(elem[1]=='1')
    return (l_state, l_mpg_state)    

def displayState(grblState:str):     
    global g_state
    global g_mpg_state
    l_state, l_mpg_state =  parseState(grblState.strip())
    print("MPG ->",grblState,' - >>',l_state, l_mpg_state,'now=>',g_state, g_mpg_state)
    if l_mpg_state is not None and g_mpg_state!=l_mpg_state:
        g_mpg_state=l_mpg_state
        
        flashKbdLeds(LED_SCROLLLOCK , BLINK_5 if g_mpg_state else BLINK_2) 
    if l_state is not None:  
        if  l_state!= g_state or l_state == 'run' or l_state == 'hold' or l_state == 'jog' or l_state == 'alarm':
            if l_state == 'alarm':
                flashKbdLeds(LED_ALL , BLINK_INFINITE) 
            elif l_state == 'run':    
                flashKbdLeds(LED_SCROLLLOCK , BLINK_5) 
            elif l_state == 'jog':    
                flashKbdLeds(LED_SCROLLLOCK , BLINK_5) 
            elif l_state == 'hold':    
                flashKbdLeds(LED_NUMLOCK , BLINK_INFINITE) 
            elif l_state == 'error':    
                flashKbdLeds(LED_CAPSLOCK , BLINK_5) 
            elif l_state == 'idle' and g_state!=l_state:    
                flashKbdLeds(LED_ALL , NOBLINK) 
            g_state = l_state
    #print("MPG[2] ->",'now=>',g_state, g_mpg_state)






            

    
    

def mpgCommand(command:str):
    print("mpgCommand:",command)
    uartMPG.write(command.encode())


def grblJog(x:float=0.0, y: float=0.0, z:float=0.0):
    f=g_feedrate
    if x is not None and x!=0.0:
       mpgCommand(f'$J=G91 G21 X{x} F{f} \r\n') 
    elif y is not None and y!=0.0:
       mpgCommand(f'$J=G91 G21 Y{y} F{f} \r\n')    
    elif z is not None and z!=0.0:
       mpgCommand(f'$J=G91 G21 Z{z} F{f} \r\n')    





def sent2grbl(command:str):
  global g_feedrate
  global g_step
  global g_step_z
  print('sent2grbl:',command)
  if command in ('~','!','?'):
    flashKbdLeds(LED_ALL , BLINK_2) ##7 - 3 leds       # 1 - macro1
    mpgCommand(command)
  elif command=='left' or command=='rigth':
      grblJog(y=g_step *(1.0 if command=='rigth' else -1.0))
  elif command=='up' or command=='down':
      grblJog(x=g_step *(1.0 if command=='up' else -1.0))
  elif command=='pageUp' or command=='pageDown':
      grblJog(z=g_step_z *(1.0 if command=='pageDown' else -1.0))
  elif command=='f4' or command=='f5':
      g_feedrate =  g_feedrate+100
      if  g_feedrate>C_FEED_MAX:
          g_feedrate=C_FEED_MAX
      elif g_feedrate<C_FEED_MIN:
          g_feedrate=C_FEED_MIN
      print('g_feedrate now',g_feedrate)        
  elif command=='f1' or command=='f2':
      g_step =  g_step*(10 if command=='f2' else 0.1)
      if  g_step>C_STEP_MAX:
          g_step=C_STEP_MAX
      elif g_step<C_STEP_MIN:
          g_step=C_STEP_MIN
      print('g_step now',g_step)    
  elif command=='f3' or command=='f4':
      g_step_z =  g_step_z*(10.0 if command=='f4' else 0.1)
      if  g_step_z>C_STEP_Z_MAX:
          g_step_z=C_STEP_Z_MAX
      elif g_step_z<C_STEP_Z_MIN:
          g_step_z=C_STEP_Z_MIN
      print('g_step_z now',g_step_z)    
  elif command in ('#'):  
    flashKbdLeds(LED_SCROLLLOCK , BLINK_5) ##2 - leds ???       # 2 - macro1 10/2 blink
    uartMPG.write(bytearray(b'\x8b\r\n'))
  elif command in ('@'):  
    flashKbdLeds(LED_SCROLLLOCK , BLINK_5) ##2 - leds ???       # 2 - macro1 10/2 blink
    uartMPG.write(bytearray(b'\x85\r\n'))
    uartMPG.write(bytearray(b'\x18\r\n')) # cancel ascii
  elif command in ('$'):  
    flashKbdLeds(LED_ALL , BLINK_2) ##7 - 3 leds       # 1 - macro1
    uartMPG.write('$X'.encode()+b'\r\n')
  else:
    #flashKbdLeds(LED_ALL , BLINK_5) ##7 - 3 leds       # 1 - macro1 5/2 blinks  - macro2 10/2 blinks - macro3 infinite blinks - macro4 base 
    uartMPG.write(command.encode()+b'\r\n')




COMMAND=''
MACROS={}

cmd=bytearray(  [0x01,0x01,0xFE,0x02])
start_time_q = time.time()
while True:
    #try:
        time.sleep(0.05) #50ms
        if time.time()-start_time_q>3:
            uartMPG.write(('?' if g_state == 'jog' else '?').encode()  )
            start_time_q = time.time()
        # if time.time()-start_time>1200:
        #     ii +=1
        #     start_time = time.time()
        #     kk=(0x27 if ii%2 else 0x00)
        #     cmd[1]=kk
        #     cmd[2]=255-kk
        #     uartKBD.write(cmd)
        #     print("sended ->"," ".join(hex(n) for n in cmd))
        while uartMPG.any() > 0:
            rxMPG = uartMPG.read()
            displayState(rxMPG.decode())
            
        while uartKBD.any() > 0:
            rxdata = uartKBD.read()
            # print("gets[string0 ->"," ".join(hex(n) for n in rxdata))
            for i in range(0, len(rxdata), 8):
                line1 = rxdata[i:i + 8] 
                l_char, l_shift, l_ctrl, l_caps = getKeyName(line1)
                # print("gets[string0/1 char ->",l_char,"error ->",l_ctrl,l_caps," ".join(hex(n) for n in line1))
                if l_char =='esc' or l_char =='@' or l_char =='$' or \
                    l_char =='~' or l_char =='#' or l_char =='?' or l_char =='!' or \
                    l_char =='left' or l_char =='rigth' or l_char =='pageUp' or l_char =='pageDown' or \
                    l_char =='up' or l_char =='down' or \
                    l_char =='f1' or l_char =='f2' or l_char =='f3' or l_char =='f4' or \
                    l_char =='enter' or \
                    (l_char.startswith('ctrl-f') and len(l_char)>6) or (l_char.startswith('alt-f') and len(l_char)>5):
                    if l_char in ('~','!','?','#','$','@') or \
                        l_char =='left' or l_char =='rigth' or l_char =='pageUp' or l_char =='pageDown' or \
                        l_char =='up' or l_char =='down' or \
                        l_char =='f1' or l_char =='f2' or l_char =='f3' or l_char =='f4':
                        sent2grbl(l_char)
                        COMMAND=''
                    elif l_char in ('esc'):
                        COMMAND=''
                        if g_state == 'run' or g_state == 'jog':
                            sent2grbl('@')
                        else:
                            flashKbdLeds(7 , 1) ##7 - 3 leds       # 1 - macro1
                        
                    elif l_char in ('enter'):
                        sent2grbl(COMMAND)
                        COMMAND=''
                        
                    elif l_char in ('backspace'):
                        COMMAND =COMMAND[0:-1]

                    elif l_char.startswith('ctrl-f') and len(l_char)>6:
                        COMMAND=MACROS.get(l_char[5:],'')
                        print('command/restrore F macro->',l_char[5:],'<-',COMMAND)
                        COMMAND=''
                    elif l_char.startswith('alt-f') and len(l_char)>5:
                        print('command/set F macro->',l_char[4:],'=',COMMAND)
                        MACROS[l_char[4:]]=COMMAND
                        COMMAND=''
                elif l_char in ('space'):
                    COMMAND +=' '
                    
                elif not(l_char.startswith('alt-') or l_char.startswith('shift-') or l_char.startswith('ctrl-') or l_char.startswith('opt-')
                          or l_char.startswith('ralt-') or l_char.startswith('rshift-') or l_char.startswith('rctrl-') or l_char.startswith('ropt-')):    
                    COMMAND +=l_char
                    
                    
                    
            
            if DEBUG:
                try:
                    print("end of get ->",COMMAND, l_shift,hex(rxdata[1]),rxdata[2],rxdata[3],l_char)
                except Exception as e1:
                    print("rt error",e1)
                    
                print()
                #rxdata = uart1.read()

#except Exception as e1:
    #    print("rt error",e1)

