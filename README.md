







# Part 7: Menampilkan Detail Postingan Blog

## Ringkasan
Pada part 7, kita akan menampilkan detail setiap postingan blog di halaman khusus ketika judul diklik.

## Sebelumnya
Di part 6, kita sudah menampilkan daftar postingan blog dari database menggunakan template.

## Langkah di Part 7
1. Membuat view `post_detail` di `blogs/views.py` untuk menampilkan detail postingan berdasarkan ID.
2. Membuat template HTML `post_detail.html` di `blogs/templates/blogs/` untuk menampilkan detail postingan.
3. Update routing URL di `blogs/urls.py` agar mendukung halaman detail postingan.
4. Update template `post_list.html` agar judul postingan menjadi link ke halaman detail.

Ikuti panduan detail di [tutorial/07-detail-view.md](tutorial/07-detail-view.md).

## Hasil Akhir
- Website sudah bisa menampilkan detail setiap postingan blog di halaman khusus.

## Selesai
- Tutorial selesai! Anda sudah memiliki aplikasi blog sederhana dengan Django.