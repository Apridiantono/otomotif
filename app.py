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

# Data sensor simulasi
sensor_data = {
    'rpm': 0,
    'speed': 0,
    'tire_pressure': [0, 0, 0, 0],
    'engine_temp': 0
}

# Fungsi background update data sensor
def sensor_update_loop():
    while True:
        sensor_data['rpm'] = round(random.uniform(1000, 3500), 1)
        sensor_data['speed'] = random.randint(0, 120)
        sensor_data['tire_pressure'] = [34, 35, 35, 33]
        sensor_data['engine_temp'] = random.randint(75, 115)
        time.sleep(1)

# Mulai thread update data sensor
_thread.start_new_thread(sensor_update_loop, ())

# Routing halaman utama
@app.route('/')
def index(request):
    return send_file('templates/index.html')

# Routing file statis
@app.route('/static/<path:path>')
def static(request, path):
    content_type = 'text/plain'
    if path.endswith('.css'):
        content_type = 'text/css'
    elif path.endswith('.js'):
        content_type = 'application/javascript'
    return send_file('static/' + path, content_type=content_type)

# Endpoint data sensor
@app.route('/data')
def data(request):
    return sensor_data

# Jalankan web server
if __name__ == '__main__':
    #print(ip_address)
    app.run(host='0.0.0.0', port=5000, debug=True)
