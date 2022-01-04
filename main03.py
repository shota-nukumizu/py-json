import json

def main(file_path):
    with open(file_path, "r") as f:
        data = json.load(f)
        print(data)

if __name__ == "__main__":
    file_path = 'sample.json'
    main(file_path)