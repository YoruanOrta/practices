import pywhatkit as kit
from datetime import datetime, timedelta

# This script sends a WhatsApp message to a specified phone number after a delay of 2 minutes.

def send_message_later(phone_number: str, message: str, delay_minutes: int = 2):
    now = datetime.now()
    future_time = now + timedelta(minutes=delay_minutes)
    hour = future_time.hour
    minute = future_time.minute

    print(f"📅 Message scheduled for {hour:02d}:{minute:02d}")

    kit.sendwhatmsg(
        f"+{phone_number}",
        message,
        hour,
        minute,
        wait_time=20,
    )

if __name__ == "__main__":
    phone_number = "1234567890"  #replace with a real number
    message = "Hello, this is a test message!"

    send_message_later(phone_number, message)