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
Tag <div> pada HTML digunakan untuk mengelompokkan elemen atau bermacam-macam tag agar menjadi suatu grup. Tag div ini juga sering digunakan untuk mendefinisikan ID atau Class dari CSS. Tag <body> biasanya digunakan untuk membuka dan menutup semua isian yang terdapat di dalam dokumen HTML, seperti text, grafik, link, dan lain-lain. Tag <br> adalah untuk membuat baris baru.
<button>	Specifies a push button
<b>	Specifies bold text
<head>	Specifies information about the document
<h1> to <h6>	Specifies header 1 to header 6
<input>	Specifies an input field
<label>	Specifies a label for a form control
<p>	Specifies a paragraph
<textarea>	Specifies a text area
<thead>	Specifies a table header
Tag <tr> (tabel row) untuk membuat baris. Tag <td> (table data) untuk membuat sel. Tag <th> (table head) untuk membuat judul pada header.

## Tipe CSS Selector
