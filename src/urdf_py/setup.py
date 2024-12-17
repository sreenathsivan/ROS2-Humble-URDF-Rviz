from setuptools import find_packages, setup

package_name = 'urdf_py'


import os
list1=[]
filelist=os.listdir('meshes')
for fichier in filelist[:]: # filelist[:] makes a copy of filelist.
    # if not(fichier.endswith(".stl")):
        
        # filelist.remove(fichier)
    list1.append("meshes/"+fichier)

print(list1)
setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        ('share/' + package_name + '/launch', ['launch/display.launch.py']),
        ('share/' + package_name + '/urdf', ['urdf/model.urdf']),
         ('share/' + package_name + '/meshes', list1),
    
        
     
        
    ],
    
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='user',
    maintainer_email='user@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            
        ],
    },
)
