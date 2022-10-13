# README.md Tugas 6 PBP

## Jelaskan perbedaan antara asynchronous programming dengan synchronous programming.

Asynchronous adalah arsitektur non-blocking, sehingga pelaksanaan satu tugas tidak bergantung pada yang lain. Tugas dapat berjalan secara bersamaan. Synchronous adalah arsitektur pemblokiran, sehingga pelaksanaan setiap operasi tergantung pada penyelesaian yang sebelumnya. Setiap tugas membutuhkan jawaban sebelum melanjutkan ke iterasi berikutnya.

## Dalam penerapan JavaScript dan AJAX, terdapat penerapan paradigma Event-Driven Programming. Jelaskan maksud dari paradigma tersebut dan sebutkan salah satu contoh penerapannya pada tugas ini.

Event-driven programming adalah paradigma pemrograman di mana aliran program ditentukan oleh peristiwa seperti tindakan pengguna (klik mouse, penekanan tombol), keluaran sensor, atau pesan dari program lain. Contoh penerapannya pada tugas ini adalah $("#create-btn").click(function() dimana button "create new task" akan diclick.

## Jelaskan penerapan asynchronous programming pada AJAX.

Setelah halaman HTML dimuat, data dibaca dari server web. Tanpa perlu memuat ulang halaman web, data dapat diperbarui. Transfer data terjadi ke server web pada background. Ketika method POST selesai dieksekusi, program akan langsung memanggil fungsi add_task pada views, kemudian website akan menampilkan card yang baru saja dibuat. Sehingga user tidak perlu merefresh page pada browser untuk melihat card baru yg telah dibuat.

## Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas.

1. Membuat function def show_json pada views.py untuk mengembalikan data dalam bentuk JSON
2. Menambahkan path pada urls.py `path('json/', show_json, name='show_json'),`
3. Menambahkan link scr jQuery AJAX pada `<script>` di todolist.html
4. Melakukan request get data `$.get("/todolist/json", function(data)` pada `/todolist/json` di <script> todolist.html untuk menampilkan card yg telah dibuat di web dengan for loop
5. Membuat tombol "+ New Task" yang membuka sebuah modal dengan form untuk menambahkan task dengan menggunakan Bootstrap
6. Modal dapat diisi dengan task title dan description
7. Membuat function def add_task(request): pada views.py untuk mengembalikan data yg telah diinput user berupa JsonResponse
8. Menambahkan path pada urls.py `path('add/', add_task, name='add_task'),`
9. Membuat request post data `$.post("/todolist/add/")` saat create button diclick untuk menampilkan data yg telah diinput di modal sebagai card baru pada web utama
10. Menambahkan `data-bs-dismiss="modal"` pada tombol Create Task untuk menutup modal saat new task di create.
11. Program akan melakukan refresh pada halaman utama secara asinkronus untuk menampilkan list terbaru tanpa reload seluruh page.
