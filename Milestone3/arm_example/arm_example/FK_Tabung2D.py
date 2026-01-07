'''
Catatan:
Gerakan arm bersifat 2 dimensi dan berporos pada sumbu y di urdf (nilai y selalu 0 di Rviz).
Maka dari itu, nilai x di sini mewakilkan x dan nilai y di sini mewakilkan z.
'''

import numpy as np

def rotation_y(teta):
    c, s = np.cos(teta), np.sin(teta)
    # menggunakan rotasi thd sumbu z karena hanya sumbu x dan y yang dapat berputar
    return np.array([[c, -s, 0],
                     [s, c, 0],
                     [0, 0, 1]])

def translation_z(length):
    return np.array([[1, 0, 0],      #--> Tx, bernilai 0 
                     [0, 1, length], #--> Ty, karena translasi selalu thd sumbu y
                     [0, 0, 1]])

def forward_kinematics(teta1, teta2, teta3):
    link0 = 9.0
    link1 = 7.0
    link2 = 5.0
    link3 = 3.0

    T0 = translation_z(link0)
    T1 = rotation_y(teta1) @ translation_z(link1)
    T2 = rotation_y(teta2) @ translation_z(link2)
    T3 = rotation_y(teta3) @ translation_z(link3)
    matrix = T0 @ T1 @ T2 @ T3
    x = matrix[0, 2]
    y = matrix[1, 2]
    return x, y

x, y = forward_kinematics(0, 0, 0)
print(f"End effector berada di titik x = {x:.2f} dan y = {y:.2f}")