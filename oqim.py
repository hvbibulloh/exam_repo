import threading
import requests


def send_request(site_url):
    response = requests.get(site_url)
    print(f"{threading.current_thread().name}  {site_url} ga request yubordi. Response kod >> {response.status_code}")

if __name__ == "__main__":
    site_urls = [
        "https://www.google.com",
        "https://www.facebook.com",
        "https://www.youtube.com",
        "https://www.twitter.com",
        "https://www.instagram.com"
    ]

    oqimlar = []

    for i in range(5):
        oqimnomi = f"oqim{i+1}"
        site_url = site_urls[i]
        oqim = threading.Thread(name=oqimnomi, target=send_request, args=[site_url])
        oqimlar.append(oqim)

    for i in oqimlar:
        i.start()


    for i in oqimlar:
        i.join()
