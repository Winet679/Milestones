# Serba-Serbi Kinematics

Milestone ini mencakup forward-inverse kinematics arm berbentuk tabung (Tabung 2D) dan dummy leg Loky.

### Pengertian
1. FK: proses komputasional dalam menentukan **posisi akhir end-effector** berdasarkan sudut `joint robot`, `panjang link`, dan `konfigurasi` yang diketahui.
2. IK: proses mengkalkulasi **sudut/posisi joint** yang diperlukan agar end-effector dapat mencapai titik yang diinginkan.
3. Degree of Freedom: jumlah gerakan independen yang dapat dilakukan oleh suatu komponen robot, seperti lengan atau manipulator.

### Rumus
Pergerakan sendi robot umumnya rotasional ataupun linear (translasi), jadi perlu diingat:
- Rotasi
  <img width="181" height="214" alt="Rumus rotasi" src="https://github.com/user-attachments/assets/179096cb-540b-4b57-985b-8d319b84daa0" />
- Translasi
- **Homogeneus Transformation Matrix:** matriks yang menggabungkan rotasi dan translasi 3D. Matriks ini menggunakan koordinat homogen (dengan menambahkan koma 1) untuk memungkinkan translasi dan rotasi digabungkan menjadi satu perkalian matriks, sehingga menyederhanakan FK dalam robotika. 
