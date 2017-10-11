#!/usr/bin/env bash

echo "start setup"

# environment
#PYTHON_VERSION=3.6.3
ANACONDA_VERSION=5.0.0

# homebrew
## check
echo "checking homebrew..."
if [ ! `which brew` ]; then
    ## install homebrew
    echo "install homebrew"
    /usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
fi
## upgrade
echo "upgrade homebrew"
brew upgrade
## update
echo "update homebrew"
brew update
echo "homebrew OK"

# pyenv
## check
echo "checking pyenv..."
#which pyenv
#if [ "$?" -ne 0 ]; then
if [ ! `which pyenv` ]; then
    ## install pyenv
    echo "install pyenv"
    brew install pyenv
    ## add pyenv path
    echo "add pyenv path"
    echo >> ~/.bash_profile
    echo "# Python" >> ~/.bash_profile
    echo 'export PYENV_ROOT="${HOME}/.pyenv"' >> ~/.bash_profile
    echo 'export PATH="${PYENV_ROOT}/bin:${PATH}"' >> ~/.bash_profile
    echo 'eval "$(pyenv init -)"' >> ~/.bash_profile
    echo >> ~/.bash_profile
    source ~/.bash_profile
fi
echo "pyenv OK"

# python
### check
#echo "checking python..."
#if [[ ! `python -V 2>&1 | grep "Python ${PYTHON_VERSION}"` ]]; then
#    ## install python
#    echo "install python ${PYTHON_VERSION}"
#    ### measures against openssl
#    ### https://github.com/pyenv/pyenv/wiki/Common-build-problems#error-the-python-ssl-extension-was-not-compiled-missing-the-openssl-lib
#    CFLAGS="-I$(brew --prefix openssl)/include" \
#    LDFLAGS="-L$(brew --prefix openssl)/lib" \
#    pyenv install ${PYTHON_VERSION}
#    pyenv rehash
#    pyenv global ${PYTHON_VERSION}
#fi
#echo "python OK"

# anaconda
## chack
echo "checking anaconda3-${ANACONDA_VERSION}..."
if [ ! `pyenv which conda` ]; then
    ## install anaconda
    echo "install anaconda3-${ANACONDA_VERSION}"
    pyenv install anaconda3-${ANACONDA_VERSION}
    pyenv global anaconda3-${ANACONDA_VERSION}
fi
echo "anaconda OK"

echo "end setup"
