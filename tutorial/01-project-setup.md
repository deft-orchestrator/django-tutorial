# Part 1: Membuat Django Project

Kita akan belajar membuat aplikasi berbasis web menggunakan Framework Django. Langkah pertama adalah membuat virtual environment di Python. Jika Anda belum tahu caranya, silakan mengikuti [panduan membuat virtual environment](./00-virtual-environment.md) di tulisan sebelumnya.

---

### Menginstal Django

Setelah Anda selesai membuat dan mengaktifkan virtual environtment, maka langkah selanjutnya adalah menginstal Django.

```bash
pip install Django
```

Paket Django akan terpasang dan bisa digunakan.

### Membuat Project

Pastikan sudah di dalam folder project (`website_django`) yang telah kita buat ketika kita membuat Virtual Environment.

Untuk membuat project, perintah yang digunakan adalah:

```bash
django-admin startproject website_django .
```

Setelah django project selesai kita buat, maka Django secara otomatis menghasilkan folder dan file untuk kita. Struktur folder kita sekarang akan terlihat seperti ini:

```
website_django/
├── .venv/
├── manage.py
└── website_django/
    ├── __init__.py
    ├── asgi.py
    ├── settings.py
    ├── urls.py
    └── wsgi.py
```

### Menjalankan Project

Project Django bisa kita jalankan melalui Server Development bawaan Django. Untuk menjalankan server dan mengakses project kita, gunakan perintah berikut:

```bash
python manage.py runserver
```

Otomatis server akan berjalan dan secara default menggunakan port 8000. Tampilan di terminal adalah seperti di bawah ini.

```
Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).

You have 18 unapplied migration(s). Your project may not work properly until you apply the migrations for app(s): admin, auth, contenttypes, sessions.
Run 'python manage.py migrate' to apply them.

September 10, 2025 - 07:02:46
Django version 5.2.6, using settings 'website_django.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.
```
> **Catatan:** Jangan khawatir dengan pesan `warning` yang ada terkait `unapplied migrations`. Kita akan membahasnya nanti.

Apabila kita buka browser dan kita ketikan alamat `http://127.0.0.1:8000`, maka otomatis akan menampilkan halaman selamat datang Django.

**Selamat, Anda sudah berhasil membuat project dengan Django!**

Selanjutnya di [Part 2](./02-creating-an-app.md), kita akan menambahkan aplikasi `blog` ke project kita.