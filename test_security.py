import pytest       #Needed for the unit testing 
from security import Security as Sec
from io import StringIO


#Caesar tests
def test_CaesarEncryptor_String(monkeypatch):
    textInput = 'Normal text'
    userInput = StringIO('24\n')
    monkeypatch.setattr('sys.stdin', userInput)
    encryptedText = Sec().CaesarEncrypt(textInput)
    assert isinstance(encryptedText, str)
def test_CaesarEncryptor_isDifferent(monkeypatch):
    textInput = 'Normal text'
    userInput = StringIO('24\n')
    monkeypatch.setattr('sys.stdin', userInput)
    encryptedText = Sec().CaesarEncrypt(textInput)
    assert textInput != encryptedText

#Decryptor
def test_CaesarDecryptor_String(monkeypatch):
    textInput = 'Encrypted text'
    userInput = StringIO('24\n')
    monkeypatch.setattr('sys.stdin', userInput)
    encryptedText = Sec().CaesarDecrypt(textInput)
    assert isinstance(encryptedText, str)
def test_CaesarDecryptor_isDifferent(monkeypatch):
    textInput = 'Encrypted text'
    userInput = StringIO('24\n')
    monkeypatch.setattr('sys.stdin', userInput)
    encryptedText = Sec().CaesarDecrypt(textInput)
    assert textInput != encryptedText




#Polyalphabetic tests
def test_PolyEncryptor_String(monkeypatch):
    textInput = 'Normal text'
    userInput = StringIO('24\n')
    monkeypatch.setattr('sys.stdin', userInput)
    encryptedText = Sec().PolyEncrypt(textInput)
    assert isinstance(encryptedText, str)
def test_PolyEncryptor_isDifferent(monkeypatch):
    textInput = 'Normal text'
    userInput = StringIO('24\n')
    monkeypatch.setattr('sys.stdin', userInput)
    encryptedText = Sec().PolyEncrypt(textInput)
    assert textInput != encryptedText

#Decryptor
def test_PolyDecryptor_String(monkeypatch):
    textInput = 'Encrypted text'
    userInput = StringIO('24\n')
    monkeypatch.setattr('sys.stdin', userInput)
    encryptedText = Sec().PolyDecrypt(textInput)
    assert isinstance(encryptedText, str)
def test_PolyDecryptor_isDifferent(monkeypatch):
    textInput = 'Encrypted text'
    userInput = StringIO('24\n')
    monkeypatch.setattr('sys.stdin', userInput)
    encryptedText = Sec().PolyDecrypt(textInput)
    assert textInput != encryptedText
