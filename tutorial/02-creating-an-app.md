# Part 2: Membuat App Blog

Kali ini kita akan membuat *app* di dalam Django. App tersebut adalah sebuah Blog. Kita akan memulai dari blog yang sederhana, yaitu isi blog dimasukan oleh admin dan ditampilkan di halaman blog website.

**User Story:** Sebagai admin, saya ingin bisa membuat postingan blog di website Django saya. Saya juga ingin bisa mengupdate postingan tersebut dan bisa menghapusnya.

---

### Membuat dan Menambahkan App

Untuk membuat app bernama `blogs` (disarankan nama app berupa kata jamak/plural), perintah yang kita gunakan adalah sebagai berikut:

```bash
python manage.py startapp blogs
```

Perintah ini akan membuat folder `blogs` di dalam direktori proyek Django kita. Struktur folder kita sekarang akan terlihat seperti ini:

```
website_django/
├── .venv/
├── blogs/              <-- App baru
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── migrations/
│   ├── models.py
│   ├── tests.py
│   └── views.py
├── manage.py
└── website_django/
    └── ...
```

### Mendaftarkan App di `settings.py`

Membuat app saja tidaklah cukup. Agar app tersebut terbaca oleh Django, kita perlu mendaftarkannya di dalam file `settings.py` agar Django mengenalinya.

Buka file `website_django/website_django/settings.py` dan tambahkan aplikasi `blogs` ke dalam daftar `INSTALLED_APPS`.

Secara default, Django Framework sudah menyiapkan 6 buah aplikasi bawaan:

```python
# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]
```

Tambahkan `'blogs.apps.BlogsConfig'` di bagian akhir daftar `INSTALLED_APPS` sehingga menjadi seperti berikut:

```python
# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'blogs.apps.BlogsConfig', # <-- Tambahkan baris ini
]
```

> **Mengapa `blogs.apps.BlogsConfig`?**
> Ini adalah cara yang direkomendasikan oleh Django untuk mendaftarkan aplikasi. `BlogsConfig` adalah kelas konfigurasi aplikasi yang dibuat secara otomatis di dalam file `blogs/apps.py` ketika kita membuat app. Dengan menambahkan aplikasi ke dalam `INSTALLED_APPS`, Django akan mengenali aplikasi tersebut dan kita dapat mulai menggunakannya dalam proyek kita.

### Kesimpulan

Dalam tutorial ini, kita telah berhasil membuat aplikasi blog di dalam proyek Django kita dan mendaftarkannya di dalam `settings.py`. Dengan langkah ini, kita telah menyiapkan dasar untuk mengembangkan aplikasi blog lebih lanjut.

Pada [tutorial berikutnya](./03-model-and-migrations.md), kita akan menambahkan fitur `Post` ke dalam aplikasi blog kita.