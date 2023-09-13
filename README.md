# TUGAS 2
### Fiona Ratu Maheswari
### 2206024575

**Link Adaptable: https://teyvat-item-tracker.adaptable.app/main/**

**- Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).**

1. Membuat direktori baru bernama Teyvat_Item_Tracker di direktori lokal dan repository baru berjudul sama di GitHub.
2. Inisiasi Git pada direktori Teyvat_Item_Tracker dan menghubungkan direktori lokal dengan repository GitHub.
3. Membuat virtual environment terlebih dahulu.
4. Melakukan instalasi dependencies pada virtual environment.
5. Mengizinkan akses kepada semua host.
6. Menambahkan .gitignore pada direktori.
7. Membuat aplikasi baru bernama main.
8. Menambahkan aplikasi main ke dalam proyek.
9. Membuat folder templates lalu membuat main.html.
10. Membuat model Item pada models.py dengan atribut name, description, amount, dan category.
11. Membuat fungsi show_main pada views.py yang berisi data yang akan ditampilkan.
12. Melakukan routing URL aplikasi main dengan membuat berkas urls.py lalu mengisinya dengan path menggunakan show_main.
13. Melakukan routing  URL Proyek menggunakan fungsi include dan menambahkan rute URL ke dalam urlpatterns.
14. Membuat unit test seperti pada tutorial dan menjalankan test.
15. Melakukan push ke repository GitHub.

**- Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html.**

![Bagan](Bagan_Request_Client.png)

**- Jelaskan mengapa kita menggunakan virtual environment? Apakah kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environment?**

Kita sebaiknya menggunakan virtual environment agar proyek-proyek lainnya yang kita miliki tidak terganggu dan agar dependencies yang kita gunakan pada proyek-proyek yang kita miliki tidak konflik versi.

**- Jelaskan apakah itu MVC, MVT, MVVM dan perbedaan dari ketiganya.**

**MVC** adalah sebuah pendekatan arsitektur perangkat lunak yang digunakan dalam pengembangan aplikasi dimana **Controller** sebagai penghubungnya.
Model: Model mengelola data aplikasi, berkomunikasi dengan database, dan menjalankan logika bisnis.
View: View mengatur tampilan aplikasi dan tidak memiliki logika bisnis.
Controller: Controller menerima input dari pengguna, memprosesnya, dan memutuskan tindakan yang akan diambil berdasarkan input tersebut.

**MVT** adalah sebuah pendekatan arsitektur perangkat lunak yang digunakan dalam pengembangan aplikasi dimana **Template** sebagai penghubungnya.
Model: Komponen yang berhubungan dengan data dan logika bisnis.
View: View bertanggung jawab untuk menampilkan data kepada pengguna.
Template: Berisi kode HTML dengan syntax template yang disediakan dan digunakan untuk mengatur tampilan aplikasi.

**MVVM** adalah sebuah pendekatan arsitektur perangkat lunak yang digunakan dalam pengembangan aplikasi dimana **Template** sebagai penghubungnya.
Model: Komponen yang berhubungan dengan data dan logika bisnis.
View: View bertanggung jawab untuk menampilkan data kepada pengguna.
ViewModel: ViewModel berisi logika tampilan (UI logic) yang menghubungkan Model dengan View. Ini memungkinkan tampilan untuk berkomunikasi dengan Model tanpa harus mengetahui detailnya.

**Perbedaan utama MVC, MVT, dan MVVM:**
MVC akan menerima input pada Controller lalu diarahkan ke view (Controller menjadi penghubung view dengan model), sedangkan pada MVT dan MVVM akan menerima input dan diarahkan ke view langsung. Lalu untuk MVT sendiri, setelah view mendapatkan data dari model, maka view akan menyalurkan data untuk tampilan ke template, lalu template akan memberikan respon ke user melalui urls. Khusus MVVM, ViewModel menjadi penghubung antara view dengan model.