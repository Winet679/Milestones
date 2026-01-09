QnA
1. Apa itu servo Dynamixel?
Servo Dynamixel merupakan aktuator cerdas "all-in-one" yang dikembangkan oleh Robotis (Korsel). Servo ini mengintegrasikan motor DC, kontrol melalui Dynamixel Protocol (mengendalikan posisi, velocity, torsi, dan masih banyak lagi), hingga jaringan daisy-chain sehingga bisa menghasilkan output yang presisi dalam robotika.
User mengirimkan perintah, kemudian kontroler internalnya akan memanfaatkan feedback dari sensor dan PID control untuk menggerakkan servo sesuai keinginan user. Servo ini umumnya digunakan untuk robot-robot kompleks seperti humanoid.

3. Apa yang membedakan servo Dynamixel dengan servo biasa?
- Desain yang terintegrasi
- Sistem kontrol
- Feedback data
- Daisy-chain network
- Versatile:
  
5. Apa kegunaan U2D2?
U2D2 adalah USB kecil yang berperan menghubungkan PC dengan Dynamixel. U2D2 sebagai konverter komunikasi akan menerjemahkan komunikasi USB dari PC menjadi komunikasi serial, tanpa proses ini Dynamixel tidak akan memahami input yang user berikan.

6. Apa itu URDF?
Unified Robot Description Format adalah **format file** yang berfungsi menjabarkan geometry dan susunan robot di ROS, format penulisannya sama dengan XML.

7. Packages apa saja yang diperlukan untuk memvisualisasikan URDF di Rviz2?
- Rviz2
- robot_state_publisher
- joint_state_publisher
  
9. URDF bisa digunakan untuk simulasi di software apa saja?
- Rviz
- Gazebo
- 
