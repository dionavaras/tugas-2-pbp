# Tugas 4 PBP

Link menuju aplikasi Heroku : https://tugas-2-diona.herokuapp.com/todolist/

## Apa kegunaan {% csrf_token %} pada elemen <form>? Apa yang terjadi apabila tidak ada potongan kode tersebut pada elemen <form>?

Django memiliki tag {% csrf_token %} yang diimplementasikan untuk menghindari serangan berbahaya. Hal ini menghasilkan token di sisi server saat merender halaman dan memastikan untuk memeriksa ulang token ini untuk setiap permintaan yang masuk kembali. Jika permintaan yang masuk tidak berisi token, permintaan tersebut tidak akan dieksekusi. {% csrf_token %} diperlukan untuk mengamankan formulir login dari serangan CSRF. Apabila tidak ada potongan kode tersebut pada elemen <form>, akan rentan terhadap semacam serangan "phishing" sehingga halaman login yang rentan terhadap CSRF memungkinkan penyerang untuk berbagi akun pengguna dengan korban.

## Apakah kita dapat membuat elemen <form> secara manual (tanpa menggunakan generator seperti {{ form.as_table }})? Jelaskan secara gambaran besar bagaimana cara membuat <form> secara manual.

Ya, kita dapat membuat elemen <form> secara manual tanpa {{ form.as_table }}. Caranya adalah dengan membuat file dulu seperti forms.py dan membuat table dan tr yang berisi elemen seperti text dan option yang dapat diisi oleh user dengan `<input>`. Jika posisinya masih belum rapih, dapat diatur dengan CSS. Lalu terakhir membuat elemen submit.
