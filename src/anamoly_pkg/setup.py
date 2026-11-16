from setuptools import find_packages, setup

package_name = 'anamoly_pkg'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='vaibhav',
    maintainer_email='vaibhav@todo.todo',
    description='TODO: Package description',
    license='Apache-2.0',
    extras_require={
        'test': [
            'pytest',
        ],
    },
    entry_points={
        'console_scripts': [
            'publisher = anamoly_pkg.publisher_member_function:main',
            'subscriber = anamoly_pkg.subscriber_member_function:main',
        ],
    },
)
