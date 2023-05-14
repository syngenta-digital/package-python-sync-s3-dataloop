from setuptools import setup, find_packages
from os import path

this_directory = path.abspath(path.dirname(__file__))

readme_file = open("README.md")
long_description= "\n".join(readme_file.readlines())
readme_file.close()

setup(
    name='sync_s3_and_dataloop',
    version='0.0.1',
    description='Python library to synchronize s3 buckets and Dataloop datasets',
    keywords='dataloop, bucket, s3, datasets',
    url='https://github.com/syngenta-digital/research-python-ml-automation-process',
    packages=find_packages(exclude=['tests', 'docs*', 'experiments*', 'scripts*']),
    include_package_data=True,
    license='MIT',
    zip_safe=True,
    package_data={
        'sync_s3_and_dataloop': [
            'README.md'
        ],
    },
    install_requires=[
        'boto3',
        'dtlpy',
        'argparse'
    ],
    entry_points='''
        [console_scripts]
            sync_s3_and_dataloop = sync_s3_and_dataloop.__main__:main
            ''',
)
