from flask import Flask, jsonify, render_template
import rethinkdb as r

app = Flask(__name__)

@app.route('/')
def index():
	r.connect( "localhost", 28015).repl()
	cosa = r.table('geo').get(3)['location'].to_geojson().run()
	print cosa
	return jsonify(**cosa)

@app.route('/home')
def home():
	return render_template('index.html')

if __name__ == "__main__":
	app.run(debug=True, host="192.168.0.112")