{\rtf1\ansi\ansicpg1252\cocoartf2822
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fswiss\fcharset0 Helvetica-Bold;\f1\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\paperw11900\paperh16840\margl1440\margr1440\vieww8940\viewh8420\viewkind0
\pard\tx720\tx1440\tx2160\tx2880\tx3600\tx4320\tx5040\tx5760\tx6480\tx7200\tx7920\tx8640\pardirnatural\partightenfactor0

\f0\b\fs28 \cf0 Milestone1 (22/12/2025)
\f1\b0\fs24 \
\

\f0\b 1. Jelaskan pin apa saja yang ada di Servo!
\f1\b0 \
Terdapat 3 pin, yaitu:\
- Daya (VCC): berfungsi memasok sejumlah tegangan yang diperlukan agar motor servo bergerak. Terhubung dengan sumber daya positif pada mikon. Kabel warna merah\
- Ground (GND): Sebagai jalur kembali arus listrik (titik referensi 0V). Terhubung ke GND pada mikon. Kabel warna coklat atau hitam.\
- Sinyal (PWM): berfungsi menerima sinyal berupa Pulse Width Modulation dari mikon yang menentukan sudut putar servo. Terhubung pada pin digital pada mikon. Durasi pulse biasanya ada di rentang 1-2ms dan pulse 1,5ms umumnya mewakili posisi netral. Kabel warna oren, kuning, atau putih.\
\

\f0\b 2. ESP32 menggunakan baudrate 115200, jelaskan apa itu baudrate? Dan apakah di program python juga harus 115200?
\f1\b0 \
Baud rate adalah kecepatan transfer data dalam komunikasi serial, menunjukkan berapa banyak perubahan sinyal (bit data) yang dapat dikirim per detik. Dalam konteks port serial, 115200 baud berarti port serialnya mampu mentransfer maksimal 115200 bit per sekon. Semakin tinggi baud rate, semakin cepat pula data dikirim. Baud rate di Python tidak harus 115200, yang penting nilainya sama dengan baud rate yang diatur pada mikon melalui Serial.begin (perangkat penerima dan pengirim harus sama baud rate-nya).\
\

\f0\b 3. Jelaskan alur program yang telah dibuat!
\f1\b0 \
- Servo biasa: diawali dengan memanggil library ESP32Servo dan membuat objek servo, lalu menentukan pin kontrol servo (13). Pada fungsi setup(), servo dihubungkan ke ponnya agar siap dikendalikan. Pada fungsi loop(), perulangan for menggerakkan servo secara bertahap dari sudut 0 hingga 179 derajat dengan jeda 10 milisekon per derajatnya, kemudian program akan mengulang kembali dari awal setelah mencapai sudut maksimum.\
- Servo dengan Python: pada fungsi setup() di Arduino IDE, ESP32 menginisialisasi komunikasi serial dengan baud rate 115200 dan menghubungkan servo ke pin 13. Pada fungsi loop(), ESP32 membaca nilai sudut yang dari komputer menggunakan Serial.parseInt() jika memang ada data yang masuk. Di Python, program membuka koneksi serial ke ESP32 terlebih dulu, lalu meminta user memasukkan sudut gerakan servo yang diinginkan. Nilai sudut tersebut dikirim sebagai data teks melalui port serial ke ESP32 sehingga user dapat mengendalikan pergerakan servo.\
\
{\field{\*\fldinst{HYPERLINK "https://www-instructables-com.translate.goog/Interfacing-Servo-Motor-With-Arduino/?_x_tr_sl=en&_x_tr_tl=id&_x_tr_hl=id&_x_tr_pto=rq"}}{\fldrslt https://www-instructables-com/Interfacing-Servo-Motor-With-Arduino/?_x_tr_sl=en&_x_tr_tl=id&_x_tr_hl=id&_x_tr_pto=rq}}\
{\field{\*\fldinst{HYPERLINK "https://www-setra-com.translate.goog/blog/what-is-baud-rate-and-what-cable-length-is-required-1?_x_tr_sl=en&_x_tr_tl=id&_x_tr_hl=id&_x_tr_pto=sge"}}{\fldrslt https://www-setra-com/blog/what-is-baud-rate-and-what-cable-length-is-required-1?_x_tr_sl=en&_x_tr_tl=id&_x_tr_hl=id&_x_tr_pto=sge}}\
}