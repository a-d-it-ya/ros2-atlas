import os
from glob import glob
from setuptools import setup

package_name = 'atlas_monitor'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name, 'launch'),
            glob('launch/*.launch.py')),
        (os.path.join('share', package_name, 'urdf'),
            glob('urdf/*.urdf')),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='aditya',
    maintainer_email='aditya@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'system_monitor = atlas_monitor.system_monitor:main',
            'system_listener = atlas_monitor.system_listener:main',
            'health_service = atlas_monitor.health_service:main',
            'diagnostic_action = atlas_monitor.diagnostic_action:main',
            'tf2_broadcaster = atlas_monitor.tf2_broadcaster:main',
        ],
    },
)