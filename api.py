from flask import Flask, jsonify
import wordgen
import random

if __name__ == '__main__':
    wordlist = wordgen.get_test_wordlist()
    model = wordgen.train(wordlist, 3)
    
    app = Flask(__name__)
    app.config['DEBUG'] = True
    
    @app.route('/getword/<', methods = ['GET'])
    def get_human_f():
            return jsonify(wordgen.build(model, random.randint(5, 8)))
        
    app.run()