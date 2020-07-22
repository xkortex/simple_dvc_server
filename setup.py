import os
from setuptools import find_packages, setup
import versioneer

commands = versioneer.get_cmdclass().copy()

pkgname = 'simple_dvc_server'
packages = find_packages()


setup(
    name=pkgname,
    version=versioneer.get_version(),
    script_name='setup.py',
    python_requires='>3.5',
    zip_safe=True,
    packages=packages,
    install_requires=['RangeHTTPServer', 'loguru'],
    entry_points={
        "console_scripts": [
            "simple-dvc-server=simple_dvc_server.server:main",
        ],
    },
    cmdclass=commands,
)
