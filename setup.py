from setuptools import setup

setup(name='instagram-download',
      version='0.0.1',
      description='Download pictures from INSTAGRAM',
      author='Sayantan Paul',
      author_email='belikesayantan12@gmail.com',
      url='https://github.com/belikesayantan/CODE-PRIVATE/',
      license='MIT',
      install_requires=['splinter', 'bs4', 'click'],
      py_modules=['instagram1'],
      entry_points="""
	  [console_scripts]
		instagram_download=instagram:insta
		""",
      # copyright="Copyright (C) 2019 SAYANTAN PAUL. All rights reserved."
      )
