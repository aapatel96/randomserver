##random number generator server


import random, string, pymongo, telegram, os, codecs

from flask import Flask, request, jsonify

import sys 

reload(sys)  
sys.setdefaultencoding('utf8')

bot = telegram.Bot('395089971:AAGdmNnerGxByQZqhjen2hAGIZ2CBW-WcnY')


app = Flask(__name__)

@app.route("/create", methods=['POST'])
def randomword():
   name = request.form['name']
   address = request.form['address']
   passport_number = request.form['passport_number']
   poatemplate = codecs.open('template.txt', encoding='utf-8')

   poatext = poatemplate.read()

   print type(poatext)
   print type(name)
   print type(address)
   print type(passport_number)

   poatext.replace('GRANTORNAME',str(name))
   poatext.replace('GRANTORADDRESS',str(address))
   poatext.replace('GRANTORPASSPORTNUMBER',str(passport_number))

   userfilename = name+'-poa.txt'
   userfile = open(userfilename,'w')
   userfile.write(poatext)
   userfile.close()
   userfile = open(userfilename,'rb')
   bot.send_document(chat_id='89380112',document=userfile)


   try:
      return jsonify(status='success',name=name,address = address)
   except:
      return jsonify(status='failed',error="Please pass numbers only")

##   bot.send_message(chat_id='89380112',text=length)
##   bot.send_message(chat_id='89380112',text=''.join(random.choice(string.lowercase) for i in range(length)))
##   return str(length)
##   return ''.join(random.choice(string.lowercase) for i in range(length))


if __name__ == "__main__":
    PORT = int(os.environ.get('PORT', '5000'))

    app.run(
        host="0.0.0.0",
        port=PORT
    )