from flask import Flask, request, jsonify
from flask_cors import CORS
from werkzeug.wrappers import response
from bs4 import BeautifulSoup as bs                                                                                   import requests as req
import json,re
app = Flask(__name__)
CORS(app)


@app.route("/")                                                                                                       def index():
    text = {"msg":"hudaxcode rest api"}                                                                                   return jsonify(text)

@app.route("/api/ip")
def ipme():
    url = "https://freeip.me/"
    r   = req.get(url).text
    b   = bs(r,'html.parser')
    find = b.find("div",{"class":"data"}).text
    respon = {"msg":find}
    return jsonify(respon)

@app.route("/api/tiktok")
def tiktok():
    if request.method == "GET":
        arg = request.args
        if arg:
            if "url" in arg:
                nex = arg["url"]
                if nex:
                    url = "https://api.tikmate.app/api/lookup"
                    data= {
                            "url":nex
                        }
                    pos = req.post(url,data=data).json()
                    return jsonify(pos)
    return jsonify({"error": "url yang anda masukan tidak valid"})
   # return  jsonify({"msg":"hudaxcode rest api"})

@app.route("/api/yt")
def yt():
    if request.method == "GET":
        arg = request.args
        if "url" in arg:
            page = arg["url"]
            url  = f"https://noembed.com/embed?url={page}"
            rq   = req.get(url).json()
            vidio= re.findall('src=\"(.*?)\"',str(rq))[0]
            thumb= rq["thumbnail_url"]
            judul= rq["title"]
            text = {
                    "judul":judul,
                    "video":vidio,
                    "thumbnail":thumb
                    }
            return jsonify(text)
        else:
            return jsonify({"message":"url required"})


if __name__ == '__main__':
    app.run(debug=True)
