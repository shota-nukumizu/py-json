import json

data = {
    "pokemon": {
        "name": "Mewtwo",
        "level": 50,
        "stock": False
    }
}

def main(file_path):
    with open(file_path, 'w') as f:
        json.dump(data, f, indent=4)

if __name__ == "__main__":
    file_path = 'sample.json'
    main(file_path)