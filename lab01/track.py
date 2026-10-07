from flask import Flask, request, jsonify
import user_agents # pip install pyyaml ua-parser user-agents

app = Flask(__name__)

def get_client_ip(req):
    """
    Extrage IP-ul real al clientului, chiar dacă aplicația se află 
    în spatele unui Reverse Proxy (ex: Nginx, Cloudflare).
    """
    if req.headers.get('X-Forwarded-For'):
        ip = req.headers.get('X-Forwarded-For').split(',')[0].strip()
    elif req.headers.get('X-Real-IP'):
        ip = req.headers.get('X-Real-IP')
    else:
        ip = req.remote_addr
    return ip

@app.route('/track', methods=['POST', 'GET'])
def collect_user_data():

    # 1. Adresa IP
    client_ip = get_client_ip(request)
    
    # 2. User-Agent (sistem de operare, browser web, dispozitiv)
    ua_string = request.headers.get('User-Agent', '')
    user_agent = user_agents.parse(ua_string)
    
    device_info = {
        'raw_user_agent': ua_string,
        'browser': f"{user_agent.browser.family} {user_agent.browser.version_string}",
        'os': f"{user_agent.os.family} {user_agent.os.version_string}",
        'device_type': 'Mobile' if user_agent.is_mobile else ('Tablet' if user_agent.is_tablet else 'Desktop'),
        'is_bot': user_agent.is_bot
    }

    # 3. Context lingvistic
    accept_language = request.headers.get('Accept-Language', '')
    primary_language = accept_language.split(',')[0] if accept_language else None

    # 4. Sursa de trafic (Referrer)
    referrer = request.headers.get('Referer') # Sursa din care a venit utilizatorul (ex: Google, Social Media)
    current_url = request.url

    # 5. Sesiune si Identificatori Persistenți (Cookie-uri)
    # Permite asocierea datelor anonime cu un profil de utilizator existent
    user_session_id = request.cookies.get('session_id', 'anon_user_12345')

    # 6. Payload explicit transmis prin request (ex: interactiunea curentă)
    interaction_payload = request.get_json(silent=True) or request.args.to_dict()

    # Datele colectate pentru pipeline-ul de recomandare
    collected_data = {
        'user_session_id': user_session_id,
        'network': {
            'ip_address': client_ip
        },
        'device_context': device_info,
        'user_preferences_implicit': {
            'preferred_language': primary_language,
            'all_languages': accept_language
        },
        'navigation_context': {
            'referrer': referrer,
            'current_url': current_url,
            'http_method': request.method
        },
        'event_payload': interaction_payload
    }

    return jsonify({
        "status": "success",
        "message": "Date colectate cu succes",
        "data_preview": collected_data
    }), 200

if __name__ == '__main__':
    app.run(debug=True, port=5000)
