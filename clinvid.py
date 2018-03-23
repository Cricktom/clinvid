from flask import Flask,request,jsonify
from converter import JsonConverter
import sys,json,logging

logging.basicConfig(level=logging.INFO)
app = Flask(__name__)

#spi to convert string into desired json
@app.route('/clinvid/app/converter', methods=['POST'])
def converter():
    try:
        args = json.dumps(request.json)
        args = json.loads(args)
        str_to_parse = str(args[0])
        converter_obj = JsonConverter(str_to_parse);
        converted_json = converter_obj.parse();
        return jsonify({"profile":converted_json})

    except Exception as e:
        logging.error("In parsing"+str(e))
        return jsonify({"success":False})

if __name__ == "__main__":
    logging.info("Running Holmes Network Bot")
    app.run(host='0.0.0.0',threaded=True, debug=True, port=7080)
