from distutils.core import setup
setup(
  name = 'ascii',
  packages = ['ascii'], # this must be the same as the name above
  version = '0.2',
  description = 'Turns images into ascii art',
  author = 'Michael Kaminsky',
  author_email = 'mkaminsky11@gmail.com',
  url = 'https://github.com/mkaminsky11/ascii', # use the URL to the github repo
  download_url = 'https://github.com/mkaminsky11/ascii/tarball/0.2', # I'll explain this in a second
  keywords = ['ascii', 'image', 'asciiart'], # arbitrary keywords
  classifiers = [],
  install_requires=['Pillow','urllib3']
)