# Part 7: Menampilkan Detail Postingan Blog

Pada bagian sebelumnya, kita telah berhasil menampilkan daftar semua judul postingan blog. Pada bagian terakhir ini, kita akan mempelajari cara menampilkan detail dari setiap postingan blog ketika pengguna mengklik judul postingan tersebut.

---

### Implementasi

Kita akan membuat fungsi view baru, template HTML baru, dan rute URL baru untuk menangani halaman detail.

#### Langkah 1: Membuat Fungsi View untuk Detail Postingan

Buka file `blogs/views.py` dan tambahkan fungsi view baru untuk menampilkan detail postingan berdasarkan ID-nya.

```python
# blogs/views.py

from django.shortcuts import render, get_object_or_404 # <-- Impor get_object_or_404
from .models import Post

def get_blog_posts(request):
    # ... (fungsi yang sudah ada)
    blog_posts = Post.objects.all()
    context = {'blog_posts': blog_posts}
    return render(request, 'blogs/post_list.html', context)

# Tambahkan fungsi baru di bawah ini
def post_detail(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    return render(request, 'blogs/post_detail.html', {'post': post})
```
*   `get_object_or_404` adalah *shortcut* Django yang sangat berguna. Ia mencoba mengambil objek dari model berdasarkan kriteria yang diberikan (dalam kasus ini, `id=post_id`). Jika objek tidak ditemukan, ia akan secara otomatis menampilkan halaman "404 Not Found", sehingga kita tidak perlu menangani error secara manual.
*   Fungsi `post_detail` menerima `post_id` dari URL dan menggunakannya untuk mengambil satu objek `Post`.
*   Kemudian, ia me-render template `post_detail.html` dengan data `post` tersebut.

#### Langkah 2: Membuat Template HTML untuk Detail Postingan

Buat file baru `post_detail.html` di dalam folder `blogs/templates/blogs/` dan tambahkan kode HTML berikut:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>{{ post.title }}</title>
</head>
<body>
    <h1>{{ post.title }}</h1>
    <p>{{ post.content }}</p>
    <small>Published on {{ post.published_date }}</small>
    <br><br>
    <a href="{% url 'post_list' %}">Back to Blog List</a>
</body>
</html>
```
Template ini menampilkan `title`, `content`, dan `published_date` dari objek `post` yang kita kirim dari view. Terdapat juga tautan untuk kembali ke halaman daftar blog.

#### Langkah 3: Menambahkan Routing URL untuk Detail Postingan

Buka file `blogs/urls.py` dan tambahkan routing URL untuk fungsi view `post_detail`.

```python
# blogs/urls.py

from django.urls import path
from .views import get_blog_posts, post_detail # <-- Impor post_detail

urlpatterns = [
    path('', get_blog_posts, name='post_list'),
    path('<int:post_id>/', post_detail, name='post_detail'), # <-- Tambahkan rute ini
]
```
*   `<int:post_id>/` adalah *path converter*. Ini memberitahu Django untuk mencocokkan URL yang memiliki sebuah integer (misalnya, `blogs/1/`, `blogs/2/`) dan menangkap nilai integer tersebut sebagai argumen bernama `post_id` untuk fungsi view.

#### Langkah 4: Menghubungkan Daftar Blog ke Halaman Detail

Langkah terakhir adalah mengubah `post_list.html` agar setiap judul postingan menjadi tautan yang bisa diklik.

Buka file `blogs/templates/blogs/post_list.html` dan ubah menjadi seperti ini:

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
                <h2><a href="{% url 'post_detail' post.id %}">{{ post.title }}</a></h2>
            </li>
        {% empty %}
            <li>No blog posts available.</li>
        {% endfor %}
    </ul>
</body>
</html>
```
*   `{% url 'post_detail' post.id %}` adalah *template tag* yang sangat powerful. Ia akan secara dinamis membuat URL berdasarkan nama rute (`'post_detail'`) yang kita definisikan di `urls.py`.
*   `post.id` diteruskan sebagai argumen untuk `post_id` yang dibutuhkan oleh rute tersebut. Django akan menghasilkan URL seperti `/blogs/1/`, `/blogs/2/`, dan seterusnya.

#### Langkah 5: Menjalankan Server dan Menguji

Jalankan server dan buka `http://127.0.0.1:8000/blogs/`. Klik pada salah satu judul postingan. Anda sekarang akan diarahkan ke halaman detail untuk postingan tersebut.

### Kesimpulan

Selamat! Anda telah berhasil membangun aplikasi blog sederhana dengan Django. Anda telah mempelajari cara membuat proyek, aplikasi, model, menggunakan admin, dan menampilkan data menggunakan views, URL, dan template. Ini adalah dasar yang kuat untuk membangun aplikasi web yang lebih kompleks dengan Django.