# Tutorial Django: Membangun Aplikasi Blog Sederhana

Selamat datang di repositori untuk seri tutorial "Django untuk Pemula". Dalam tutorial ini, kita akan membangun aplikasi blog sederhana dari awal menggunakan Django.

## Deskripsi Proyek

Proyek ini adalah aplikasi web blog yang memungkinkan admin untuk membuat, membaca, memperbarui, dan menghapus postingan. Pengguna dapat melihat daftar semua postingan dan membaca detail setiap postingan.

## Fitur

* Manajemen Postingan Blog (CRUD) melalui Django Admin.
* Tampilan daftar semua postingan blog.
* Tampilan detail untuk setiap postingan.

## Prasyarat

* Python 3.10 atau lebih tinggi
* Pip (Package Installer for Python)
* Git

## Instalasi dan Setup

1.  **Clone repositori ini:**
    ```bash
    git clone https://github.com/username-anda/nama-repo-anda.git
    cd nama-repo-anda
    ```

2.  **Buat dan aktifkan virtual environment:**
    * **Windows:**
        ```bash
        python -m venv .venv
        .\.venv\Scripts\activate
        ```
    * **macOS/Linux:**
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

## Struktur Tutorial

Setiap bagian dari tutorial ini akan disimpan dalam branch yang berbeda untuk memudahkan navigasi.

* **main**: Kode akhir dari proyek.
* **part-1-setup-project**: Hasil dari Bagian 1: Membuat Proyek Django.
* **part-2-membuat-app-blog**: Hasil dari Bagian 2: Membuat App Blog.
* dan seterusnya...