from flask import Flask, request, jsonify
from flask_cors import CORS
from investigation import dns_lookup, whois_lookup, ip_whois_lookup, http_headers

app = Flask(__name__)
CORS(app)  # Enable CORS

@app.route('/api/dns', methods=['POST'])
def dns_api():
    try:
        data = request.get_json()
        if not data or 'domain' not in data:
            return jsonify({"error": "Invalid input. 'domain' is required"}), 400
        domain = data['domain']
        return jsonify(dns_lookup(domain))
    except Exception as e:
        return jsonify({"error": f"Unexpected Error: {str(e)}"}), 500

@app.route('/api/whois', methods=['POST'])
def whois_api():
    try:
        data = request.get_json()
        if not data or 'domain' not in data:
            return jsonify({"error": "Invalid input. 'domain' is required"}), 400
        domain = data['domain']
        return jsonify(whois_lookup(domain))
    except Exception as e:
        return jsonify({"error": f"Unexpected Error: {str(e)}"}), 500

@app.route('/api/ipwhois', methods=['POST'])
def ip_whois_api():
    try:
        data = request.get_json()
        if not data or 'ip_address' not in data:
            return jsonify({"error": "Invalid input. 'ip_address' is required"}), 400
        ip_address = data['ip_address']
        return jsonify(ip_whois_lookup(ip_address))
    except Exception as e:
        return jsonify({"error": f"Unexpected Error: {str(e)}"}), 500

@app.route('/api/http_headers', methods=['POST'])
def http_headers_api():
    try:
        data = request.get_json()
        if not data or 'domain' not in data:
            return jsonify({"error": "Invalid input. 'domain' is required"}), 400
        domain = data['domain']
        return jsonify(http_headers(domain))
    except Exception as e:
        return jsonify({"error": f"Unexpected Error: {str(e)}"}), 500

if __name__ == "__main__":
    app.run(debug=True)
