##random number generator server


import random, string, pymongo, telegram, os, boto3

from flask import Flask, request, jsonify

##bot = telegram.Bot('395089971:AAGdmNnerGxByQZqhjen2hAGIZ2CBW-WcnY')

client = pymongo.MongoClient(os.environ['MONGODB_URI'])
db = client.get_default_database()
active = db['active']

app = Flask(__name__)

@app.route("/random", methods=['POST'])
def randomword():
   name = request.form['name']
##   try:
   randomstring = ''.join(random.choice(string.lowercase) for i in range(int(request.form['length'])))
   isInDB = True
   while isInDB == True:
     stringInDBactive.find_one({'string':randomstring,'name':name})
     if stringInDB == None:
         active.insert_one({'string':randomstring,'name':name})
         break
     else:
         string = ''.join(random.choice(string.lowercase) for i in range(int(request.form['length'])))
   return jsonify(status='success',string=string,name=name)
##   except:
##      return jsonify(status='failed',error="Please pass numbers only")



if __name__ == "__main__":
    PORT = int(os.environ.get('PORT', '5000'))

    app.run(
        host="0.0.0.0",
        port=PORT
    )
