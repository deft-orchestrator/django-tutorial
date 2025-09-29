# Part 3: Menambahkan Fitur Post ke Aplikasi Blog

Dalam tutorial ini, kita akan menambahkan fitur `Post` ke aplikasi blog yang telah kita buat sebelumnya.

---

### Membuat Model untuk Blog

Agar kita dapat menyimpan data postingan blog, kita perlu membuat **model**. Model adalah representasi dari tabel di database. Kita akan membuat model untuk postingan blog yang berisi judul, konten, dan tanggal publikasi.

Buka file `blogs/models.py` dan tambahkan kode berikut:

```python
from django.db import models
from django.utils import timezone

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    published_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return str(self.title)
```
Di Django, Model adalah kelas Python yang merepresentasikan sebuah tabel di database Anda. Setiap atribut dari model mewakili sebuah kolom tabel.

### Membuat dan Menjalankan Migrasi

Setelah membuat atau mengubah model, kita perlu menerapkan perubahan ini ke database. Proses ini melibatkan dua langkah:
1.  Membuat file migrasi.
2.  Menerapkan migrasi tersebut ke database.

**1. Membuat File Migrasi**

Jalankan perintah berikut di terminal:

```bash
python manage.py makemigrations
```

Perintah `makemigrations` akan membuat file migrasi berdasarkan perubahan yang kita buat di model. Hasil dari perintah ini adalah sebuah file migrasi yang berisi instruksi untuk membuat tabel `Post` di database. File migrasi ini disimpan di dalam folder `blogs/migrations/`.

Struktur folder Anda akan terlihat seperti ini:

```
blogs/
└── migrations/
    ├── __init__.py
    └── 0001_initial.py  <-- File migrasi baru
```

**2. Menerapkan Migrasi ke Database**

Setelah berhasil membuat file migrasi, langkah selanjutnya adalah menerapkan migrasi tersebut ke database dengan perintah berikut:

```bash
python manage.py migrate
```

Jika perintah ini berhasil dijalankan, maka tabel `Post` akan dibuat di database sesuai dengan definisi model yang telah kita buat.

### Kesimpulan

Dalam tutorial ini, kita telah berhasil menambahkan fitur `Post` ke aplikasi blog dengan membuat model untuk postingan blog dan menerapkan migrasi ke database.

Selanjutnya, kita akan belajar bagaimana [mengelola data postingan blog melalui halaman admin Django](./04-django-admin.md).