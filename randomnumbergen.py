##random number generator server


import random, string, pymongo, Flask
import telegram

bot = telegram.Bot('395089971:AAGdmNnerGxByQZqhjen2hAGIZ2CBW-WcnY')


app = Flask(__name__)

@app.route("/random", methods=['POST'])
def randomword(length):
   length = request.args.get('length')
   bot.send_message(chat_id='89380112',text=length)
   return ''.join(random.choice(string.lowercase) for i in range(length))