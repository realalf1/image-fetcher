import requests

class Images():
    def __init__(self, source, destination):
        self.name = "Fetch Images with Python"
        self.source = source
        self.destination = destination
        self.status = False

    def fetch(self):
        r = requests.get(self.source)

        if r.status_code == 200:
            with open(self.destination, "wb") as f:
                f.write(r.content)
                print("Fetching image successfully\n")
            self.status = True
        
        else:
            print(f"Failed to fetch {self.source}\n")
            
    def run(self):
        self.fetch()
        print(f"Source     : {self.source}")
        print(f"Destination: {self.destination}")
        print(f"Status     : {self.status}")

if __name__ == "__main__":
    src = "https://source.com/source.png"
    dst = "./img/source.png"
    image = Images(src, dst)
    image.run()
