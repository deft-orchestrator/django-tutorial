# Part 6: Menampilkan Data Blog di Halaman Web

Pada bagian sebelumnya, kita telah membuat sebuah halaman sederhana dengan `HttpResponse`. Sekarang, kita akan mempelajari cara menampilkan data blog yang telah kita simpan di database ke dalam halaman web menggunakan **template HTML**.

---

### Apa itu Template di Django?

Template di Django adalah file HTML yang berisi campuran dari HTML statis dan sintaks khusus Django. Template memungkinkan kita untuk memisahkan logika bisnis (di dalam `views.py`) dari tampilan (di dalam file `.html`), sehingga memudahkan pengelolaan kode. Dengan menggunakan template, kita dapat menampilkan data dinamis yang diambil dari database.

### Mengambil Data dari Database (Model)

Data blog diambil dari model `Post` yang telah kita buat. Untuk mengambil data ini, kita menggunakan **ORM (Object-Relational Mapping)** yang disediakan oleh Django. ORM memungkinkan kita untuk berinteraksi dengan database menggunakan kode Python, tanpa perlu menulis query SQL secara langsung.

Contoh penggunaan ORM untuk mengambil semua data blog dari model `Post`:
```python
from blogs.models import Post

# Ini akan mengambil semua objek (baris) dari tabel Post
blog_posts = Post.objects.all()
```

---

### Implementasi

Mari kita tampilkan semua judul postingan blog kita di halaman.

#### Langkah 1: Menyiapkan Template HTML

Kita akan membuat file `post_list.html`. Sesuai konvensi Django, kita harus membuat folder `templates` di dalam aplikasi kita.

1.  Buat folder `templates` di dalam folder `blogs`.
2.  Di dalam `templates`, buat lagi folder `blogs`.
3.  Di dalam `blogs/templates/blogs/`, buat file `post_list.html`.

Struktur direktori Anda akan terlihat seperti ini:
```
blogs/
├── templates/
│   └── blogs/
│       └── post_list.html  <-- File template baru
├── __init__.py
├── admin.py
...
```

Buka file `post_list.html` dan tambahkan kode HTML berikut:
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Blog List</title>
</head>
<body>
    <h1>Blog List</h1>
    <ul>
        {% for post in blog_posts %}
            <li>
                <h2>{{ post.title }}</h2>
            </li>
        {% empty %}
            <li>No blog posts available.</li>
        {% endfor %}
    </ul>
</body>
</html>
```
*   `{% for post in blog_posts %}`: Ini adalah *template tag* Django untuk perulangan (loop). Ia akan melakukan iterasi pada variabel `blog_posts` yang kita kirim dari view.
*   `{{ post.title }}`: Ini adalah sintaks untuk menampilkan variabel. Ia akan menampilkan nilai dari atribut `title` setiap objek `post`.
*   `{% empty %}`: Blok ini akan dieksekusi jika `blog_posts` kosong.

#### Langkah 2: Membuat Fungsi View untuk Menampilkan Data

Selanjutnya, kita akan memodifikasi `blogs/views.py` untuk mengambil data `Post` dan mengirimkannya ke template.

Ganti isi `blogs/views.py` dengan kode berikut:
```python
from django.shortcuts import render
from .models import Post

def get_blog_posts(request):
    blog_posts = Post.objects.all()
    context = {'blog_posts': blog_posts}
    return render(request, 'blogs/post_list.html', context)
```
*   Kita mengimpor `render`, sebuah *shortcut* untuk me-render template dengan sebuah *context*.
*   `Post.objects.all()` mengambil semua post dari database.
*   `context` adalah sebuah dictionary yang memetakan nama variabel di template (`'blog_posts'`) ke objek Python (`blog_posts`).
*   `render()` akan mengambil `request`, path ke template, dan `context`, lalu mengembalikan `HttpResponse` dengan HTML yang sudah di-render.

#### Langkah 3: Memperbarui Routing URL

Kita perlu memperbarui `blogs/urls.py` untuk menggunakan fungsi view yang baru.

Edit file `blogs/urls.py` menjadi seperti ini:
```python
from django.urls import path
from .views import get_blog_posts

urlpatterns = [
    path('', get_blog_posts, name='post_list'),
]
```
Kita sekarang mengimpor `get_blog_posts` dan menggunakannya untuk rute utama aplikasi kita. Kita juga mengubah nama rute menjadi `'post_list'` agar lebih deskriptif.

#### Langkah 4: Menjalankan Server dan Melihat Hasilnya

Jalankan server:
```bash
python manage.py runserver
```
Buka `http://127.0.0.1:8000/blogs/`. Anda akan melihat halaman yang menampilkan daftar judul postingan yang telah Anda buat melalui halaman admin.

### Kesimpulan

Pada bagian ini, kita telah mempelajari cara menampilkan data dari database di halaman web menggunakan template HTML di Django.

Pada [bagian terakhir](./07-detail-view.md), kita akan membuat halaman detail untuk setiap postingan.