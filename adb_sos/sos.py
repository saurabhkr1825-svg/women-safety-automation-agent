import subprocess
import time

def adb(cmd):
    full_cmd = f"adb shell {cmd}"
    subprocess.run(full_cmd, shell=True)

# 1️⃣ Call emergency number
def call_emergency():
    print("[+] Calling 112")
    adb("am start -a android.intent.action.CALL -d tel:112")

# 2️⃣ Send SMS
def send_sms(number, message):
    print("[+] Sending SMS")
    adb(
        f'am start -a android.intent.action.SENDTO '
        f'-d sms:{number} '
        f'--es sms_body "{message}" '
        f'--ez exit_on_sent true'
    )

# 3️⃣ Get location (last known)
def get_location():
    print("[+] Fetching location")
    result = subprocess.check_output(
        "adb shell dumpsys location | findstr latitude",
        shell=True,
        text=True,
        errors="ignore"
    )
    return result.strip() if result else "Location unavailable"

# 4️⃣ Play alarm
def play_alarm():
    print("[+] Playing alarm")
    adb("media volume --stream 3 --set 15")
    adb("cmd media_session volume --set 15")

# 🚨 MAIN SOS FUNCTION
def sos():
    location = get_location()

    message = f"""
🚨 EMERGENCY ALERT 🚨
I am in danger.
📍 Location info:
{location}
"""

    call_emergency()
    time.sleep(5)

    send_sms("+919235552376", message)
    play_alarm()

    print("[✓] SOS triggered successfully")

if __name__ == "__main__":
    sos()
