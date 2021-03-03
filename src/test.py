# Testing Chromos
# import unittest
from Chromos import Chromos
import pytest

@pytest.fixture
def bare_chromos():
    '''Returns a Chromos instance'''
    return Chromos()

def test_bare_chromos_black(bare_chromos):
    result = bare_chromos.black('Hello!!')
    assert result == '\x1b[1;30mHello!!\x1b[0m'

def test_bare_chromos_red(bare_chromos):
    result = bare_chromos.red('Hello!!')
    assert result == '\x1b[1;31mHello!!\x1b[0m'

def test_bare_chromos_green(bare_chromos):
    result = bare_chromos.green('Hello!!')
    assert result == '\x1b[1;32mHello!!\x1b[0m'
    
def test_bare_chromos_yellow(bare_chromos):
    result = bare_chromos.yellow('Hello!!')
    assert result == '\x1b[1;33mHello!!\x1b[0m'

def test_bare_chromos_blue(bare_chromos):
    result = bare_chromos.blue('Hello!!')
    assert result == '\x1b[1;34mHello!!\x1b[0m'
    
def test_bare_chromos_purple(bare_chromos):
    result = bare_chromos.purple('Hello!!')
    assert result == '\x1b[1;35mHello!!\x1b[0m'

def test_bare_chromos_cyan(bare_chromos):
    result = bare_chromos.cyan('Hello!!')
    assert result == '\x1b[1;36mHello!!\x1b[0m'
    
def test_bare_chromos_white(bare_chromos):
    result = bare_chromos.white('Hello!!')
    assert result == '\x1b[1;37mHello!!\x1b[0m'
