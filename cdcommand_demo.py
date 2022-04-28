import os
import subprocess
import pytest


def test_cd(cmd):
    a = subprocess.run(cmd, shell=True, stdout=subprocess.PIPE, text=True, check=True)
    return a.stdout


def output(test_input):
    output = test_cd(test_input)
    return output


@pytest.mark.parameterize("test_input", ['cd', 'cd -L', 'cd -P'])
def test_abc(test_input):
    output(test_input)
    assert True


@pytest.mark.parameterize("test_input", ['cd /usr/local'])
def test_cd1(test_input):
    output(test_input)
    path = "/usr/local"
    os.chdir(path)


@pytest.mark.parameterize("test_input", ['cd lib'])
def test_cd1(test_input):
    output(test_input)
    cdir = os.getcwd()
    print("Previous_dir", cdir)
    os.chdir('C:/usr/local')
    print("Current_dir", cdir)


@pytest.mark.parameterize("test_input", ['cd ..'])
def test_cd1(test_input):
    os.chdir('..')
    output(test_input)
    assert True


@pytest.mark.parameterize("test_input", ['cd . /usr/local '])
def test_cd1(test_input):
    os.chdir('/usr/local')
    output(test_input)
    assert True

