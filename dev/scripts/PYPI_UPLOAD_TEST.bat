:: this upload script when Anaconda is installed in the user folder.

:: to use twine I had to first set it up
:: conda install twine
:: conda update pip setuptools twine

:: make commands silent
@echo off

:: perform a version increase
python versionIncrease.py

:: navigate to the source folder
cd ../../src/

:: delete old builds
rmdir /S /q _build 2>nul
rmdir /S /q build 2>nul
rmdir /S /q dist 2>nul
rmdir /S /q pyabf.egg-info 2>nul
 
:: create your distribution
echo building distribution with setuptools...
python setup.py --quiet sdist

:: upload to the test server
twine upload --username swharden --repository-url https://test.pypi.org/legacy/ dist/*
explorer https://test.pypi.org/project/pyabf/

:: upload to real server
::echo CONTINUE TO UPLOAD TO REAL PYPI
::twine upload --username swharden --repository-url https://upload.pypi.org/legacy/ dist/*
::explorer https://pypi.org/project/pyabf/

:: delete old builds
rmdir /S /q _build 2>nul
rmdir /S /q build 2>nul
rmdir /S /q dist 2>nul
rmdir /S /q pyabf.egg-info 2>nul

echo COMPLETE
pause