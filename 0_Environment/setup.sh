#!/usr/bin/env bash

echo "start setup"

# environment
export ANACONDA_VERSION=4.4.0

# homebrew
echo "checking homebrew..."
if [ ! `which brew` ]; then
    echo "install homebrew"
    /usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
fi
echo "OK"
echo "update homebrew"
brew update

# pyenv
echo "checking pyenv..."
brew list pyenv
if [ "$?" -ne 0 ]; then
    echo "install pyenv"
    brew install pyenv
    echo "add pyenv path"
    echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.bash_profile
    echo 'export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.bash_profile
    echo 'eval "$(pyenv init -)"' >> ~/.bash_profile
    source ~/.bash_profile
fi
echo "OK"

# anaconda
echo "checking anaconda3-"$ANACONDA_VERSION"..."
pyenv which conda
if [ "$?" -ne 0 ]; then
    echo "install anaconda3-"$ANACONDA_VERSION
    pyenv install anaconda3-$ANACONDA_VERSION
    pyenv global anaconda3-$ANACONDA_VERSION
fi
echo "OK"

echo "end setup"
