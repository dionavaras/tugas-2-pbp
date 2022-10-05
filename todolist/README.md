# Tugas 4 PBP

Link menuju aplikasi Heroku : https://tugas-2-diona.herokuapp.com/todolist/

## Apa kegunaan {% csrf_token %} pada elemen <form>? Apa yang terjadi apabila tidak ada potongan kode tersebut pada elemen <form>?

Django memiliki tag {% csrf_token %} yang diimplementasikan untuk menghindari serangan berbahaya. Hal ini menghasilkan token di sisi server saat merender halaman dan memastikan untuk memeriksa ulang token ini untuk setiap permintaan yang masuk kembali. Jika permintaan yang masuk tidak berisi token, permintaan tersebut tidak akan dieksekusi. {% csrf_token %} diperlukan untuk mengamankan formulir login dari serangan CSRF. Apabila tidak ada potongan kode tersebut pada elemen <form>, akan rentan terhadap semacam serangan "phishing" sehingga halaman login yang rentan terhadap CSRF memungkinkan penyerang untuk berbagi akun pengguna dengan korban.

## Apakah kita dapat membuat elemen <form> secara manual (tanpa menggunakan generator seperti {{ form.as_table }})? Jelaskan secara gambaran besar bagaimana cara membuat <form> secara manual.

Ya, kita dapat membuat elemen `<form>` secara manual tanpa {{ form.as_table }}. Caranya adalah dengan membuat file dulu seperti forms.py dan membuat `<table>` dan `<tr>` yang berisi elemen seperti text dan option yang dapat diisi oleh user dengan `<input>`. Jika posisinya masih belum rapih, dapat diatur dengan CSS. Lalu terakhir membuat elemen submit.
  
## Jelaskan proses alur data dari submisi yang dilakukan oleh pengguna melalui HTML form, penyimpanan data pada database, hingga munculnya data yang telah disimpan pada template HTML.
  
Saat user melakukan submisi melalui HTML form dengan mengeklik tombol submit, data yang telah diinput oleh user pada form akan dapat diakses dengan request POST. Lalu data tersebut akan dicek apakah sesuai atau tidak, jika valid maka akan disimpan pada database. Untuk dapat mengakses data yang telah disimpan, dapat menggunakan Models.objects.filter(user=request.user) sesuai dengan akun user. Lalu pada HTML akan dilakukan pemanggilan data melalui context pada views.py untuk menampilkan data.
  
## Implementasi checklist
  
1. Pertama, membuat suatu aplikasi baru bernama todolist dengan menjalankan perintah `py manage.py startapp todolist` pada cmd
2. Menambahkan path todolist dengan memasukkan `path('todolist/', include('todolist.urls')),` pada urls.py di project_django
3. Membuat models.py dengan atribut sebagai berikut di folder todolist
```bash
  class TodolistModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()
    title = models.CharField(max_length=255)
    description  = models.TextField()
```
4. Membuat fungsi register, show_todolist, login_user, show_newtask dan logout_user pada views.py folder todolist untuk membuat form registrasi, login, membuat task baru, halaman utama dan logout yang dihubungkan pada HTML. Membuat fungsi show_newtask dan show_todolist dengan login_required agar user perlu masuk ke akunnya untuk mengakses halaman. Pada halaman new task, user dapat memasukkan title dan description dari tugas. 
5. Membuat halaman utama todolist yang memuat username, tombol New Task, tombol logout, dan tabel to do list dengan meloop data todo yang ada pada context  show_todolist untuk menampilkan data pada todolist.html. Tabel menggunakan `<table>` dan tombol menggunakan `button`
6. Melakukan routing pada folder urls.py :
```bash
  urlpatterns = [
    path('', show_todolist, name='show_todolist'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('create-task/', show_newtask, name='show_newtask'),
]
```
7. Melakukan deployment ke heroku dengan git add ., git commit, dan git push
8. Membuat dua akun dan 3 dummy data yaitu:
```bash
Username : akunpertama
Password : passwordakun1
  
Username : akunkedua
Password : passwordakun2
```
