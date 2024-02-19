class Library:
    def __init__(self):
        self.file = open("books.txt", "a+")

    def list_books(self):
        self.file.seek(0)
        books = self.file.read().splitlines()
        for book in books:
            book_info = book.split(',')
            print(f"Kitap Adı: {book_info[0]}, Yazar: {book_info[1]}")

    def add_book(self):
        title = input("Kitap adını giriniz: ")
        author = input("Yazar ismini giriniz: ")
        release_year = input("Basım yılını giriniz: ")
        num_pages = input("Sayfa sayısını giriniz: ")
        book_info = f"{title},{author},{release_year},{num_pages}\n"
        self.file.write(book_info)
        print("Kitap kütüphane listesine eklendi.")

    def remove_book(self):
        title = input("Listeden kaldırmak istediğiniz kitabın adını giriniz: ")
        self.file.seek(0)
        books = self.file.readlines()
        updated_books = []
        for book in books:
            if not book.startswith(title):
                updated_books.append(book)
        self.file.seek(0) # dosya içinde kaçıncı bayt konumuna gideceğimizi gösteren method
        self.file.truncate()# dosya boyutunu kısaltmak için kullanılan method
        self.file.writelines(updated_books)
        print(f"'{title}' adlı kitap listeden kaldırıldı.")

    def __del__(self):
        self.file.close()

# Library sınıfından lib adlı nesne üretme
lib = Library()

# Menü bölümünü hazırlama
while True:
    print("\n*** MENU ***")
    print("1) List Books")
    print("2) Add Book")
    print("3) Remove Book")
    print("4) Exit")
    choice = input("Seçiminizi giriniz: ")

    if choice == '1':
        lib.list_books()
    elif choice == '2':
        lib.add_book()
    elif choice == '3':
        lib.remove_book()
    elif choice == 'q' or choice == 'Q':
        break
    else:
        print("Geçersiz seçim. Lütfen tekrar deneyin.")
