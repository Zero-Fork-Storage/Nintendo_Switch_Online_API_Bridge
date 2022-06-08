import re

from setuptools import setup
from setuptools import find_packages


version = ''

with open('nso_bridge/__init__.py') as f:
    version = re.search(r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]', f.read(), re.MULTILINE).group(1)

if not version:
    raise RuntimeError('version is not set')


readme = ''
with open('README.md') as f:
    readme = f.read()

setup(
    name='nso_bridge',
    version=version,
    description='NINTENDO SWITCH ONLINE API BRIDGE',
    long_description=readme,
    long_description_content_type="text/markdown",
    license='MIT',
    include_package_data=True,
    author='zeroday0619',
    author_email='zeroday0619_dev@outlook.com',
    url='https://github.com/zeroday0619/Nintendo_Switch_Online_API_Bridge',
    packages=find_packages(exclude=['.vscode', '.idea', '.github', 'tests']),
    install_requires=[
        "requests", "keyring", "bs4"
    ],
    keywords=[
        "Nintendo", 
        "Nintendo Switch", 
        "Nintendo Switch Online",
        "Nintendo Switch Online API",
    ],
    python_requires='>=3',
    zip_safe=False,
    classifiers=[
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
    ]
)