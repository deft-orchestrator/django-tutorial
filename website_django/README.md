# Tutorial Django: Membangun Aplikasi Blog Sederhana

Selamat datang di repositori untuk seri tutorial "Django untuk Pemula". Repositori ini berisi kode sumber lengkap dan panduan langkah demi langkah untuk membangun aplikasi blog sederhana dari awal menggunakan Django.

## Deskripsi Proyek

Proyek ini adalah aplikasi web blog yang memungkinkan admin untuk membuat, membaca, memperbarui, dan menghapus postingan. Pengguna dapat melihat daftar semua postingan dan membaca detail setiap postingan.

## Fitur

*   Manajemen Postingan Blog (CRUD) melalui Django Admin.
*   Tampilan daftar semua postingan blog.
*   Tampilan detail untuk setiap postingan.

## Tutorial Guides

Berikut adalah panduan langkah demi langkah untuk tutorial ini. Setiap bagian mencakup penjelasan konsep dan kode yang relevan.

*   [**Part 0: Membuat Virtual Environment**](./tutorial/00-virtual-environment.md) - Pelajari mengapa dan bagaimana menggunakan virtual environment untuk proyek Python.
*   [**Part 2: Membuat App Blog**](./tutorial/02-creating-an-app.md) - Cara membuat aplikasi baru di dalam proyek Django dan mendaftarkannya.
*   [**Part 3: Model dan Migrasi**](./tutorial/03-model-and-migrations.md) - Mendefinisikan struktur data dengan Model dan menerapkannya ke database dengan migrasi.
*   [**Part 4: Mengelola Data melalui Halaman Admin**](./tutorial/04-django-admin.md) - Menggunakan Django Admin untuk mengelola data aplikasi.
*   [**Part 5: Mengenal Routing URL dan Views**](./tutorial/05-urls-and-views.md) - Dasar-dasar penanganan permintaan web dengan Views dan URL.
*   [**Part 6: Menampilkan Data di Halaman Web**](./tutorial/06-list-view-and-templates.md) - Menggunakan Template Django untuk menampilkan daftar data dari database.
*   [**Part 7: Menampilkan Detail Postingan Blog**](./tutorial/07-detail-view.md) - Membuat halaman detail untuk setiap item data.

## Prasyarat

*   Python 3.10 atau lebih tinggi
*   Pip (Package Installer for Python)
*   Git

## Instalasi dan Setup (Kode Final)

1.  **Clone repositori ini:**
    ```bash
    git clone https://github.com/username-anda/nama-repo-anda.git
    cd nama-repo-anda
    ```

2.  **Buat dan aktifkan virtual environment:**
    *   **Windows:**
        ```bash
        python -m venv .venv
        .\.venv\Scripts\activate
        ```
    *   **macOS/Linux:**
        ```bash
        python -m venv .venv
        source .venv/bin/activate
        ```

3.  **Instal dependensi:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Lakukan migrasi database:**
    ```bash
    python manage.py migrate
    ```

5.  **Buat superuser untuk mengakses halaman admin:**
    ```bash
    python manage.py createsuperuser
    ```

6.  **Jalankan server pengembangan:**
    ```bash
    python manage.py runserver
    ```
    Buka browser Anda dan kunjungi `http://127.0.0.1:8000/blogs/`.







# Part 7: Menampilkan Detail Postingan Blog

Dokumentasi ini menjelaskan secara detail langkah-langkah yang dilakukan pada part 7 tutorial membangun aplikasi blog sederhana dengan Django.

## Tujuan Part 7
- Menampilkan detail setiap postingan blog di halaman khusus

## Langkah-langkah

1. **Membuat View post_detail**
   - Tambahkan kode berikut ke `blogs/views.py`:
     ```python
     from django.shortcuts import render, get_object_or_404
     from .models import Post

     def get_blog_posts(request):
         blog_posts = Post.objects.all()
         context = {'blog_posts': blog_posts}
         return render(request, 'blogs/post_list.html', context)

     def post_detail(request, post_id):
         post = get_object_or_404(Post, id=post_id)
         return render(request, 'blogs/post_detail.html', {'post': post})
     ```

2. **Membuat Template HTML post_detail**
   - Buat file `post_detail.html` di `blogs/templates/blogs/` dengan kode:
     ```html
     <!DOCTYPE html>
     <html lang="en">
     <head>
         <meta charset="UTF-8">
         <meta name="viewport" content="width=device-width, initial-scale=1">
         <title>{{ post.title }}</title>
     </head>
     <body>
         <h1>{{ post.title }}</h1>
         <p>{{ post.content }}</p>
         <small>Published on {{ post.published_date }}</small>
         <br>
         <a href="{% url 'post_list' %}">Back to Blog List</a>
     </body>
     </html>
     ```

3. **Update Routing URL di blogs/urls.py**
   - Update routing agar mendukung halaman detail postingan:
     ```python
     from django.urls import path
     from .views import get_blog_posts, post_detail

     urlpatterns = [
         path('', get_blog_posts, name='post_list'),
         path('<int:post_id>/', post_detail, name='post_detail'),
     ]
     ```

4. **Update Template post_list agar judul menjadi link**
   - Update template agar judul postingan menjadi link ke halaman detail:
     ```html
     <ul>
         {% for post in blog_posts %}
             <li>
                 <h2><a href="{% url 'post_detail' post.id %}">{{ post.title }}</a></h2>
             </li>
         {% empty %}
             <li>Tidak ada postingan blog.</li>
         {% endfor %}
     </ul>
     ```

## Hasil Akhir
- Website sudah bisa menampilkan detail setiap postingan blog di halaman khusus.

## Selesai
- Tutorial selesai! Anda sudah memiliki aplikasi blog sederhana dengan Django.