from setuptools import setup, find_packages


setup(name='clean_folder',
      version='0.0.1',
      packages=find_packages(),
      author='GO_IT',
      description="clean folder from trash",
      entry_point={
          'console_scripts': ['clean-folder = clean_folder.clean:main']
      }      
)  