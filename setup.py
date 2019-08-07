from setuptools import setup, find_packages

setup(name='sentinel_api',
      packages=find_packages(),
      include_package_data=True,
      version='0.5.2',
      description='ESA Sentinel Search & Download API',
      classifiers=[
          'Programming Language :: Python',
      ],
      install_requires=['gdal>=1.11.3',
                        'spatialist',
                        'progressbar2',
                        'requests>=2.8.1'],
      url='https://github.com/jonas-eberle/esa_sentinel.git',
      author='Jonas Eberle, John Truckenbrodt, Felix Cremer',
      author_email='jonas.eberle@uni-jena.de, john.truckenbrodt@uni-jena.de, felix.cremer@uni-jena.de',
      license='MIT',
      zip_safe=False)
