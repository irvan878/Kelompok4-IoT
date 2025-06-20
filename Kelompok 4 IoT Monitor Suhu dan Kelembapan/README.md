# IOT-Monitor-Suhu-dan-Kelembapan
Proyek ini merupakan implementasi sistem monitoring suhu dan kelembapan secara real-time menggunakan mikrokontroler ESP8266, sensor DHT11/DHT22, dan platform cloud ThingSpeak sebagai antarmuka visualisasi data. ESP8266 digunakan untuk membaca data dari sensor DHT11 dan menampilkannya ke layar LCD maupun mengirimkannya ke platform ThingSpeak. Sensor DHT11 dapat mendeteksi suhu dan kelembapan dengan cukup baik, dan datanya bisa diakses secara langsung dan jarak jauh. Layar LCD 16x2 menampilkan informasi suhu dan kelembapan secara real-time, sehingga memudahkan pemantauan secara langsung. Sistem ini juga mampu terhubung dengan WiFi dan mengirim data secara berkala ke internet, memungkinkan kita memantau kondisi lingkungan dari mana saja.


Hardware :
1. Esp8266
2. LCD 16x2 l2C
3. Sensor DHT11

Software dan Tools :
1. Arduino IDE
2. Library:
   - ESP8266WiFi.h
   - DHT.h
   - ThingSpeak.h
4. ThingSpeak (akun dan channel)

Wiring Diagram :
![Diagram](https://github.com/user-attachments/assets/aa06326a-987d-4a6c-88f5-24241e1ed06c)

Desain Circuit:
![Desin](https://github.com/user-attachments/assets/2c44d758-de7e-499a-be81-e6c6c8a34a98)

1. Buat Channel di ThingSpeak
   https://thingspeak.mathworks.com/
   - Daftar/login ke ThingSpeak
   - Buat channel baru
   - Aktifkan field 1 dan field 2 untuk suhu dan kelembapan
   - Salin Write API Key
3. Instal Library di Arduino IDE
   - Melalui Library Manager:
     - DHT sensor library by Adafruit
     - ThingSpeak library
     - ESP8266 board melalui Board Manager

4. Upload Kode ke ESP8266


Foto Hasil:
![hasil](https://github.com/user-attachments/assets/ba694b21-195f-4a93-b8d0-eb85877c2173)
![Thingspeak](https://github.com/user-attachments/assets/23d1ebe9-eed6-46c1-a77d-ce1b679689a1)

