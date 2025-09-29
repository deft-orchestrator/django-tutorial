# Part 4: Mengelola Data melalui Halaman Admin

Setelah kita berhasil membuat model `Post` pada artikel sebelumnya, sekarang kita akan belajar cara mengelola data postingan blog menggunakan halaman admin bawaan Django.

---

### Apa itu Django Admin?

Django Admin adalah aplikasi siap pakai yang disediakan oleh Django secara default untuk mengelola data aplikasi web Anda. Halaman admin ini memungkinkan kita untuk melakukan operasi CRUD (Create, Read, Update, Delete) pada model yang telah kita daftarkan, tanpa perlu membuat antarmuka pengguna (UI) dari nol.

### Membuat Superuser

Untuk dapat masuk ke halaman admin, kita perlu membuat **superuser** terlebih dahulu. Superuser adalah akun dengan hak akses penuh yang dapat mengelola semua aspek dari aplikasi Django.

**1. Jalankan Perintah `createsuperuser`**

Buka terminal dan pastikan Anda berada di direktori proyek Django Anda (`website_django`). Jalankan perintah berikut:
```bash
python manage.py createsuperuser
```

**2. Isi Detail Akun**

Ikuti instruksi di terminal untuk memasukkan **username**, **email**, dan **password** untuk superuser Anda.

### Mengakses Halaman Admin

Setelah superuser berhasil dibuat, jalankan server pengembangan Django:
```bash
python manage.py runserver
```

Buka browser dan akses halaman admin Django di `http://127.0.0.1:8000/admin/`. Masukkan username dan password superuser yang telah Anda buat untuk masuk.

Jika berhasil, Anda akan melihat halaman admin Django. Untuk saat ini, hanya model `Users` dan `Groups` yang tersedia secara default. Model `Post` yang kita buat sebelumnya belum muncul karena kita belum mendaftarkannya.

### Menambahkan Model Post ke Django Admin

Agar model `Post` yang kita buat di aplikasi `blogs` dapat dikelola melalui halaman admin, kita perlu mendaftarkannya di file `blogs/admin.py`.

**1. Buka file `blogs/admin.py`**

**2. Tambahkan kode berikut untuk mendaftarkan model `Post`:**

```python
from django.contrib import admin
from .models import Post

admin.site.register(Post)
```
Kode ini mengimpor model `Post` dan memberitahu Django untuk menampilkannya di halaman admin.

**3. Verifikasi di Halaman Admin**

Simpan perubahan pada file `admin.py`. Sekarang, segarkan halaman admin di browser Anda (`http://127.0.0.1:8000/admin/`). Anda akan melihat bagian "Blogs" dengan model "Posts" yang telah terdaftar. Anda sekarang dapat menambahkan, mengedit, dan menghapus postingan blog melalui antarmuka admin ini.

### Kesimpulan

Django Admin adalah alat yang sangat berguna untuk mengelola data aplikasi. Dengan mengikuti langkah-langkah di atas, Anda dapat dengan mudah membuat superuser dan mendaftarkan model ke halaman admin.

Pada [bagian selanjutnya](./05-urls-and-views.md), kita akan mulai menampilkan data ini di halaman web untuk pengguna.