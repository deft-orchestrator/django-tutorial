



# Part 3: Membuat Model dan Migrasi Database

## Ringkasan
Pada part 3, kita akan membuat model `Post` untuk aplikasi blog dan melakukan migrasi database agar model tersebut tersedia di database.

## Sebelumnya
Di part 2, kita sudah membuat app baru bernama `blogs` dan mendaftarkannya ke Django.

## Langkah di Part 3
1. Membuat model `Post` di `blogs/models.py` dengan field judul, konten, dan tanggal publikasi.
2. Membuat file migrasi dengan perintah:
	```bash
	python manage.py makemigrations blogs
	```
3. Menjalankan migrasi ke database:
	```bash
	python manage.py migrate
	```

Ikuti panduan detail di [tutorial/03-model-and-migrations.md](tutorial/03-model-and-migrations.md).

## Hasil Akhir
- Database sudah memiliki tabel untuk menyimpan postingan blog.
- Model `Post` siap digunakan untuk fitur blog selanjutnya.

## Selanjutnya
- Di part 4, kita akan mengelola data blog melalui halaman admin Django.