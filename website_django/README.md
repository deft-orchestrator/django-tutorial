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

# Part 1: Setup Proyek Django

Dokumentasi ini menjelaskan secara detail langkah-langkah yang dilakukan pada part 1 tutorial membangun aplikasi blog sederhana dengan Django.

## Tujuan Part 1
- Menyiapkan virtual environment untuk project Python
- Menginstal Django
- Membuat struktur awal proyek Django

## Langkah-langkah

1. **Membuat Virtual Environment**
    - Jalankan perintah berikut di terminal:
      ```bash
      python -m venv .venv
      source .venv/bin/activate  # Untuk Linux/Mac
      .\.venv\Scripts\activate  # Untuk Windows
      ```

2. **Instalasi Django**
    - Setelah virtual environment aktif, install Django:
      ```bash
      pip install Django
      ```

3. **Membuat Proyek Django**
    - Buat folder project (misal: `website_django`) lalu jalankan:
      ```bash
      django-admin startproject website_django .
      ```
    - Struktur project yang dihasilkan:
      ```
      website_django/
      ├── manage.py
      └── website_django/
            ├── __init__.py
            ├── asgi.py
            ├── settings.py
            ├── urls.py
            └── wsgi.py
      ```

## Hasil Akhir
- Proyek Django siap digunakan untuk pengembangan lebih lanjut.
- Belum ada aplikasi (app) khusus, hanya struktur dasar Django.

## Selanjutnya
- Di part 2, kita akan membuat aplikasi blog di dalam proyek Django ini.