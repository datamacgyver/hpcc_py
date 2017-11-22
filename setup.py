from setuptools import setup

setup(
    name='hpcc_py',
    version='0.1',
    scripts=['getHPCCfile', 'getECLquery']
)

setup(name='hpcc_py',
	  version='0.1',
      description='Download THOR files',
      url='http://github.com/mansfieldbitter/hpcc_py',
      author='Rob Mansfield',
      author_email='mansfieldbitter@gmail.com',
      license='GNU GPLv3',
      packages=['funniest'],
      zip_safe=False,
      install_requires=[
          'pandas', 'json'
      ]
	  )