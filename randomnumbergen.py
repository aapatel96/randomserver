##random number generator server


import random, string, pymongo, telegram, os, boto3

from flask import Flask, request, jsonify

##bot = telegram.Bot('395089971:AAGdmNnerGxByQZqhjen2hAGIZ2CBW-WcnY')



app = Flask(__name__)

@app.route("/random", methods=['POST'])
def randomword():
   try:
      return jsonify(status='success',string=''.join(random.choice(string.lowercase) for i in range(int(request.form['length']))))
   except:
      return jsonify(status='failed',error="Please pass numbers only")



if __name__ == "__main__":
    PORT = int(os.environ.get('PORT', '5000'))

    app.run(
        host="0.0.0.0",
        port=PORT
    )