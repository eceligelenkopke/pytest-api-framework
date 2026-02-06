from setuptools import setup, find_packages

setup(name='grrmapitest',
      version='1.0', #büyük projede versiyon check önemli
      description='Practice API testing',
      author='Alperen Acar',
      author_email='alperenacar123@gmail.com',
      url='https://georgerrmartin.com',
      packages= find_packages(),  #çok çok çok önemli
      zip_safe=False,
      install_requires=[
                        "PyMySQL==1.1.2",
                        "pytest==9.0.2",
                        "pytest-html==4.1.1",
                        "pytest-metadata==3.1.1",
                        "requests==2.32.5",
                        "requests-oauthlib==2.0.0",
                        "WooCommerce==3.0.0",

      ]
      )