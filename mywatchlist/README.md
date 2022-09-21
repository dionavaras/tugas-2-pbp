# Tugas 3 PBP

Link menuju aplikasi Heroku : https://tugas-2-diona.herokuapp.com/mywatchlist/

## Perbedaan antara JSON, XML, dan HTML

JavaScript Object Notation (JSON) adalah format berbasis teks standar untuk mewakili data terstruktur berdasarkan sintaks objek JavaScript. Biasanya digunakan untuk mentransmisikan data dalam aplikasi web. Extensible Markup Language (XML) adalah bahasa markup dan format file untuk menyimpan, mentransmisikan, dan merekonstruksi data arbitrer. XML (Extensible Markup Language) adalah bahasa markup yang mirip dengan HTML, tetapi tanpa tag yang telah ditentukan. HTML (HyperText Markup Language) adalah kode yang digunakan untuk menyusun halaman web dan isinya. Tag HTML digunakan untuk menampilkan data, tetapi tag XML digunakan untuk mendeskripsikan data bukan untuk ditampilkan. Tag HTML adalah tag yang telah ditentukan sebelumnya dan tag XML adalah tag yang ditentukan pengguna.JSON adalah cara untuk merepresentasikan objek sedangkan XML adalah bahasa markup dan menggunakan struktur tag untuk mewakili item data. File JSON sangat mudah dibaca dibandingkan dengan XML yang dokumen-dokumennya relatif sulit untuk dibaca dan ditafsirkan. 

## Mengapa perlu data delivery

Kita memerlukan data delivery dalam pengimplementasian sebuah platform karena data delivery dapat mempermudah proses pengiriman data antar komputer dan platform. Data dalam proses pengiriman tersebut biasanya berbentuk HTML, XML, dan JSON.

## Cara implementasi
1. Membuat suatu aplikasi baru bernama mywatchlist dengan perintah `py manage.py startapp mywatchlist`
2. Menambahkan path mywatchlist dengan menambahkan `path('mywatchlist/', include('mywatchlist.urls')),` pada `urls.py` dan `'mywatchlist'` pada `INSTALLED_APPS` di folder project_django. 
3. Membuat fungsi berikut untuk mengembalikan data dalam bentuk HTML, JSON, XML
```bash
def show_mywatchlist(request):
    data_movie = MovieWatchlist.objects.all()
    context = {
        'list_movie': data_movie,
        'name': 'Diona Varastika',
        'npm': '2106708255'
    }
    return render(request, "mywatchlist.html", context)

def show_watchlink(request):
    context = {
        'name': 'Diona Varastika',
        'npm': '2106708255'
    }
    return render(request, "watchlink.html", context)

def show_xml(request):
    data = MovieWatchlist.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = MovieWatchlist.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")
```
4. Menambahkan kode berikut ke urls.py folder mywatchlist untuk membuat routing sehingga dapat pengguna dapat mengakses http://localhost:8000/mywatchlist 
```
urlpatterns = [
    path('', show_watchlink, name='show_watchlink'),
    path('html/', show_mywatchlist, name='show_mywatchlist'),
    path('xml/', show_xml, name='show_xml'),
    path('json/', show_json, name='show_json'),
]
```
5. Membuka file `models.py` yang ada di folder mywatchlist dan menambahkan potongan kode berikut.
```bash
class MovieWatchlist(models.Model):
    watched = models.BooleanField()
    title = models.CharField(max_length=255)
    rating  = models.IntegerField(validators=[MaxValueValidator(5), MinValueValidator(1)])
    release_date = models.DateField()
    review  = models.TextField()
```
6. Menambahkan 10 data untuk objek MyWatchList pada file `initial_watchlist_data.json`
7. Menjalankan perintah `python manage.py makemigrations` dan `python manage.py migrate` untuk melakukan migrasi

## HTML
![image](https://user-images.githubusercontent.com/112402619/191556347-dadb5124-1811-4e92-a2c9-d6fdab999667.png)

## XML
![image](https://user-images.githubusercontent.com/112402619/191556537-49cb21dd-9686-4012-914d-893d7409b1e8.png)

## JSON
![image](https://user-images.githubusercontent.com/112402619/191556735-8a59dd9e-7608-4ca3-a418-6118b45148c5.png)
