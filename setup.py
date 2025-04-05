from setuptools import setup, find_packages

setup(
    name='superset-analytics-project',
    version='0.1.0',
    author='Your Name',
    author_email='your.email@example.com',
    description='A project showcasing data analytics capabilities using Apache Superset.',
    packages=find_packages(),
    install_requires=[
        'apache-superset',
        'pandas',
        'sqlalchemy',
        'requests',
        'numpy',
        'matplotlib',
        'flask',
        'flask-cors',
        'flask-sqlalchemy',
        'pytest',
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)