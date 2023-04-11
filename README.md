# AstroLibrary
<center><img src="./logo_spacemap.png"></center>  

### Install poetry
`poetry` must be installed before building the package.
```terminal
pip install poetry
```

### How to build package and use AstroLibrary
You can use poetry to make it a distributable file.
```terminal
poetry build
```
After receiving git clone, the result of executing the above command in the directory is as follows.
```terminal
Building astrolibrary (0.1.0)
  - Building sdist
  - Built astrolibrary-0.1.0.tar.gz
  - Building wheel
  - Built astrolibrary-0.1.0-py3-none-any.whl
```
If you go to the `dist` folder, you will find the following files:
```terminal
astrolibrary-0.1.0.tar.gz
astrolibrary-0.1.0-py3-none-any.whl
```
After that, you can install the package in your preferred Python environment and then use the library.  

#### install example
```terminal
pip3 install ./dist/astrolibrary-0.1.0-py3-none.any.whl
```
The result of running the above code is:
```terminal
Processing ./dist/astrolibrary-0.1.0-py3-none-any.whl
Requirement already satisfied: black<24.0.0,>=23.3.0 in /Users/spacemap/Library/Caches/pypoetry/virtualenvs/astrolibrary-SERaLF6_-py3.8/lib/python3.8/site-packages (from astrolibrary==0.1.0) (23.3.0)
Requirement already satisfied: requests<3.0.0,>=2.28.2 in /Users/spacemap/Library/Caches/pypoetry/virtualenvs/astrolibrary-SERaLF6_-py3.8/lib/python3.8/site-packages (from astrolibrary==0.1.0) (2.28.2)
Requirement already satisfied: configparser<6.0.0,>=5.3.0 in /Users/spacemap/Library/Caches/pypoetry/virtualenvs/astrolibrary-SERaLF6_-py3.8/lib/python3.8/site-packages (from astrolibrary==0.1.0) (5.3.0)
Requirement already satisfied: typing-extensions>=3.10.0.0 in /Users/spacemap/Library/Caches/pypoetry/virtualenvs/astrolibrary-SERaLF6_-py3.8/lib/python3.8/site-packages (from black<24.0.0,>=23.3.0->astrolibrary==0.1.0) (4.5.0)
Requirement already satisfied: packaging>=22.0 in /Users/spacemap/Library/Caches/pypoetry/virtualenvs/astrolibrary-SERaLF6_-py3.8/lib/python3.8/site-packages (from black<24.0.0,>=23.3.0->astrolibrary==0.1.0) (23.0)
Requirement already satisfied: pathspec>=0.9.0 in /Users/spacemap/Library/Caches/pypoetry/virtualenvs/astrolibrary-SERaLF6_-py3.8/lib/python3.8/site-packages (from black<24.0.0,>=23.3.0->astrolibrary==0.1.0) (0.11.1)
Requirement already satisfied: click>=8.0.0 in /Users/spacemap/Library/Caches/pypoetry/virtualenvs/astrolibrary-SERaLF6_-py3.8/lib/python3.8/site-packages (from black<24.0.0,>=23.3.0->astrolibrary==0.1.0) (8.1.3)
Requirement already satisfied: platformdirs>=2 in /Users/spacemap/Library/Caches/pypoetry/virtualenvs/astrolibrary-SERaLF6_-py3.8/lib/python3.8/site-packages (from black<24.0.0,>=23.3.0->astrolibrary==0.1.0) (3.2.0)
Requirement already satisfied: tomli>=1.1.0 in /Users/spacemap/Library/Caches/pypoetry/virtualenvs/astrolibrary-SERaLF6_-py3.8/lib/python3.8/site-packages (from black<24.0.0,>=23.3.0->astrolibrary==0.1.0) (2.0.1)
Requirement already satisfied: mypy-extensions>=0.4.3 in /Users/spacemap/Library/Caches/pypoetry/virtualenvs/astrolibrary-SERaLF6_-py3.8/lib/python3.8/site-packages (from black<24.0.0,>=23.3.0->astrolibrary==0.1.0) (1.0.0)
Requirement already satisfied: idna<4,>=2.5 in /Users/spacemap/Library/Caches/pypoetry/virtualenvs/astrolibrary-SERaLF6_-py3.8/lib/python3.8/site-packages (from requests<3.0.0,>=2.28.2->astrolibrary==0.1.0) (3.4)
Requirement already satisfied: certifi>=2017.4.17 in /Users/spacemap/Library/Caches/pypoetry/virtualenvs/astrolibrary-SERaLF6_-py3.8/lib/python3.8/site-packages (from requests<3.0.0,>=2.28.2->astrolibrary==0.1.0) (2022.12.7)
Requirement already satisfied: charset-normalizer<4,>=2 in /Users/spacemap/Library/Caches/pypoetry/virtualenvs/astrolibrary-SERaLF6_-py3.8/lib/python3.8/site-packages (from requests<3.0.0,>=2.28.2->astrolibrary==0.1.0) (3.1.0)
Requirement already satisfied: urllib3<1.27,>=1.21.1 in /Users/spacemap/Library/Caches/pypoetry/virtualenvs/astrolibrary-SERaLF6_-py3.8/lib/python3.8/site-packages (from requests<3.0.0,>=2.28.2->astrolibrary==0.1.0) (1.26.15)
Installing collected packages: astrolibrary
Successfully installed astrolibrary-0.1.0
```
Now that we have finished installing astrolibrary, let's run the example code.
