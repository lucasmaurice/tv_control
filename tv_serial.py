import time, serial, signal

class TvSerial:
    @staticmethod
    def handler(signum, frame):
        raise Exception("Serial connection timeout")

    @staticmethod
    def writeCommand(command):
        print("Will execute: " + command)
        
        signal.signal(signal.SIGALRM, TvSerial.handler)
        signal.alarm(10)

        try:
            # configure the serial connections (the parameters differs on the device you are connecting to)
            ser = serial.Serial(port='/dev/ttyUSB0', baudrate=9600, parity=serial.PARITY_NONE, stopbits=serial.STOPBITS_ONE, bytesize=serial.EIGHTBITS)
            ser.xonxoff = False
            ser.rtscts = False
            ser.dsrdtr = False
            
            # prepare command
            serialcmd = command + '\r\n'
            
            # execute command
            ser.write(serialcmd.encode())

            out = ''
            while out != 'WAIT' and out != 'OK' and out != 'ERR':

                # wait for answer
                while ser.inWaiting() == 0:
                    time.sleep(0.5)
            
                # read answers
                while ser.inWaiting() > 0:
                    char = ser.read(1).decode('utf-8')
                    if char != "\n" and char != "\r":
                        out += char
                    if out == "WAIT":
                        out = ""

        except Exception:
            return "TIMEOUT"

        signal.alarm(0)
        return out

