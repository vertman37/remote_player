
from flask import Flask, render_template, request, send_from_directory, redirect, url_for, jsonify
import os

from player import Player
player = Player()

app = Flask(__name__)

# Path for uploaded files
UPLOAD_FOLDER = os.path.join('static', 'uploads')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Ensure upload folder exists
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return "No file part", 400
    file = request.files['file']
    if file.filename == '':
        return "No selected file", 400
    if file:
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(filepath)
        return redirect(url_for('play_file', filename=file.filename))

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

@app.route('/play/<filename>')
def play_file(filename):
    filepath = url_for('uploaded_file', filename=filename)
    return render_template('play.html', filepath=filepath, filename=filename)

@app.route('/play/<filename>', methods=['POST'])
def control_file(filename):
    action = request.json.get('action')
    if action in ['play', 'pause', 'rewind']:
        # print(f"Action received for {filename}: {action}")
        fpath = os.path.join(app.config['UPLOAD_FOLDER'],filename)
        if action == 'play':
            player.load(fpath)
            player.stop()
            player.play()
        elif action == 'pause':
            player.stop()
        
        return jsonify({"status": "success", "action": action})
    return jsonify({"status": "error", "message": "Invalid action"}), 400


@app.route('/set_volume', methods=['POST'])
def set_volume():
    volume = float(request.json.get('volume'))
    player.set_volume(volume)
    return jsonify(status="Volume set", volume=volume)



if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
