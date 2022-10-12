# README.md Tugas 5

## Perbedaan dari Inline, Internal, dan External CSS

Pada Inline CSS, styles CSS diterapkan dalam tag HTML itu sendiri menggunakan parameter style.
`<h1 style=”color: red; font-size: 3rem;”>hello world</h1>`
Inline digunakan ketika jumlah styles yang dibutuhkan lebih sedikit atau ketika hanya satu elemen yang harus distyles. Metode ini membuat tag terlihat sangat jelek dan menyulitkan untuk menemukan kesalahan. 
Pros : Dapat dengan mudah dan cepat memasukkan CSS ke halaman HTML. Tidak perlu membuat dan mengunggah dokumen terpisah seperti pada gaya eksternal.
Cons: Menambahkan aturan CSS ke setiap elemen HTML memakan waktu dan membuat struktur HTML berantakan. Menata beberapa elemen dapat memengaruhi ukuran halaman dan waktu pengunduhan.

Pada Internal CSS, styles CSS diterapkan dalam file HTML yang sama. Setiap tag HTML dirancang secara terpisah dalam file yang sama. Internal digunakan jika satu dokumen html memiliki style yang unik dan beberapa elemen perlu ditata untuk mengikuti format tertentu. CSS Internal digunakan dengan menambahkan tag <style> di bagian <head> dokumen HTML.
Pros : Dapat menggunakan ID dan class selector pada style. Tidak perlu mengunggah banyak file.
Cons : Menambahkan kode ke dokumen HTML dapat meningkatkan ukuran halaman dan waktu pemuatan.

Pada External CSS, CSS diterapkan ke setiap elemen dalam file CSS yang berbeda. Jenis CSS ini adalah metode yang lebih efisien, terutama untuk menata situs web besar. Dengan mengedit satu file .css, dapat mengubah seluruh situs sekaligus. Ini adalah metode terbaik untuk penataan gaya karena dapat menemukan CSS untuk semua elemen dalam satu file tertentu dan mempermudah proses debug. Dengan CSS eksternal, perlu menghubungkan file CSS eksternal ke file HTML.
Pros : Karena kode CSS berada dalam dokumen terpisah, file HTML akan memiliki struktur yang lebih bersih dan ukurannya lebih kecil. Dapat menggunakan file .css yang sama untuk beberapa halaman.
Cons : Tampilan mungkin tidak dirender dengan benar hingga CSS eksternal dimuat. Mengunggah atau menautkan ke beberapa file CSS dapat meningkatkan waktu pengunduhan situs.

## Tag HTML 5
Tag `<div>` pada HTML digunakan untuk mengelompokkan elemen atau bermacam-macam tag agar menjadi suatu grup. Tag div ini juga sering digunakan untuk mendefinisikan ID atau Class dari CSS. Tag `<body>` biasanya digunakan untuk membuka dan menutup semua isian yang terdapat di dalam dokumen HTML, seperti text, grafik, link, dan lain-lain. Tag `<br>` adalah untuk membuat baris baru. Tag `<button>` digunakan untuk membuat button. Tag `<b>`	digunakkan untuk membuat tulisan menjadi bold. Tag `<head>` tugasnya adalah memberikan informasi tentang dokumen. Tag `<h1>` sampai `<h6>`	digunakan untuk header level1  sampai 6.
Tag `<input>`	merupakan tag pada HTML yang digunakan untuk menciptakan bidang formulir yang memungkinkan pengguna dalam memasukkan entry data.
Tag `<label>`	sebagai pelengkap keterangan untuk beberapa objek form seperti radio atau checkbox. 
Tag `<p>`	untuk membuat paragraf.
Tag `<textarea>`	untuk membuat textarea.
Tag `<thead>`	untuk membuat table header.
Tag <tr> (tabel row) untuk membuat baris. Tag <td> (table data) untuk membuat sel. Tag <th> (table head) untuk membuat judul pada header.

## Tipe CSS Selector
Tipe CSS Selector pertama yang saya ketahui adalah `element selector` yang memilih elemen HTML berdasarkan nama elemen. Yang kedua adalah `id selector` yang menggunakan atribut id dari elemen HTML untuk memilih elemen tertentu. Untuk memilih elemen dengan id tertentu, tulis karakter hash (#), diikuti dengan id elemen. Yang ketiga adalah `class selector` yang memilih elemen HTML dengan atribut kelas tertentu. Untuk memilih elemen dengan kelas tertentu, tulis karakter titik (.), diikuti dengan nama kelas. Lalu ada `universal selector` memilih semua elemen HTML pada halaman. `Grouping selector` memilih semua elemen HTML dengan definisi style yang sama. Untuk group selector, pisahkan setiap pemilih dengan koma.
  
## Implementasi
Saya mengkostumisasi template HTML yang telah dibuat pada Tugas 4 dengan menggunakan CSS dan Bootstrap. CSS saya gunakan untuk membuat background, button, dan mengkostumisasi tulisan dan input, saya menggunakan margin, text-align, dan justify content untuk menengahkan elemen. Menggunakan font-family, text-shadow, dan color untuk mengkostumisasi tampilan tulisan. Saya jg menggunakan CSS untuk membuat tampilan hover pada card. Saya menggunakan bootstrap untuk membuat card. Langkah pertama yang saya lakukan dengan bootstrap adalah menambahkan link `<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-Zenh87qX5JnK2Jl0vWa8Ck2rdkQ2Bzep5IDxbcnCeuOxjzrPF/et3URy9Bv1WTRi" crossorigin="anonymous">` dan `<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.2.2/dist/js/bootstrap.bundle.min.js" integrity="sha384-OERcA2EqjJCMA+/3y+gxIOqMEjwtxJY7qPCqsdltbNJuaOe923+mo//f6V8Qbsw3" crossorigin="anonymous"></script>` pada head html di base.html. Saya membuat card dengan menambahkan class card pada html. Untuk membuat website menjadi responsive, bootstrap telah menyediakan sifat responsive bawaaannya.
