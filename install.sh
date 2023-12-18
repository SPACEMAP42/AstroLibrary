pip3 uninstall -y astrolibrary
python setup.py bdist_wheel
pip3 install ./dist/astrolibrary-0.1.6-py3-none-any.whl
