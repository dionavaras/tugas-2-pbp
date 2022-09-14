# Tugas 2 PBP

Link menuju aplikasi Heroku : https://tugas-2-diona.herokuapp.com/katalog/


## Diagram request client ke web aplikasi berbasis Django beserta responnya
![Presentation1](https://user-images.githubusercontent.com/112402619/190239170-c5161240-66dd-4753-9d47-486d1965aa8f.jpg)
User akan mengirim request ke server melalui browser. Setelah menerima permintaan, Django mencari jika ada tanggapan yang sesuai untuk request ini. Django mendapatkan request pengguna dengan pencari URL dan meneruskannya ke view. Jika tidak ada view untuk permintaan ini maka tidak ada tanggapan. View berbicara ke model dan template untuk mengirim tanggapan atas permintaan. View juga bertanggung jawab untuk menerima permintaan web dan mengembalikan respons web yang sesuai. Model berisi data yang diperlukan untuk permintaan tertentu. View akan memanggil query ke model dan database akan mengembalikan hasil query dalam view. Setelah itu, akan berlanjut ke template. Template tidak lain adalah komponen front-end dari aplikasi Django. Template berisi output HTML statis dari halaman web serta informasi dinamis. HTML tersebut dikembalikan ke user sebagai respons.

## Jelaskan kenapa menggunakan virtual environment? Apakah kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environment?
Virtualenv can help you create a separate environment where you don't need root privileges as well as be able to tailor the environment according to your need. It consists of self-contained python installation which only interacts with your specific created environment. A virtualenv enabling you to create seperate virtual (development) environments that aren't tied to each other and can be activated and deactivated easily when you're done. kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environment, tetapi package akan terinstall ke global package. Tidak menggunakan virtualenv meningkatkan risiko error pada open-source project.

## Implementasi poin 1-4
1. Membuat repositori baru bernama tugas-2-diona. Menyalin URL clone dengan HTTPS. Membuka command prompt dan mengeksekusi perintah git clone <URL repo>.
2. Masuk ke dalam direktori tugas-2-diona pada cmd. Membuat virtual environment dengan mengeksekusi perintah 
```bash
python -m venv env
```
3. Menyalakan virtual environment dengan mengeksekusi perintah
```bash
env\Scripts\activate.bat
pip install -r requirements.txt
```
4. Membuka views.py pada folder katalog dan membuat sebuah fungsi yang menerima parameter request dan mengembalikan render(request, "katalog.html").
```python
def show_katalog(request):
    return render(request, "katalog.html")
```
5. Melakukan routing terhadap fungsi views dengan membuat berkas dalam folder katalog bernama urls.py
```python
from django.urls import path
from katalog.views import show_katalog
 
app_name = 'katalog'
 
urlpatterns = [
    path('', show_katalog, name='show_katalog'),
]
```
6. Mendaftarkan aplikasi katalog ke dalam urls.py yang ada pada folder project_django dengan menambahkan potongan kode berikut pada variabel urlpatterns.
```python
path('katalog/', include('katalog.urls')),
```
7. import models yang sudah kamu buat sebelumnya ke dalam file views.py:
```python
from django.shortcuts import render
from katalog.models import CatalogItem
```
8. Menambahkan potongan kode di bawah ini ke dalam fungsi show_wishlist
```python
item_catalog = CatalogItem.objects.all()
    context = {
        'list_barang': item_catalog,
        'nama': 'Diona',
        'npm': 2106708255,
    }
return render(request, "wishlist.html", context)
```
9. Membuka file katalog.html dan mengubah Fill me! menjadi :
```python
<h5>Name: </h5>
  <p>{{nama}}</p>
 
  <h5>Student ID: </h5>
  <p>{{npm}}</p>
```
10. Untuk menampilkan daftar item, menambahkan kode berikut:
```python
{% for barang in list_barang %}
    <tr>
        <th>{{barang.item_name}}</th>
        <th>{{barang.item_price}}</th>
        <th>{{barang.item_stock}}</th>
        <th>{{barang.description}}</th>
        <th>{{barang.rating}}</th>
        <th>{{barang.item_url}}</th>
    </tr>
    {% endfor %}
```
11. Menjalankan projek django dengan mengeksekusi perintah python manage.py runserver dan membuka http://localhost:8000/katalog/ untuk memastikan tampilan sudah sesuai
12. Melakukan add, commit, and push pada perubahan
