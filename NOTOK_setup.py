from setuptools import setup,find_packages
setup(name='PythonBDDSeleniumMengkome',
      version='1.0',
      description='Python BDD Selenium run on MengKome site',
      author='cromox1',
      author_email='xixa01@yahoo.co.uk',
      url='http://mengkome.pythonanywhere.com/',
      # packages=find_packages()
      packages=[
            'BDDCommon',
            'BDDCommon.CommonFuncs',
            'BDDCommon.CommonSteps',
            'BDDCommon.CommonConfigs'
      ],
     )