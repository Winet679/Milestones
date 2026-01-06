from setuptools import find_packages, setup
from glob import glob
import os

package_name = 'arm_example'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),

        (os.path.join('share', package_name, 'urdf'), glob('urdf/*')),
        (os.path.join('share', package_name, 'launch'), glob('launch/*')),
        (os.path.join('share', package_name, 'config'), glob('config/*')),
        # supaya 3 dir tsb masuk ke package share (~/ros2_ws/install/arm_example/share/arm_example)
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='winet',
    maintainer_email='winet@todo.todo',
    description='TODO: Package description',
    license='Apache-2.0',
    extras_require={
        'test': [
            'pytest',
        ],
    },
    entry_points={
        'console_scripts': [
        ],
    },
)
