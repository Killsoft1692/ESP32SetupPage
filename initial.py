import network
import machine
import usocket as socket
import ujson as json


def run():
    html = """
      <html>
      <head>
      <title>Setup Page</title>
      <style>
      input {
        border: none;
        padding: 12px 20px;
        margin: 8px 0;
        border-bottom: 2px solid red;
      }
      form {
        margin: 80px;
      }
      button {
        background-color: #4CAF50;
        color: white;
        with: 80px;
        margin: 4px 2px;
        padding: 16px 32px;
        border: none;
      }
      </style>
      </head>
      <body>
      <h1>######## Setup ########</h1> 
          <form action="/" method="post">
            <p><label for="ssid">SSID</label></p>
            <p><input id="ssid" type="text" name="ssid" required/></p>
            <p><label for="pwd">Password</label></p>
            <p><input id="pwd" type="text" name="pwd" required/></p>
            <button type="submit">Save</button>
          </form>
      </body>
      </html>
      """

    ap = network.WLAN(network.AP_IF)
    ap.active(True)
    ap.config(essid="Setup")

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(('', 80))
    s.listen(5)

    while True:
        conn, _ = s.accept()
        request = conn.recv(1024)
        request = str(request)
        data = request.find('ssid=')
        if data != -1:
            st = dict((v.split('=')[0], v.split('=')[1]) for v in request[data:-1].split('&'))
            with open('setup.ini', 'w') as file:
                file.write(json.dumps(st))
            machine.reset()
        conn.send(html)
        conn.close()


run()
