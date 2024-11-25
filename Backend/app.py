from flask import Flask, request, jsonify
from flask_cors import CORS
from investigation import dns_lookup, whois_lookup, ip_whois_lookup, http_headers
import re
import logging

# Initialize Flask app and enable CORS
app = Flask(__name__)
CORS(app)

# Configure logging
logging.basicConfig(level=logging.DEBUG)

# Helper function to validate domains
def is_valid_domain(domain):
    pattern = r'^(?:[a-zA-Z0-9-]{1,63}\.)+[a-zA-Z]{2,}$'
    return re.match(pattern, domain) is not None

@app.route('/api/dns', methods=['POST'])
def dns_api():
    try:
        data = request.get_json()
        domain = data.get('domain', '').strip()
        if not is_valid_domain(domain):
            return jsonify({"error": "Invalid domain format"}), 400
        logging.debug(f"Processing DNS for: {domain}")
        return jsonify(dns_lookup(domain))
    except Exception as e:
        logging.error(f"DNS API Error: {e}")
        return jsonify({"error": f"Unexpected Error: {str(e)}"}), 500

@app.route('/api/whois', methods=['POST'])
def whois_api():
    try:
        data = request.get_json()
        domain = data.get('domain', '').strip()
        if not is_valid_domain(domain):
            return jsonify({"error": "Invalid domain format"}), 400
        logging.debug(f"Processing WHOIS for: {domain}")
        return jsonify(whois_lookup(domain))
    except Exception as e:
        logging.error(f"WHOIS API Error: {e}")
        return jsonify({"error": f"Unexpected Error: {str(e)}"}), 500

@app.route('/api/ipwhois', methods=['POST'])
def ip_whois_api():
    try:
        data = request.get_json()
        ip_address = data.get('ip_address', '').strip()
        if not ip_address:
            return jsonify({"error": "Invalid IP address"}), 400
        logging.debug(f"Processing IP WHOIS for: {ip_address}")
        return jsonify(ip_whois_lookup(ip_address))
    except Exception as e:
        logging.error(f"IP WHOIS API Error: {e}")
        return jsonify({"error": f"Unexpected Error: {str(e)}"}), 500

@app.route('/api/http_headers', methods=['POST'])
def http_headers_api():
    try:
        data = request.get_json()
        domain = data.get('domain', '').strip()
        if not is_valid_domain(domain):
            return jsonify({"error": "Invalid domain format"}), 400
        logging.debug(f"Processing HTTP Headers for: {domain}")
        return jsonify(http_headers(domain))
    except Exception as e:
        logging.error(f"HTTP Headers API Error: {e}")
        return jsonify({"error": f"Unexpected Error: {str(e)}"}), 500

if __name__ == "__main__":
    app.run(debug=True)
