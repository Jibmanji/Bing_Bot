# import

import requests, random, os

# Declare
payload = {
    'loginfmt': "jckhendrix@gmail.com",
    'passwd': "VY65224q$"
}
url_login = "https://login.live.com/"
url_search = "http://www.bing.com"
package_dir = os.path.dirname(os.path.abspath(__file__))
bing_words = os.path.join(package_dir, 'bing_words.txt')
search_count = 0

# define function
def bing_search():
    r = requests.post(url_login, data=payload)
    r.status_code
    s = requests.post(url_search, data={print(random.choice(open(bing_words).readline().split()))})
    print("success")

# Repeat

while search_count <= 10:
    bing_search()
    search_count = search_count + 1
    print("current value of ", search_count)

# Send Email After daily run
