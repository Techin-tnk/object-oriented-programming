import requests

# กำหนดค่า ISBN ที่ต้องการค้นหา
isbn = "9780140328721"

# URL สำหรับการเรียก API
url = f"https://openlibrary.org/api/books"
params = {
    "bibkeys": f"ISBN:{isbn}",
    "format": "json",
    "jscmd": "data"
}

# เรียก API
response = requests.get(url, params=params)

# ตรวจสอบสถานะการตอบกลับ
if response.status_code == 200:
    data = response.json()
    if f"ISBN:{isbn}" in data:
        book = data[f"ISBN:{isbn}"]
        title = book['title']
        authors = ", ".join([author['name'] for author in book.get('authors', [])])
        publish_date = book.get('publish_date', 'N/A')

        print(f"Title: {title}")
        print(f"Authors: {authors}")
        print(f"Publish Date: {publish_date}")
    else:
        print("No book found with that ISBN.")
else:
    print("Failed to fetch data.")
