import json
import urllib3
import base64

VT_API_KEY = "YOUR_VIRUSTOTAL_API_KEY_HERE"

def lambda_handler(event, context):
    method = event.get("requestContext", {}).get("http", {}).get("method") or event.get("httpMethod")

    if method == "GET" or method is None:
        html_code = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>LINK VALIDATOR | MUHAMMAD ALFATIH</title>
    <style>
        :root { --neon-green: #00ff41; --dark-bg: #050a10; --card-bg: #0a0f1a; }
        body { background: var(--dark-bg); color: var(--neon-green); font-family: 'Courier New', monospace; display: flex; justify-content: center; align-items: center; min-height: 100vh; margin: 0; padding: 20px; }
        .terminal { background: var(--card-bg); border: 1px solid var(--neon-green); padding: 35px; border-radius: 12px; box-shadow: 0 0 40px rgba(0, 255, 65, 0.15); width: 100%; max-width: 480px; text-align: center; }
        .header { margin-bottom: 30px; padding-bottom: 15px; border-bottom: 1px solid rgba(0, 255, 65, 0.2); }
        h1 { margin: 0; font-size: 1.8rem; letter-spacing: 5px; text-shadow: 0 0 10px var(--neon-green); text-align: center; }
        .dev-tag { font-size: 13px; color: #8892b0; margin-top: 10px; letter-spacing: 1px; text-align: center; }
        .input-group { margin: 25px 0; text-align: left; }
        input { width: 93%; background: #000; border: 1px solid #333; color: var(--neon-green); padding: 15px; outline: none; font-family: inherit; font-size: 14px; text-align: center; }
        input:focus { border-color: var(--neon-green); }
        button { width: 100%; background: var(--neon-green); color: #000; border: none; padding: 16px; font-weight: 900; cursor: pointer; font-family: inherit; font-size: 14px; letter-spacing: 2px; text-transform: uppercase; }
        button:hover { background: #fff; box-shadow: 0 0 20px #fff; }
        button:disabled { background: #222; color: #444; }
        #res { margin-top: 25px; padding: 20px; background: rgba(0,0,0,0.8); border: 1px solid #333; border-left: 5px solid var(--neon-green); text-align: left; font-size: 14px; display: none; }
        .danger { border-left-color: #ff3e3e !important; color: #ff3e3e; }
        .footer-stack { margin-top: 40px; font-size: 10px; color: #444; border-top: 1px solid #222; padding-top: 15px; }
        .grid { display: grid; grid-template-columns: 1fr 1fr; gap: 8px; margin-top: 10px; text-align: left; }
        .grid span { background: #070707; padding: 4px; border: 1px solid #111; }
    </style>
</head>
<body>
    <div class="terminal">
        <div class="header">
            <h1>LINK VALIDATOR</h1>
            <div class="dev-tag">DEVELOPED BY MUHAMMAD ALFATIH</div>
        </div>
        <div class="input-group">
            <div style="font-size: 11px; margin-bottom: 8px; text-align: center;">[V3_ENGINE]: WAITING_FOR_INPUT...</div>
            <input type="text" id="urlInp" placeholder="HTTPS://TARGET-URL.COM" autocomplete="off">
        </div>
        <button id="scanBtn" onclick="runScan()">RUN SECURITY CHECK</button>
        <div id="res"></div>
        <div class="footer-stack">
            <div style="font-weight: bold; color: #666; margin-bottom: 5px; text-align: center;">ARCHITECTURE_STACK:</div>
            <div class="grid">
                <span>> AWS_LAMBDA</span> <span>> VIRUSTOTAL_V3</span>
                <span>> PYTHON_3.12</span> <span>> BOTO3_SDK</span>
                <span>> HTML5_CSS3</span> <span>> JS_ES6_FETCH</span>
            </div>
        </div>
    </div>
    <script>
        async function runScan() {
            const urlInput = document.getElementById("urlInp");
            const res = document.getElementById("res");
            const btn = document.getElementById("scanBtn");
            if(!urlInput.value) return;
            btn.disabled = true;
            btn.innerText = "PROCESSING...";
            res.style.display = "block";
            res.className = "";
            res.innerHTML = "> INITIATING API V3...<br>> ANALYZING REPUTATION...";
            try {
                const response = await fetch(window.location.href, {
                    method: 'POST',
                    headers: {'Content-Type': 'application/json'},
                    body: JSON.stringify({ url: urlInput.value })
                });
                const data = await response.json();
                if(data.error) {
                    res.innerHTML = "> SYSTEM_ALERT: " + data.error;
                } else {
                    const s = data.stats;
                    const threat = s.malicious > 0 || s.suspicious > 0;
                    if(threat) res.classList.add("danger");
                    res.innerHTML = "<b>[ SCAN_REPORT ]</b><br>" +
                                   "STATUS      : " + (threat ? "THREAT_DETECTED" : "CLEAN_URL") + "<br>" +
                                   "----------------------------<br>" +
                                   "MALICIOUS   : " + s.malicious + "<br>" +
                                   "SUSPICIOUS  : " + s.suspicious + "<br>" +
                                   "HARMLESS    : " + s.harmless + "<br>" +
                                   "----------------------------<br>" +
                                   "<small>ANALYSIS BY MUHAMMAD ALFATIH</small>";
                }
            } catch (e) {
                res.innerHTML = "> CRITICAL_ERROR: FAIL_TO_CONNECT";
            } finally {
                btn.disabled = false;
                btn.innerText = "RUN SECURITY CHECK";
            }
        }
    </script>
</body>
</html>
        """
        return {"statusCode": 200, "headers": {"Content-Type": "text/html"}, "body": html_code}

    try:
        body = json.loads(event.get("body", "{}"))
        target_url = body.get("url")
        if not target_url: return {"statusCode": 400, "body": json.dumps({"error": "Empty URL"})}

        url_id = base64.urlsafe_b64encode(target_url.encode()).decode().strip("=")
        http = urllib3.PoolManager()
        headers = {"x-apikey": VT_API_KEY}
        r = http.request("GET", f"https://www.virustotal.com/api/v3/urls/{url_id}", headers=headers)
        
        if r.status == 404:
            return {"statusCode": 200, "body": json.dumps({"error": "URL NOT FOUND IN DATABASE"})}
        
        data = json.loads(r.data.decode())
        stats = data['data']['attributes']['last_analysis_stats']
        
        return {
            "statusCode": 200,
            "headers": {"Access-Control-Allow-Origin": "*", "Content-Type": "application/json"},
            "body": json.dumps({"stats": stats})
        }
    except Exception as e:
        return {"statusCode": 500, "body": json.dumps({"error": str(e)})}
