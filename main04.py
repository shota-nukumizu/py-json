import json

def main():
    json_string = """{
        "pokemon": {"name": "Mewtwo", "level": 50, "stock": false}}
    """
    data = json.loads(json_string)
    print(data)

if __name__ == '__main__':
    main()
