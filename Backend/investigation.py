import socket
import whois
from ipwhois import IPWhois
import requests

def dns_lookup(domain):
    """Resolve the domain to an IP address."""
    try:
        ip_address = socket.gethostbyname(domain)
        return {"ip_address": ip_address}
    except Exception as e:
        return {"error": f"DNS Lookup Error: {e}"}

def whois_lookup(domain):
    """Perform a WHOIS lookup on the domain."""
    try:
        w = whois.whois(domain)
        return {
            "domain_name": w.domain_name,
            "owner": w.name,
            "organization": w.org,
            "email": w.emails,
            "registration_date": str(w.creation_date),
            "expiration_date": str(w.expiration_date),
            "name_servers": w.name_servers,
        }
    except Exception as e:
        return {"error": f"WHOIS Error: {e}"}

def ip_whois_lookup(ip_address):
    """Perform an IP WHOIS lookup."""
    try:
        ip_info = IPWhois(ip_address)
        result = ip_info.lookup_whois()
        return {
            "asn": result.get("asn"),
            "asn_registry": result.get("asn_registry"),
            "asn_country_code": result.get("asn_country_code"),
            "asn_description": result.get("asn_description"),
            "nets": result.get("nets"),
        }
    except Exception as e:
        return {"error": f"IP WHOIS Error: {e}"}

def http_headers(domain):
    """Inspect HTTP headers of the web server."""
    try:
        response = requests.head(f"http://{domain}", timeout=5)
        return dict(response.headers)
    except Exception as e:
        return {"error": f"HTTP Request Error: {e}"}
