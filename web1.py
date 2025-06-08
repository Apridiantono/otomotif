from microdot import Microdot, send_file, Response
import time
import random
#import network
import _thread

'''
# Koneksi WiFi
ssid = 'NAMA_WIFI'
password = 'PASSWORD_WIFI'

sta = network.WLAN(network.STA_IF)
sta.active(True)
sta.connect(ssid, password)
while not sta.isconnected():
    pass

print('Connected, IP:', sta.ifconfig()[0])
'''
# Inisialisasi aplikasi
app = Microdot()
Response.default_content_type = 'text/html'

# Routing halaman utama
@app.route('/')
def index(request):
    return send_file('templates/index.html')

# Routing file statis
@app.route('/static/<filename>')
def static_files(request, filename):
    return send_file(f'static/{filename}')

# Endpoint data sensor
@app.route('/data')
def data(request):
    return 0

# Jalankan web server
if __name__ == '__main__':
    #print(ip_address)
    app.run(host='0.0.0.0', port=5000, debug=True)
