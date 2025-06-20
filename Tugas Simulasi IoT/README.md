# Simulasi-IoT Cisco Packet Tracert Kelompok 4
Selamat datang di repositori Simulasi IoT Smart Home! Proyek ini adalah simulasi sistem Smart Home berbasis IoT (Internet of Things) menggunakan Cisco Packet Tracer. Dalam simulasi ini, berbagai perangkat di seperti SBC-PT, lampu, pintu garasi, pintu, dan Montiom Sensor dapat diatur dan dikendalikan melalui sebuah aplikasi berbasis web yang terhubung ke jaringan rumah.
Tujuan utama projek ini adalah untuk mempelajari bagaimana perangkat IoT berkomunikasi dalam jaringan lokal, serta bagaimana kita dapat mengontrol dan memonitor perangkat-perangkat tersebut secara otomatis menggunakan teknologi jaringan.

Simulasi di bagi menjadi 3 yaitu:
1. Analog Led
2. Smart Home Digital
3. Smart Home IoT
   
Teknologi yang Digunakan
- Cisco Packet Tracer: Digunakan untuk mensimulasikan jaringan perangkat IoT di rumah pintar.
- IoT Devices: Berbagai perangkat IoT seperti SBC-PT, Montion Sensor, lampu dan Garage door.
- Protokol: Protokol komunikasi seperti MQTT atau HTTP digunakan untuk komunikasi antar perangkat.
- Pemrograman: Beberapa perangkat mungkin membutuhkan pemrograman menggunakan Python.

Langkah-langkah Menjalankan Simulasi
1. Unduh dan Install Cisco Packet Tracer jika belum memiliki.
   Link software: https://www.nesabamedia.com/download-cisco-packet-tracer/ 
2. Clone repositori ini:

   git clone https://github.com/irvan878/Simulasi-IoT
4. Buka file .pkt di Cisco Packet Tracer pada masing-masing folder.
5. Jalankan masing-masing simulasi dan lihat bagaimana perangkat Smart Home berfungsi.

-------------------------------------------------------------------------------------------------------------------------------
TOPOLOGI
1. Analog Led
  
  Simulasi Sistem ini menggunakan perangkat analog untuk mengontrol dan memantau perangkat output seperti LED. Sistem analog lebih sederhana dan tidak terhubung dengan internet atau perangkat lain dalam jaringan.
  
  Device :
  - SBC-PT
  - Rocker Switch
  - Led
    
  Input seperti saklar rocker (rocker switch) digunakan untuk memberikan sinyal on/off, yang kemudian diproses oleh SBC (Single-Board Computer) dan dihubungkan ke LED sebagai output.

  ![image](https://github.com/user-attachments/assets/f8b8db82-7e7d-426a-9862-8d40d3dbeadb)

2. Smart Home Digital
  
  Simuasi sistem digital, perangkat seperti sensor gerak dan pintu garasi dikendalikan dan dipantau secara otomatis. Semua perangkat terhubung dengan SBC yang mengatur logika dan proses secara lokal, tanpa melibatkan komunikasi
  nirkabel atau Internet.

  Device:
  - SBC-PT
  - Montion Sensor
  - Garage Door
  - Light
    
  Input dari sensor gerak mengaktifkan atau menonaktifkan perangkat output seperti pintu garasi atau lampu.

  ![image](https://github.com/user-attachments/assets/8ba9b28a-d48d-45f3-8524-39e467239f66)

3. Smart Home IoT

   Simulasi sistem IoT, terdapat koneksi nirkabel yang menghubungkan berbagai perangkat seperti sensor gerak, smartphone, dan perangkat output (pintu, lampu, garasi). Dalam sistem ini, ada komunikasi data yang dilakukan secara nirkabel      (wireless), memberikan fleksibilitas dan kemampuan untuk mengontrol perangkat dari mana saja melalui aplikasi atau perangkat lain yang terhubung ke jaringan.

   Device:
   - Home Gateway DLC100
   - Smartphone-PT
   - Montion Detector
   - Garage Door
   - Light
   - Door
     
   Sistem ini lebih canggih dan melibatkan Home Gateway Wireless (DLC100) yang menghubungkan perangkat IoT ke jaringan dan memungkinkan kontrol dari jarak jauh menggunakan smartphone.

![image](https://github.com/user-attachments/assets/274c9beb-b104-493f-9b05-1ef2cfcb6a38)

-------------------------------------------------------------------------------------------------------------------------------
Kesimpulan:
- Analog lebih sederhana, mengandalkan perangkat fisik yang saling terhubung tanpa pengolahan data atau kontrol jarak jauh.
- Digital menggunakan logika digital untuk mengatur perangkat, tetapi tetap dalam jaringan lokal tanpa konektivitas ke Internet.
- IoT mengintegrasikan perangkat ke dalam jaringan Internet, memungkinkan kontrol dan monitoring perangkat dari jarak jauh dengan fleksibilitas tinggi, termasuk penggunaan aplikasi mobile untuk mengontrol berbagai perangkat.
