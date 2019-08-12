from setuptools import setup

setup(name='instagram',
      version='0.0.1',
      description='Download pictures from INSTAGRAM',
      author='Subhrajit Prusty',
      url='https://github.com/SubhrajitPrusty/instagram-download/',
      license='MIT',
      install_requires=['splinter', 'bs4', 'click'],
      py_modules=['instagram'],
      entry_points="""
	  [console_scripts]
		instagram=instagram:insta
		"""
      )
