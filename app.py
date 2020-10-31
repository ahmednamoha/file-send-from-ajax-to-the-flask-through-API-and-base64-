from flask import Flask, request, jsonify
from flask_restful import Api, Resource, reqparse
from werkzeug.datastructures import FileStorage
import json
import base64
from io import BytesIO
from os import path
from pydub import AudioSegment


app = Flask(__name__)
api = Api(app)


class Test(Resource):
    listOfAudioFormat = ['mp3', 'wav', 'ogg', 'mpeg']

    def exten_file_valid(self, file_type):
        file_type = file_type.lower()
        if file_type in self.listOfAudioFormat:
            return True
        else:
            return False

    def get(self):
        return {'hello': 'world'}

    def post(self):
        data = request.get_json(force=True)
        # nmm = data['file'].decode('utf-8')
        # # confile = BytesIO(base64.decodestring(data['file']))
        files = BytesIO(base64.b64decode(data['file']))
        # data = request.json
        language = request.args.get('name')
        # name = data['name']
        dataa = json.loads(request.data)
        # f = json.loads(request.files)
        # files = request.files['file']
        filea = request.form
        # filea = request.files['file']
        # myfile = data['file']
        myfile = data['file']
        # image_string = base64.b64encode(myfile.read())
        print(dataa['name'])
        # print(type(data['file']))
        print("====================================")
        # print(nmm)
        # print(type(confile))
        # confile.save(, 'txt')
        isVlaid = self.exten_file_valid(data['contentType'])
        if isVlaid:
            with open(data['name'], "wb") as f:
                f.write(files.getbuffer())
            nameFile = data['name'].split('.')[-2]
            src = data['name']
            dst = 'Intro_'+nameFile+".wav"
            sound = AudioSegment.from_mp3(src)

            sound.export(dst, format="wav")
            print('the file name is ', dst)
        else:
            print('no think we uplad')
            return {'unesebtibl': "no thing uploaded"}
        # print(data['file'])
        print(isVlaid)
        # confile.decode("utf-8")
        # print(type(confile))

        return {'hello': 'post'}


api.add_resource(Test, '/')


@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers',
                         'Content-Type,Authorization')
    response.headers.add('Access-Control-Allow-Methods',
                         'GET,PUT,POST,DELETE')
    return response


if __name__ == '__main__':
    app.run(debug=True)
