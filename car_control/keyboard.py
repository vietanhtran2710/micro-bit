import serial
import serial.tools.list_ports as list_ports
from pynput.keyboard import Key, Controller

PID_MICROBIT = 516
VID_MICROBIT = 3368
TIMEOUT = 0.1

keyboard = Controller()
left_key, right_key = "a", "d"
hold_left, hold_right = False, False
break_key, move_key = "s", "w"
hold_break, hold_move = False, False

def find_comport(pid, vid, baud):
    ''' return a serial port '''
    ser_port = serial.Serial(timeout=TIMEOUT)
    ser_port.baudrate = baud
    ports = list(list_ports.comports())
    print('scanning ports')
    for p in ports:
        print('port: {}'.format(p))
        try:
            print('pid: {} vid: {}'.format(p.pid, p.vid))
        except AttributeError:
            continue
        if (p.pid == pid) and (p.vid == vid):
            print('found target device pid: {} vid: {} port: {}'.format(
                p.pid, p.vid, p.device))
            ser_port.port = str(p.device)
            return ser_port
    return None

print('looking for microbit')
ser_micro = find_comport(PID_MICROBIT, VID_MICROBIT, 115200)
if not ser_micro:
    print('microbit not found')
else:
    print('opening and monitoring microbit port')
    ser_micro.open()
    while True:
        try:
            line = ser_micro.readline().decode('utf-8')
        except Exception:
            pass
        if line:
            try:
                items = line.strip().split()
                x = int(items[0])
                button = items[-1]
            except Exception:
                continue
            if x <= -300 and not hold_right:
                keyboard.press(right_key)
                keyboard.release(left_key)
                hold_left, hold_right = True, False
            elif x >= 300 and not hold_left:
                keyboard.press(left_key)
                keyboard.release(right_key)
                hold_right, hold_left = True, False
            else:
                keyboard.release(left_key)
                keyboard.release(right_key)
                hold_left, hold_right = False, False
            if button[1] == "1" and not hold_move:
                keyboard.press(move_key)
                hold_move = True
                continue
            else:
                keyboard.release(move_key)
                hold_move = False
            # if button[0] == "1" and not hold_break:
            #     keyboard.press(break_key)
            #     hold_break = True
            # else:
            #     keyboard.release(break_key)
            #     hold_break = False
    ser_micro.close()