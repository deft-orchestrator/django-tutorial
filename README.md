






# Part 6: Menampilkan Data Blog dengan Template

## Ringkasan
Pada part 6, kita akan menampilkan data postingan blog dari database ke halaman web menggunakan template HTML.

## Sebelumnya
Di part 5, kita sudah membuat routing URL dan views untuk halaman blog sederhana.

## Langkah di Part 6
1. Membuat template HTML `post_list.html` di `blogs/templates/blogs/`.
2. Membuat view `post_list` di `blogs/views.py` untuk mengambil data dari model `Post` dan menampilkannya di template.
3. Update routing URL di `blogs/urls.py` agar mengarah ke view `post_list`.

Ikuti panduan detail di [tutorial/06-list-view-and-templates.md](tutorial/06-list-view-and-templates.md).

## Hasil Akhir
- Website sudah bisa menampilkan daftar postingan blog dari database secara dinamis.

## Selanjutnya
- Di part 7, kita akan menampilkan detail postingan blog di halaman khusus.