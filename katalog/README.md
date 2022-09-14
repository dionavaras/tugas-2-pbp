# Tugas 2 PBP

Link menuju aplikasi Heroku : https://tugas-2-diona.herokuapp.com


## Diagram request client ke web aplikasi berbasis Django beserta responnya
![Presentation1](https://user-images.githubusercontent.com/112402619/190239170-c5161240-66dd-4753-9d47-486d1965aa8f.jpg)
User akan mengirim request ke server melalui browser. Setelah menerima request, Django mencari jika ada response yang sesuai untuk request ini. Django mendapatkan request pengguna dengan pencari URL dan meneruskannya ke view. Jika tidak ada view untuk request ini maka tidak ada response. View berbicara ke model dan template untuk mengirim response atas request. View juga bertanggung jawab untuk menerima request web dan mengembalikan respons web yang sesuai. Model berisi data yang diperlukan untuk request tertentu. View akan memanggil query ke model dan database akan mengembalikan hasil query dalam view. Setelah itu, akan berlanjut ke template. Template tidak lain adalah komponen front-end dari aplikasi Django. Template berisi output HTML statis dari halaman web serta informasi dinamis. HTML tersebut dikembalikan ke user sebagai respons.

## Jelaskan kenapa menggunakan virtual environment? Apakah kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environment?
Virtual environment dapat membantu kita membuat environment terpisah di mana kita tidak memerlukan hak akses root serta dapat menyesuaikan environment sesuai dengan kebutuhan kita. Ini terdiri dari instalasi python mandiri yang hanya berinteraksi dengan environment khusus yang kita buat. Sebuah virtual environment memungkinkan kita untuk membuat lingkungan virtual (pengembangan) terpisah yang tidak terikat satu sama lain dan dapat diaktifkan dan dinonaktifkan dengan mudah. Kita masih dapat membuat aplikasi web berbasis Django tanpa menggunakan lingkungan virtual, tetapi paket tersebut akan diinstal ke dalam paket global. Tidak menggunakan virtual environment meningkatkan risiko error dalam open-source project.

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
4. Melakukan perintah python manage.py makemigrations untuk mempersiapkan migrasi skema model ke dalam database Django lokal. Menjalankan perintah python manage.py migrate untuk menerapkan skema model yang telah dibuat ke dalam database Django lokal. Menjalankan perintah python manage.py loaddata initial_wishlist_data.json untuk memasukkan data tersebut ke dalam database Django lokal. 
5. Membuka views.py pada folder katalog dan membuat sebuah fungsi yang menerima parameter request dan mengembalikan render(request, "katalog.html").
```python
def show_katalog(request):
    return render(request, "katalog.html")
```
6. Melakukan routing terhadap fungsi views dengan membuat berkas dalam folder katalog bernama urls.py
```python
from django.urls import path
from katalog.views import show_katalog
 
app_name = 'katalog'
 
urlpatterns = [
    path('', show_katalog, name='show_katalog'),
]
```
7. Mendaftarkan aplikasi katalog ke dalam urls.py yang ada pada folder project_django dengan menambahkan potongan kode berikut pada variabel urlpatterns.
```python
path('katalog/', include('katalog.urls')),
```
8. Mengimport models yang sudah dibuat sebelumnya ke dalam file views.py:
```python
from django.shortcuts import render
from katalog.models import CatalogItem
```
9. Menambahkan potongan kode di bawah ini ke dalam fungsi show_wishlist
```python
item_catalog = CatalogItem.objects.all()
    context = {
        'list_barang': item_catalog,
        'nama': 'Diona',
        'npm': 2106708255,
    }
return render(request, "wishlist.html", context)
```
10. Membuka file katalog.html dan mengubah Fill me! menjadi :
```python
<h5>Name: </h5>
  <p>{{nama}}</p>
 
  <h5>Student ID: </h5>
  <p>{{npm}}</p>
```
11. Untuk menampilkan daftar item, menambahkan kode berikut:
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
12. Menjalankan projek django dengan mengeksekusi perintah python manage.py runserver dan membuka http://localhost:8000/katalog/ untuk memastikan tampilan sudah sesuai
13. Melakukan add, commit, and push pada perubahan.
14. Untuk melakukan deployment ke Heroku, menyalin API Key dan app name. Kemudian membuka bagian Secrets untuk GitHub Actions (Settings -> Secrets -> Actions) untuk menambahkan variabel repository secret baru untuk melakukan deployment. Terakhir, membuka tab GitHub Actions dan menjalankan kembali workflow yang gagal.
