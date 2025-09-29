# Part 5: Mengenal Routing URL dan Views di Django

Pada bagian sebelumnya, kita telah mempelajari tentang model dan bagaimana mengelola data melalui halaman admin. Tahapan selanjutnya adalah menampilkan data tersebut di halaman web menggunakan **views** dan **routing URL**.

File `urls.py` dan `views.py` adalah dua file inti yang bekerja sama untuk menangani permintaan (*request*) dari pengguna dan memberikan respons (*response*).

---

### Apa itu Views?

**Views** adalah bagian dari Django yang bertanggung jawab untuk menangani logika bisnis aplikasi web. Views menerima permintaan dari pengguna, memprosesnya (misalnya, dengan mengambil data dari database), dan mengembalikan respons yang sesuai (misalnya, halaman HTML).

Views diatur dalam file `views.py` di setiap aplikasi Django.

### Apa itu Routing URL?

**Routing URL** adalah cara Django mengarahkan permintaan dari pengguna ke fungsi atau kelas yang sesuai di dalam `views.py`. Routing URL diatur dalam file `urls.py`.

Setiap proyek Django memiliki file `urls.py` utama (`website_django/urls.py`), dan setiap aplikasi juga dapat memiliki file `urls.py` sendiri (`blogs/urls.py`).

---

### Contoh Implementasi

Mari kita lihat contoh implementasi routing URL dan views. Kita akan membuat halaman sederhana yang menampilkan judul "Selamat Datang di Blog Saya".

#### Langkah 1: Membuat Fungsi View di `views.py`

Buka file `blogs/views.py` dan tambahkan fungsi view berikut untuk menampilkan halaman blog:

```python
from django.http import HttpResponse

def home(request):
    html_header_and_title = "<h1>Selamat Datang di Blog Saya</h1>"
    return HttpResponse(html_header_and_title)
```
Pada kode di atas, kita mengimpor `HttpResponse` untuk mengembalikan respons HTTP sederhana. Fungsi `home` menerima objek `request` dan mengembalikan respons berupa HTML.

#### Langkah 2: Menambahkan Routing URL di Aplikasi `blogs`

Buat file baru bernama `urls.py` di dalam folder `blogs/` (`blogs/urls.py`) dan tambahkan routing URL untuk fungsi view `home`:

```python
from django.urls import path
from .views import home

urlpatterns = [
    path('', home, name='home'),
]
```
Pada kode di atas, fungsi `path()` mendefinisikan sebuah rute:
*   **Pola URL:** String kosong `''` berarti ini adalah URL dasar dari aplikasi `blogs`.
*   **View:** `home` adalah fungsi view yang akan dipanggil ketika pola URL cocok.
*   **Nama:** `name='home'` adalah nama unik untuk pola URL ini, yang bisa kita gunakan untuk merujuknya di tempat lain.

#### Langkah 3: Menghubungkan Routing URL Aplikasi ke Proyek

Sekarang, kita perlu memberitahu proyek utama tentang URL aplikasi `blogs`. Buka file `website_django/urls.py` dan tambahkan routing URL untuk aplikasi `blogs`:

```python
from django.contrib import admin
from django.urls import path, include # <-- Impor 'include'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('blogs/', include('blogs.urls')), # <-- Tambahkan baris ini
]
```
Tambahan `path('blogs/', include('blogs.urls'))` menghubungkan routing URL aplikasi `blogs` ke proyek utama. Dengan ini, setiap permintaan yang dimulai dengan `/blogs/` akan diteruskan ke file `blogs/urls.py` untuk penanganan lebih lanjut.

#### Langkah 4: Menjalankan Server dan Mengakses Halaman Blog

Jalankan server Django:
```bash
python manage.py runserver
```
Buka browser dan akses URL `http://127.0.0.1:8000/blogs/`. Anda akan melihat halaman blog yang telah Anda buat.

### Kesimpulan

Routing URL dan Views adalah dua komponen penting dalam Django. Routing URL mengarahkan permintaan pengguna ke fungsi di Views, sedangkan Views menangani logika dan mengembalikan respons.

Pada [bagian selanjutnya](./06-list-view-and-templates.md), kita akan mempelajari tentang *template* untuk membuat tampilan halaman web yang lebih menarik dan dinamis.