# Aim: Extract email addresses, Indian mobile numbers, and URLs using regex.
import re

text = """
Contact us at student@gmail.com or admin@yahoo.com.
Phone: 9876543210
Website: https://www.example.com
"""

print("Emails:", re.findall(r"[\w.-]+@[\w.-]+\.\w+", text))
print("Mobile numbers:", re.findall(r"\b[6-9]\d{9}\b", text))
print("URLs:", re.findall(r"https?://\S+", text))
