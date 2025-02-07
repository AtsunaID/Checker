from flask import Flask, request, jsonify
import instaloader

app = Flask(__name__)
loader = instaloader.Instaloader()

@app.route('/check_account', methods=['GET'])
def check_account():
    username = request.args.get('username')
    if not username:
        return jsonify({"error": "Username is required"}), 400

    try:
        profile = loader.get_profile_from_username(username)
        return jsonify({
            "username": username,
            "status": "live"
        })
    except instaloader.exceptions.ProfileNotExistsException:
        return jsonify({
            "username": username,
            "status": "dead"
        })
    except Exception as e:
        return jsonify({
            "error": str(e)
        }), 500


