import pytest
import main

def test_city1():
  assert main.available('Boston') == 1

def test_city2():
  assert main.available('New York') == 1

def test_city3():
  assert main.available('BU') == 0