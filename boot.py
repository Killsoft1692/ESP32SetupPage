import network
import usocket as socket
import ujson as json
import uos as os
import gc


if not 'setup.ini' in os.listdir():
    import initial

cnf = json.loads(open('setup.ini', 'r').read())

ap = network.WLAN(network.STA_IF)
ap.active(True)
ap.connect(cnf['ssid'], cnf['pwd'])

gc.collect()
