from setuptools import setup, find_packages


with open('README.md', 'rt', encoding='utf-8') as fh:
    long_description = fh.read()

setup(
    name='simplex',
    version='0.0.2',
    author='shosatojp',
    author_email='me@shosato.jp',
    description='simplex method',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/shosatojp/simplex',
    packages=find_packages(),  # find package `simplex`
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
    ],
    python_requires='>=3.6',
    install_requires=[
        'numpy',
        'simpy',
        'pandas',
    ],
)
