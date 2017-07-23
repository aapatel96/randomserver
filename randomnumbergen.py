##random number generator server


import random, string, pymongo, telegram, os

from flask import Flask, request

##bot = telegram.Bot('395089971:AAGdmNnerGxByQZqhjen2hAGIZ2CBW-WcnY')


app = Flask(__name__)

@app.route("/random", methods=['POST'])
def randomword():
   length = request.args.get('length')
   print length
##   bot.send_message(chat_id='89380112',text=length)
##   bot.send_message(chat_id='89380112',text=''.join(random.choice(string.lowercase) for i in range(length)))
   return str(length)
##   return ''.join(random.choice(string.lowercase) for i in range(length))



if __name__ == "__main__":
    PORT = int(os.environ.get('PORT', '5000'))

    app.run(
        host="0.0.0.0",
        port=PORT
    )