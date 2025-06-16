import requests
import time

TOKEN = "8093843084:AAEAwokhExTaWZ4ya3EIa0WIqLnW9NFzVsA"
CHAT_ID = "5926971390"

def send(msg):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    requests.post(url, data={"chat_id": CHAT_ID, "text": msg})

def check_capago_france():
    try:
        r = requests.get("https://dz-fr.capago.eu/", timeout=10)
        if "Aucun rendez-vous disponible" not in r.text:
            send("🇫🇷 موعد متاح في Capago فرنسا")
    except:
        send("⚠️ خطأ في فرنسا")

def check_bls_spain():
    try:
        r = requests.get("https://dz.blsspainvisa.com/book_appointment.php", timeout=10)
        if "No appointment slots" not in r.text:
            send("🇪🇸 موعد متاح في BLS إسبانيا")
    except:
        send("⚠️ خطأ في إسبانيا")

def check_tls_germany():
    try:
        r = requests.get("https://dz.tlscontact.com/dz/ALG/de", timeout=10)
        if "no appointments available" not in r.text.lower():
            send("🇩🇪 موعد متاح في TLS ألمانيا")
    except:
        send("⚠️ خطأ في ألمانيا")

def check_vfs_italy():
    try:
        r = requests.get("https://visa.vfsglobal.com/dza/en/ita/book-an-appointment", timeout=10)
        if "No appointment available" not in r.text:
            send("🇮🇹 موعد متاح في VFS إيطاليا")
    except:
        send("⚠️ خطأ في إيطاليا")

def check_all():
    check_capago_france()
    check_bls_spain()
    check_tls_germany()
    check_vfs_italy()

while True:
    print("🔄 التحقق من المواعيد الأوروبية...")
    check_all()
    time.sleep(300)
