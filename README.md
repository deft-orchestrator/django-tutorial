




# Part 4: Mengelola Data Blog melalui Django Admin

## Ringkasan
Pada part 4, kita akan mengelola data postingan blog menggunakan halaman admin bawaan Django.

## Sebelumnya
Di part 3, kita sudah membuat model `Post` dan melakukan migrasi database.

## Langkah di Part 4
1. Membuat superuser dengan perintah:
	```bash
	python manage.py createsuperuser
	```
2. Menjalankan server dan mengakses halaman admin di `http://127.0.0.1:8000/admin/`.
3. Mendaftarkan model `Post` ke admin di `blogs/admin.py` agar bisa dikelola melalui halaman admin.

Ikuti panduan detail di [tutorial/04-django-admin.md](tutorial/04-django-admin.md).

## Hasil Akhir
- Model `Post` bisa dikelola (CRUD) melalui halaman admin Django.

## Selanjutnya
- Di part 5, kita akan membuat routing URL dan views untuk menampilkan data blog di website.