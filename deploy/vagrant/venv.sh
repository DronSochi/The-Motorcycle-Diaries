#!/bin/bash

set -e

echo "cd src" >> /home/vagrant/.bashrc
echo "cd src" >> /home/vagrant/.zprofile


echo "Create python virtual environment"
pyvenv-3.5 "/home/vagrant/env"
source "/home/vagrant/env/bin/activate"
echo 'source "/home/vagrant/env/bin/activate"' >> /home/vagrant/.bashrc
echo 'source "/home/vagrant/env/bin/activate"' >> /home/vagrant/.zprofile

# echo "Install python packages"
# cd "/home/vagrant/src"
# pip install -e .
# python setup.py develop
