import requests

def search_books(query):
    url = "https://www.googleapis.com/books/v1/volumes"
    params = {
        "q": query,  
        "maxResults": 5,  
        "printType": "books"
    }

    response = requests.get(url, params=params)    

    if response.status_code == 200:
        books = response.json().get("items", [])
        for book in books:
            volume_info = book.get("volumeInfo", {})
            title = volume_info.get("title", "ไม่พบชื่อหนังสือ")
            authors = volume_info.get("authors", ["ไม่ทราบผู้แต่ง"])
            print(f"📖 {title} - โดย {', '.join(authors)}")
    else:
        print("เกิดข้อผิดพลาดในการเรียก API")

search_books("Python programming")