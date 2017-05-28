from setuptools import setup

def readme():
    with open('README.rst') as f:
        return f.read()


setup(name='nude-finder',
      version='0.1',
      description='A command line tool to recursively search images with nudity.',
      long_description=readme(),
      classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2.7',
      ],
      keywords='nude nudes image photos finder find search locate file folder',
      url='http://github.com/paladini/nude-finder',
      author='Fernando Paladini',
      author_email='fnpaladini@gmail.com',
      license='MIT',
      packages=['finder'],
      install_requires=[
          'Pillow',
          'nudepy',
      ],
      test_suite='nose.collector',
      tests_require=['nose', 'nose-cover3'],
      entry_points={
          'console_scripts': ['nude-finder=finder.command_line:main'],
      },
      include_package_data=True,
      zip_safe=False)
