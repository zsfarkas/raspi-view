sudo python3 -m pip install --upgrade pip setuptools wheel
sudo python3 -m pip install tqdm
sudo python3 -m pip install --user --upgrade twine

python3 setup.py bdist_wheel

pip3 install dist/raspi_view-0.2-py3-none-any.whl

# do not forget to set up your .pypirc file
python3 -m twine upload dist/*
# or use
# sudo /root/.local/bin/twine upload dist/*