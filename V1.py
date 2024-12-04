from googlesearch import search
import requests
from bs4 import BeautifulSoup

def fetch_clothing_sites(query, country, num_results=10):
    print(f"جلب مواقع بيع لـ {country}...")
    results = []
    
    search_query = f"{query} site:.{country} online clothing store"


    count = 0
    for url in search(search_query):
        if count >= num_results:
            break
        try:
            
            response = requests.get(url, timeout=10)
            if response.status_code == 200:
                
                soup = BeautifulSoup(response.text, 'html.parser')
                title = soup.title.string if soup.title else "No title"
                results.append(f"{title}\n{url}\n")
                print(f"تم العثور على: {url} - {title}")
                count += 1
        except Exception as e:
            print(f"خطأ أثناء الوصول إلى {url}: {e}")

    return results


country_code = input("أدخل رمز الدولة (مثل 'uk' أو 'us'): ").strip() 
query = "online clothing store"  

sites = fetch_clothing_sites(query, country_code, num_results=10)


file_path = '/sdcard/v1.txt'


with open(file_path, 'a', encoding='utf-8') as file:
    for site in sites:
        file.write(site + "\n")

print(f"تم حفظ النتائج في {file_path}")