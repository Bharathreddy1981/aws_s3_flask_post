from flask import Flask,jsonify,request
import aws_s3_image,aws_get


aws_flask = Flask(__name__)

@aws_flask.route("/mountain", methods=["POST"])
def gun():
    jsondata = request.get_json()
    final = aws_s3_image.cat(jsondata)
    return jsonify(final)



@aws_flask.route("/all/<string:name>", methods=["GET"])
def all(name):
    bha=aws_get.mat(name)
    return jsonify(bha)



if __name__=="__main__":
    aws_flask.run(host='0.0.0.0')
