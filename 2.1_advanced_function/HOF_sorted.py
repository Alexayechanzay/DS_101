a = [
    {"name": "Harry", "score": 85},
    {"name": "Leo", "score": 91},
    {"name": "Eve", "score": 78}
]

b = sorted(a, key=lambda x: x['score'],reverse=True)
print(b)
