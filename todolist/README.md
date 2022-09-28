# Tugas 4 PBP

Link menuju aplikasi Heroku : https://tugas-2-diona.herokuapp.com/todolist/

## Apa kegunaan {% csrf_token %} pada elemen <form>? Apa yang terjadi apabila tidak ada potongan kode tersebut pada elemen <form>?

Django memiliki tag {% csrf_token %} yang diimplementasikan untuk menghindari serangan berbahaya. Ini menghasilkan token di sisi server saat merender halaman dan memastikan untuk memeriksa ulang token ini untuk setiap permintaan yang masuk kembali. Jika permintaan yang masuk tidak berisi token, permintaan tersebut tidak akan dieksekusi. Secara umum, Anda perlu mengamankan formulir login Anda dari serangan CSRF seperti yang lainnya. Jika tidak, situs Anda rentan terhadap semacam serangan "phishing domain tepercaya". Singkatnya, halaman login yang rentan terhadap CSRF memungkinkan penyerang untuk berbagi akun pengguna dengan korban.

## Apakah kita dapat membuat elemen <form> secara manual (tanpa menggunakan generator seperti {{ form.as_table }})? Jelaskan secara gambaran besar bagaimana cara membuat <form> secara manual.

In your geeks app make a new file called forms.py where you would be making all your forms. Form is working properly but visuals are disappointing, We can render these fields manually to improve some visual stuff. Each field is available as an attribute of the form using {{ form.name_of_field }},Let’s modify our form to look pretty impressive, {{ field }} attributes
