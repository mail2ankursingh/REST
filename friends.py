from flask import Flask, request, Response
from flask_restful import Resource, Api
import pprint

app = Flask(__name__)
api = Api(app)

db = {'ankur':{'city':'Fremont', 'dob':'Aug 7'}, 'ujjval':{'city':'Sunnyvale', 'dob':'Jul 5'}}
class friendBase(Resource):
   def get(self):
      return {'names': list(db.keys())}
   
class friendInfo(Resource):
   def get(self,friendName):
      return {friendName : db[friendName]}
   def put(self, friendName):
#      str = pprint.pformat(request.environ, depth=5)
#      return Response(str, mimetype="text/text")
      key = str(list(request.form.keys())[0])
      val = str(list(request.form.values())[0])
      db[friendName][key] = val

api.add_resource(friendBase, '/')
api.add_resource(friendInfo, '/<string:friendName>')

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
