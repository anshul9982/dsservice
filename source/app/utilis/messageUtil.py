import re

class MessageUtil:
    def isBankSms(self, message):
        bank_keywords = ["debited", "credited", "txn", "payment", "UPI", "IMPS", "NEFT", "ATM", "card", "Rs"]
        pattern = r'\b(' + '|'.join(re.escape(word) for word in bank_keywords) + r')\b'
        return bool(re.search(pattern, message, re.IGNORECASE))