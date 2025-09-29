


# Part 2: Membuat App Blog

## Ringkasan
Pada part 2, kita akan membuat aplikasi (app) baru bernama `blogs` di dalam proyek Django yang sudah dibuat pada part 1.

## Sebelumnya
Di part 1, kita sudah melakukan setup awal proyek Django dan memiliki struktur dasar project.

## Langkah di Part 2
1. Membuat app baru dengan perintah:
	```bash
	python manage.py startapp blogs
	```
2. Memastikan folder `blogs` sudah ada di dalam `website_django/`.
3. Mendaftarkan app `blogs` ke dalam `INSTALLED_APPS` di `settings.py`.

Ikuti panduan detail di [tutorial/02-creating-an-app.md](tutorial/02-creating-an-app.md).

## Hasil Akhir
- Proyek Django kini memiliki app baru bernama `blogs` yang siap dikembangkan untuk fitur blog.

## Selanjutnya
- Di part 3, kita akan membuat model data untuk blog dan melakukan migrasi database.