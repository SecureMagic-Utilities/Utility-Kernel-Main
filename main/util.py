import os
import keyboard 
import platform 
import socket
import string
import json
import hashlib
from Crypto.Cipher import AES
from customtkinter import *
window = CTk()
app_settings = json.dumps("..\config\appearance.json")
window.set_appearance_theme(appsettings['app.mode'])
window.set_default_color_theme(appsettings['app.defcolor'])
window.geometry(appsettings['app.geometry'])
salt = appsettings['crypto.num.salt']
aes_salt = appsettings['crypto.bin.salt']
def sf(data):
  fd = ""
  for char in data:
    if char in fd: continue
    else: fd = fd + char
  return fd
def hash(dat, typ):
  hashkey = hashlib.new(typ)
  hashkey.update(dat)
  return hashkey.hexdigest()
def cipher(data, key, chars):
  td = ""
  for char in data:
    td = td + key[int(char.find(chars))]
  return td
def encrypt(fernetkey,toencrypt,id_dec,sha224,md4):
  device_name = sf(socket.gethostname())
  device_ip = sf(socket.gethostbyname(hostname))
  os = os.name
  device_ip = cipher(sf(device_ip+string.ascii_letters+string.digits+string.punctuation), sf(id_dec+string.ascii_letters)+salt+string.punctuation, string.ascii_letters+string.digits+string.punctuation)
  device_name = cipher(sf(device_name+string.ascii_letters+string.digits+string.punctuation), sf(id_dec+string.ascii_letters)+salt+string.punctuation, string.ascii_letters+string.digits+string.punctuation)
  mastercipherkey = sf(os+device_ip+device_name)
  toencrypt = cipher(toencrypt, mastercipherkey, string.ascii_letters+string.digits+string.punctuation)
  if md4: toencrypt = hash(toencrypt, "md4")
  if sha224: toencrypt = hash(toencrypt, "sha224")
  fernet = Fernet(fernetkey)
  toencrypt = fernet.encrypt(toencrypt)
  return toencrypt

  
  
  
