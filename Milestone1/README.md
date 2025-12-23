**Milestone1 (22/12/2025)**

**1. Jelaskan pin apa saja yang ada di Servo!**
Terdapat 3 pin, yaitu:
- Daya (VCC): berfungsi memasok sejumlah tegangan yang diperlukan agar motor servo bergerak. Terhubung dengan sumber daya positif pada mikon. Kabel warna merah
- Ground (GND): Sebagai jalur kembali arus listrik (titik referensi 0V). Terhubung ke GND pada mikon. Kabel warna coklat atau hitam.
- Sinyal (PWM): berfungsi menerima sinyal berupa Pulse Width Modulation dari mikon yang menentukan sudut putar servo. Terhubung pada pin digital pada mikon. Durasi pulse biasanya ada di rentang 1-2ms dan pulse 1,5ms umumnya mewakili posisi netral. Kabel warna oren, kuning, atau putih.

**2. ESP32 menggunakan baudrate 115200, jelaskan apa itu baudrate? Dan apakah di program python juga harus 115200?**
Baud rate adalah kecepatan transfer data dalam komunikasi serial, menunjukkan berapa banyak perubahan sinyal (bit data) yang dapat dikirim per detik. Dalam konteks port serial, 115200 baud berarti port serialnya mampu mentransfer maksimal 115200 bit per sekon. Semakin tinggi baud rate, semakin cepat pula data dikirim. Baud rate di Python **tidak harus 115200**, yang penting nilainya sama dengan baud rate yang diatur pada mikon melalui Serial.begin (perangkat penerima dan pengirim harus sama baud rate-nya).

**3. Jelaskan alur program yang telah dibuat!**
- Servo biasa: diawali dengan memanggil library ESP32Servo dan membuat objek servo, lalu menentukan pin kontrol servo (13). Pada fungsi setup(), servo dihubungkan ke ponnya agar siap dikendalikan. Pada fungsi loop(), perulangan for menggerakkan servo secara bertahap dari sudut 0 hingga 179 derajat dengan jeda 10 milisekon per derajatnya, kemudian program akan mengulang kembali dari awal setelah mencapai sudut maksimum.
- Servo dengan Python: pada fungsi setup() di Arduino IDE, ESP32 menginisialisasi komunikasi serial dengan baud rate 115200 dan menghubungkan servo ke pin 13. Pada fungsi loop(), ESP32 membaca nilai sudut yang dari komputer menggunakan Serial.parseInt() jika memang ada data yang masuk. Di Python, program membuka koneksi serial ke ESP32 terlebih dulu, lalu meminta user memasukkan sudut gerakan servo yang diinginkan. Nilai sudut tersebut dikirim sebagai data teks melalui port serial ke ESP32 sehingga user dapat mengendalikan pergerakan servo.

Referensi:
- https://www.instructables.com/Interfacing-Servo-Motor-With-Arduino/
- https://www.setra.com/blog/what-is-baud-rate-and-what-cable-length-is-required-1
