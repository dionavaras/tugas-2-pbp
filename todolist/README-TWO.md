# README.md Tugas 6 PBP

## Jelaskan perbedaan antara asynchronous programming dengan synchronous programming.

Asynchronous adalah arsitektur non-blocking, sehingga pelaksanaan satu tugas tidak bergantung pada yang lain. Tugas dapat berjalan secara bersamaan. Synchronous adalah arsitektur pemblokiran, sehingga pelaksanaan setiap operasi tergantung pada penyelesaian yang sebelumnya. Setiap tugas membutuhkan jawaban sebelum melanjutkan ke iterasi berikutnya.

## Dalam penerapan JavaScript dan AJAX, terdapat penerapan paradigma Event-Driven Programming. Jelaskan maksud dari paradigma tersebut dan sebutkan salah satu contoh penerapannya pada tugas ini.

Event-driven programming adalah paradigma pemrograman di mana aliran program ditentukan oleh peristiwa seperti tindakan pengguna (klik mouse, penekanan tombol), keluaran sensor, atau pesan dari program lain. Contoh penerapannya pada tugas ini adalah $("#create-btn").click(function() dimana button "create new task" akan diclick.

## Jelaskan penerapan asynchronous programming pada AJAX.

Setelah halaman HTML dimuat, data dibaca dari server web. Tanpa perlu memuat ulang halaman web, data dapat diperbarui. Transfer data terjadi ke server web pada background. Ketika method POST selesai dieksekusi, program akan langsung memanggil fungsi add_task pada views, kemudian website akan menampilkan card yang baru saja dibuat. Sehingga user tidak perlu merefresh page pada browser untuk melihat card baru yg telah dibuat.

## Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas.
