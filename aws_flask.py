from flask import Flask,jsonify
import aws_s3_image


aws_flask = Flask(__name__)





@aws_flask.route("/mountain", methods=["POST"])
def gun():
    #jsondata = request.get_json()
    final = aws_s3_image.cat()
    return jsonify(final)




if __name__=="__main__":
    aws_flask.run(debug=True)
