sudo pip3 install --upgrade pip setuptools wheel
sudo pip3 install tqdm
sudo pip3 install --user --upgrade twine

python3 setup.py bdist_wheel

pip3 install dist/raspi_view-0.1-py3-none-any.whl

# do not forget to set up your .pypirc file
python3 -m twine upload dist/*