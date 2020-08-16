from flask import Flask
from flask import render_template, request
from modules import affine
from modules import atbash
from modules import baconian
from modules import caesar
from modules import polybius_square
from modules import rot13
from modules import vigenere
from modules import xor

application = Flask(__name__)


def removeAllSpecialCharactersIncludingSpaces(text):
  return ''.join(a for a in text if a.isalnum())


def removeAllSpecialCharactersExcludingSpaces(text):
  return ''.join(a for a in text if a.isalnum() or a == ' ')


@application.route('/')
@application.route('/home')
def home():
	return render_template('index.html', title='Home', output="")


@application.route('/about-us')
def support():
  return render_template('about.html', title='About Us', output="")


@application.route('/contact-us', methods=['GET', 'POST'])
def contact():
  if request.method == 'POST':
    name = request.form.get('name')
    email = request.form.get('email')
    msg = request.form.get('comment')
    #send mail
    print(name, email, msg)
    return render_template('index.html', title='Home', output="")
  return render_template('contact.html', title='Contact Us', output="")


@application.route('/layout')
def layout():
  return render_template('layout.html', title='Layout')


@application.route('/cipher')
def cipher():
  return render_template('cipher.html', title='Cipher')


@application.route('/affine', methods=['GET', 'POST'])
def Affine():
  msg = ''
  output = ''
  set1 = 'opt1'
  set2 = 'opt4'
  a = '1'
  b = '0'
  if request.method == 'POST':
    task = request.form.get('task')
    msg = request.form.get('original-text')
    set1 = request.form.get('set1')
    set2 = request.form.get('set2')
    a = request.form.get('value-of-a')
    b = request.form.get('value-of-b')
    if task == 'encrypt':
      output = affine.encrypt(msg, int(a), int(b))
      if set1 == 'opt1':
        pass
      elif set1 == 'opt2':
        output = removeAllSpecialCharactersExcludingSpaces(output)
      elif set1 == 'opt3':
        output = removeAllSpecialCharactersIncludingSpaces(output)
    elif task == 'decrypt':
      output = affine.decrypt(msg, int(a), int(b))
      if set1 == 'opt1':
        pass
      elif set1 == 'opt2':
        output = removeAllSpecialCharactersExcludingSpaces(output)
      elif set1 == 'opt3':
        output = removeAllSpecialCharactersIncludingSpaces(output)
    if set2 == 'opt4':
        pass
    elif set2 == 'opt5':
      output = output.upper()
    elif set2 == 'opt6':
      output = output.lower()
  return render_template('affine.html', title='Affine Cipher', msg=msg, output=output, set1=set1, set2=set2, a=a, b=b)


@application.route('/atbash', methods=['GET', 'POST'])
def Atbash():
  msg = ''
  output = ''
  set1 = 'opt1'
  set2 = 'opt4'
  if request.method == 'POST':
    task = request.form.get('task')
    msg = request.form.get('original-text')
    set1 = request.form.get('set1')
    set2 = request.form.get('set2')
    if task == 'encrypt':
      output = atbash.encrypt(msg)
      if set1 == 'opt1':
        pass
      elif set1 == 'opt2':
        output = removeAllSpecialCharactersExcludingSpaces(output)
      elif set1 == 'opt3':
        output = removeAllSpecialCharactersIncludingSpaces(output)
    elif task == 'decrypt':
      output = atbash.decrypt(msg)
      if set1 == 'opt1':
        pass
      elif set1 == 'opt2':
        output = removeAllSpecialCharactersExcludingSpaces(output)
      elif set1 == 'opt3':
        output = removeAllSpecialCharactersIncludingSpaces(output)
    if set2 == 'opt4':
        pass
    elif set2 == 'opt5':
      output = output.upper()
    elif set2 == 'opt6':
      output = output.lower()
  return render_template('atbash.html', title='Atbash Cipher', msg=msg, output=output, set1=set1, set2=set2)


@application.route("/baconian", methods=['GET', 'POST'])
def Baconian():
  msg = ''
  output = ''
  set1 = 'opt1'
  set2 = 'opt4'
  if request.method == 'POST':
    task = request.form.get('task')
    msg = request.form.get('original-text')
    set1 = request.form.get('set1')
    set2 = request.form.get('set2')
    try:
      if task == 'encrypt':
        output = baconian.encrypt(msg)
        if set1 == 'opt1':
          pass
        elif set1 == 'opt2':
          output = removeAllSpecialCharactersExcludingSpaces(output)
        elif set1 == 'opt3':
          output = removeAllSpecialCharactersIncludingSpaces(output)
      elif task == 'decrypt':
        output = baconian.decrypt(msg)
        if set1 == 'opt1':
          pass
        elif set1 == 'opt2':
          output = removeAllSpecialCharactersExcludingSpaces(output)
        elif set1 == 'opt3':
          output = removeAllSpecialCharactersIncludingSpaces(output)
      if set2 == 'opt4':
          pass
      elif set2 == 'opt5':
        output = output.upper()
      elif set2 == 'opt6':
        output = output.lower()
    except:
      return render_template('baconian.html', title='Baconian Cipher', msg=msg, output=output, set1=set1, set2=set2, disp=True)
  return render_template('baconian.html', title='Baconian Cipher', msg=msg, output=output, set1=set1, set2=set2, disp=False)


@application.route('/caesar', methods=['GET', 'POST'])
def Caesar():
  msg = ''
  output = ''
  set1 = 'opt1'
  set2 = 'opt4'
  shift = '0'
  if request.method == 'POST':
    task = request.form.get('task')
    msg = request.form.get('original-text')
    set1 = request.form.get('set1')
    set2 = request.form.get('set2')
    shift = request.form.get('shift')
    if task == 'encrypt':
      output = caesar.encrypt(msg,int(shift))
      if set1 == 'opt1':
        pass
      elif set1 == 'opt2':
        output = removeAllSpecialCharactersExcludingSpaces(output)
      elif set1 == 'opt3':
        output = removeAllSpecialCharactersIncludingSpaces(output)
    elif task == 'decrypt':
      output = caesar.decrypt(msg,int(shift))
      if set1 == 'opt1':
        pass
      elif set1 == 'opt2' :
        output = removeAllSpecialCharactersExcludingSpaces(output)
      elif set1 == 'opt3':
        output = removeAllSpecialCharactersIncludingSpaces(output)
    if set2 == 'opt4':
        pass
    elif set2 == 'opt5':
      output = output.upper()
    elif set2 == 'opt6':
      output = output.lower()
  return render_template('caesar.html', title='Caesar Cipher', msg=msg, output=output, set1=set1, set2=set2, shift=shift)


@application.route("/rot13", methods=['GET', 'POST'])
def Rot13():
  msg = ''
  output = ''
  set1 = 'opt1'
  set2 = 'opt4'
  if request.method == 'POST':
    task = request.form.get('task')
    msg = request.form.get('original-text')
    set1 = request.form.get('set1')
    set2 = request.form.get('set2')
    if task == 'encrypt':
      output = rot13.encrypt(msg)
      if set1 == 'opt1':
        pass
      elif set1 == 'opt2':
        output = removeAllSpecialCharactersExcludingSpaces(output)
      elif set1 == 'opt3':
        output = removeAllSpecialCharactersIncludingSpaces(output)
    elif task == 'decrypt':
      output = rot13.decrypt(msg)
      if set1 == 'opt1':
        pass
      elif set1 == 'opt2' :
        output = removeAllSpecialCharactersExcludingSpaces(output)
      elif set1 == 'opt3':
        output = removeAllSpecialCharactersIncludingSpaces(output)
    if set2 == 'opt4':
        pass
    elif set2 == 'opt5':
      output = output.upper()
    elif set2 == 'opt6':
      output = output.lower()
  return render_template('rot13.html', title='Rot13 Cipher', msg=msg, output=output, set1=set1, set2=set2)


# @application.route("/polybius_square")
# def Polybius_Square():
#   msg = ''
#   output = ''
#   set1 = 'opt1'
#   set2 = 'opt4'
#   if request.method == 'POST':
#     task = request.form.get('task')
#     msg = request.form.get('original-text')
#     set1 = request.form.get('set1')
#     set2 = request.form.get('set2')
#     if task == 'encrypt':
#       output = rot13.encrypt(msg)
#       if set1 == 'opt1':
#         pass
#       elif set1 == 'opt2':
#         output = removeAllSpecialCharactersExcludingSpaces(output)
#       elif set1 == 'opt3':
#         output = removeAllSpecialCharactersIncludingSpaces(output)
#     elif task == 'decrypt':
#       output = rot13.decrypt(msg)
#       if set1 == 'opt1':
#         pass
#       elif set1 == 'opt2' :
#         output = removeAllSpecialCharactersExcludingSpaces(output)
#       elif set1 == 'opt3':
#         output = removeAllSpecialCharactersIncludingSpaces(output)
#     if set2 == 'opt4':
#         pass
#     elif set2 == 'opt5':
#       output = output.upper()
#     elif set2 == 'opt6':
#       output = output.lower()
#   return render_template('polybius_square.html', title='Polybius Square Cipher', msg=msg, output=output, set1=set1, set2=set2)


@application.route("/vigenere", methods=['GET', 'POST'])
def Vigenere():
  msg = ''
  output = ''
  set1 = 'opt1'
  set2 = 'opt4'
  key = 'key'
  if request.method == 'POST':
    task = request.form.get('task')
    msg = request.form.get('original-text')
    set1 = request.form.get('set1')
    set2 = request.form.get('set2')
    key = request.form.get('key')
    key = ''.join([i for i in key if i.isupper() or i.islower()])
    if task == 'encrypt':
      output = vigenere.encrypt(msg,key)
      if set1 == 'opt1':
        pass
      elif set1 == 'opt2':
        output = removeAllSpecialCharactersExcludingSpaces(output)
      elif set1 == 'opt3':
        output = removeAllSpecialCharactersIncludingSpaces(output)
    elif task == 'decrypt':
      output = vigenere.decrypt(msg,key)
      if set1 == 'opt1':
        pass
      elif set1 == 'opt2' :
        output = removeAllSpecialCharactersExcludingSpaces(output)
      elif set1 == 'opt3':
        output = removeAllSpecialCharactersIncludingSpaces(output)
    if set2 == 'opt4':
        pass
    elif set2 == 'opt5':
      output = output.upper()
    elif set2 == 'opt6':
      output = output.lower()
  return render_template('vigenere.html', title='Vigenère Cipher', msg=msg, output=output, set1=set1, set2=set2, key=key)

# @application.route("/xor", methods=['GET', 'POST'])
# def Xor():
#   msg = ''
#   output = ''
#   set1 = 'opt1'
#   set2 = 'opt4'
#   key = 'key'
#   if request.method == 'POST':
#     task = request.form.get('task')
#     msg = request.form.get('original-text')
#     set1 = request.form.get('set1')
#     set2 = request.form.get('set2')
#     key = request.form.get('key')
#     if task == 'encrypt':
#       output = xor.encrypt(msg,key)
#       if set1 == 'opt1':
#         pass
#       elif set1 == 'opt2':
#         output = removeAllSpecialCharactersExcludingSpaces(output)
#       elif set1 == 'opt3':
#         output = removeAllSpecialCharactersIncludingSpaces(output)
#     elif task == 'decrypt':
#       output = xor.decrypt(msg,key)
#       if set1 == 'opt1':
#         pass
#       elif set1 == 'opt2' :
#         output = removeAllSpecialCharactersExcludingSpaces(output)
#       elif set1 == 'opt3':
#         output = removeAllSpecialCharactersIncludingSpaces(output)
#     if set2 == 'opt4':
#         pass
#     elif set2 == 'opt5':
#       output = output.upper()
#     elif set2 == 'opt6':
#       output = output.lower()
#   return render_template('xor.html', title='XOR Cipher', msg=msg, output=output, set1=set1, set2=set2, key=key)


if __name__ == "__main__":
  application.run()
