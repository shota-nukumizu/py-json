import json

data = {
    "pokemon": {
        "name": "Mewtwo",
        "level": 50,
        "stock": False
    }
}

def main():
    json_string = json.dumps(data, indent=4)
    print(json_string)

if __name__ == "__main__":
    main()