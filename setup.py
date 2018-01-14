from setuptools import find_packages
from setuptools import setup


setup(
    name='pre_commit_hooks',
    description='Some out-of-the-box hooks for pre-commit.',
    url='https://github.com/dzhwinter/pre-commit-hooks',
    version='1.2.0',

    author='dzhwinter',
    author_email='dzhwinter@gmail.com',

    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
    ],

    packages=find_packages(exclude=('tests*')),
    install_requires=[
        # quickfix to prevent pycodestyle conflicts
        'flake8!=2.5.3',
        'autopep8>=1.3',
        'pyyaml',
        'six',
    ],
    entry_points={
        'console_scripts': [
            'copyright_checker = pre_commit_hooks.copyright_checker:main',
        ],
    },
)
