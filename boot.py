import usocket as socket
import ujson as json
import uos as os
import network
import machine
import gc

rst = machine.Pin(12, machine.Pin.IN, machine.Pin.PULL_UP)

if not 'setup.ini' in os.listdir():
    import initial
elif not rst.value():
    os.remove('setup.ini')
    machine.reset()

cnf = json.loads(open('setup.ini', 'r').read())

ap = network.WLAN(network.STA_IF)
ap.active(True)
ap.connect(cnf['ssid'], cnf['pwd'])

gc.collect()
