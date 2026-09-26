requests = [
    {
        "message": "I forgot my password",
        "category": "account",
        "confidence": 0.94
    },
    {
        "message": "Where is my order?",
        "category": "delivery",
        "confidence": 0.87
    },
    {
        "message": "I want a refund",
        "category": "billing",
        "confidence": 0.91
    }
]


high_confidence = [request for request in requests if request["confidence"] >= 0.90]

print(high_confidence)