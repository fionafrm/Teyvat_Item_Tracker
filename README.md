# TUGAS 5
### Fiona Ratu Maheswari
### 2206024575

**Jelaskan manfaat dari setiap element selector dan kapan waktu yang tepat untuk menggunakannya.**
Terdapat beberapa element selector yang ada pada CSS.
*1. Universal Selector*
Universal selector digunakan untuk memilih semua elemen dalam dokumen HTML. Biasanya Universal Selector digunakan ketika ingin mereset semua style pada HTML (reset CSS) atau untuk memilih semua elemen dalam konteks tertentu.
*2. Type selector*
Type selector digunakan untuk memilih semua elemen dengan nama elemen yang cocok. Biasanya type selector digunakan ketika kita ingin menerapkan style pada semua elemen yang memiliki nama tertentu.
*3. ID Selector*
ID selector digunakan untuk memilih elemen dengan atribut id tertentu. Biasanya ID selector digunakan ketika kita ingin merancang satu elemen khusus pada halaman web kita.
*4. Class Selector*
Class Selector digunakan untuk memilih semua elemen yang memiliki nama kelas tertentu. Biasanya Class Selector digunakan ketika kita ingin menerapkan style yang sama pada beberapa elemen dengan kelas yang sama.
*5. Descendant Selector*
Descendant Selector digunakan untuk memilih suatu elemen yang merupakan turunan dari elemen lainnya. Biasanya Descendant Selector digunakan ketika kita ingin menerapkan style pada elemen-elemen yang berada dalam konteks tertentu.
*6. Child Selector*
Child Selector digunakan untuk memilih suatu elemen yang merupakan anak langsung dari elemen lainnya. Biasanya Child Selector digunakan ketika kita ingin merancang elemen-elemen yang menjadi anak langsung dari elemen lain, dan tidak peduli dengan elemen anak dari anak tersebut
*7. Adjacent Sibling Selector*
Adjacent Sibling Selector digunakan untuk memilih suatu elemen yang menjadi saudara sejajar elemen lainnya, yaitu elemen yang memiliki elemen yang sama sebagai elemen induk. Biasanya Adjacent Sibling Selector digunakan ketika kita ingin merancang elemen-elemen yang sejajar satu sama lain.
*8. General Sibling Selector*
General Sibling Selector digunakan untuk memilih suatu elemen yang menjadi saudara sejajar elemen lainnya, tanpa peduli hubungan hierarki mereka. Biasanya Adjacent Sibling Selector digunakan ketika kita ingin merancang elemen-elemen yang sejajar satu sama lain, tanpa peduli apakah mereka memiliki elemen induk yang sama.

**Jelaskan HTML5 Tag yang kamu ketahui.**
1. '!DOCTYPE html': Ini adalah deklarasi dokumen yang digunakan mengikuti standar HTML5.
2. html: Ini adalah elemen root yang mengelilingi semua konten halaman web.
3. head: Elemen ini berisi informasi metadata tentang halaman web, seperti judul, karakter set, dan tautan ke file eksternal seperti CSS dan JavaScript.
4. meta: Digunakan untuk mendefinisikan metadata.
5. title: Menentukan judul dari halaman web, yang akan ditampilkan di bilah judul browser.
6. link: Digunakan untuk menghubungkan halaman web dengan file eksternal seperti stylesheet (CSS).
7. style: Ini adalah elemen untuk menyematkan style CSS secara langsung ke dalam halaman HTML.
8. script: Digunakan untuk menambahkan kode JavaScript ke halaman web.
9. body: Ini adalah elemen yang berisi semua konten yang akan ditampilkan di halaman web.
10. header: Digunakan untuk mengelompokkan elemen-elemen yang merupakan bagian atas dari halaman web.
11. nav: Ini adalah elemen yang digunakan untuk mengelompokkan tautan navigasi atau menu halaman web.

**Jelaskan perbedaan antara margin dan padding.**
Margin mengacu pada ruang di luar elemen, dan ini adalah jarak yang mengatur elemen tersebut dengan elemen-elemen lain di sekitarnya. Margin tidak memiliki latar belakang atau warna, dan penggunaannya lebih untuk mengendalikan jarak antara elemen dengan elemen lain. Di sisi lain, padding merujuk pada ruang di dalam elemen, yang mengatur jarak antara batas elemen dan kontennya sendiri. Salah satu perbedaan utama adalah bahwa padding dapat memiliki latar belakang atau warna, sehingga memengaruhi tampilan elemen dan kontennya.


**Jelaskan perbedaan antara framework CSS Tailwind dan Bootstrap. Kapan sebaiknya kita menggunakan Bootstrap daripada Tailwind, dan sebaliknya?**
Bootstrap dan Tailwind CSS adalah dua framework CSS yang dapat digunakan untuk membangun tampilan web yang responsif. Bootstrap menyediakan sejumlah besar komponen dan gaya pra-didefinisikan, sehingga cocok untuk proyek-proyek yang membutuhkan desain cepat dan konsisten. Di sisi lain, Tailwind CSS mengikuti pendekatan "utility-first" yang memberikan tingkat fleksibilitas tinggi dalam menentukan tampilan, tetapi memerlukan lebih banyak penulisan kode CSS khusus. Pemilihan antara keduanya tergantung pada kebutuhan proyek, tingkat desain kustom, dan tingkat fleksibilitas yang Anda inginkan dalam menentukan tampilan web.

**Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).**
1. Menghapus style pada html sebelumnya.
2. Menambahkan style pada html login, register, main, dan create_item, seperti body, .login dan lain-lain. Perubahan yang dilakukan adalah seperti merubah warna dan align items.
3. Memastikan tiap bagian dari tiap file html mendapatkan style.

# TUGAS 4
### Fiona Ratu Maheswari
### 2206024575

**Apa itu Django UserCreationForm, dan jelaskan apa kelebihan dan kekurangannya?**
UserCreationForm digunakan untuk pendaftaran user baru. Form ini diperlukan agar aplikasi dapat melakukan autentikasi.
Kelebihan: UserCreationForm mudah untuk dikostumisasi sehingga kita dapat menggunakannya sesuai dengan kebutuhan kita. Tidak hanya itu, UserCreationForm dapat melalukan validasi otomatis dan telah terintegrasi dengan model User secara default oleh Django, sehingga kita tidak perlu memikirkan tentang validasi user.
Kekurangan: Fiturnya masih terbatas dan tidak cocok untuk validasi yang kompleks.

**Apa perbedaan antara autentikasi dan otorisasi dalam konteks Django, dan mengapa keduanya penting?**
**Autentikasi** adalah proses verifikasi identitas user. Dalam Django, autentikasi artinya memastikan bahwa user tersebut adalah sesuai dengan yang mereka input kepada aplikasi, hal ini bisa dilihat melalui kombinasi username dan password. Autentikasi sangat penting untuk diimplementasikan agar kita dapat mencegah akses tidak sah ke aplikasi.
**Otorisasi** adalah proses pemberian atau penolakan izin kepada user untuk mengakses sumber daya tertentu atau melakukan tindakan tertentu. Hal ini dapat dilakukan setelah melakukan autentikasi. Otorisasi sangat penting untuk diimplementasikan agar kita dapat mencegah terjadinya akses dan tindakan tertentu yang tidak sesuai dengan role user.

Kedua proses ini sangat penting untuk diimplementasikan agar keamanan aplikasi kita terjaga dan user dapat merasa aman terhadap aplikasi yang kita miliki

**Apa itu cookies dalam konteks aplikasi web, dan bagaimana Django menggunakan cookies untuk mengelola data sesi pengguna?**
Cookies adalah mekanisme yang memungkinkan server web untuk menyimpan informasi di browser klien untuk digunakan dalam sesi atau kunjungan berikutnya.

**Apakah penggunaan cookies aman secara default dalam pengembangan web, atau apakah ada risiko potensial yang harus diwaspadai?**
Penggunaan cookies tidak selalu aman dalam pengembangan web. Masih ada beberapa risiko potensial yang harus diwaspadai.
1. Cross-Site Scripting (XSS): Jika web yang kita miliki masih rentan terhadap serangan XSS, maka penyerang dapat mencuri cookies dari user aplikasi kita. Hal ini bisa sangat berbahaya jika cookies tersebut berisi informasi sensitif seperti ID sesi.
2. Third-Party Cookies: Cookies yang ditempatkan oleh domain pihak ketiga dapat digunakan untuk melacak perilaku user di web milik kita. Hal ini dapat melanggar privasi user.
3. Over-reliance on Cookies: Jika informasi sensitif hanya disimpan dalam cookies tanpa enkripsi atau proteksi lainnya, maka hal ini dapat membahayakan informasi user.

**Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).**
1. Menjalankan env pada folder root untuk memulai modifikasi web.
2. Membuat fungsi register dengan parameter request pada views.py di folder main. Lalu tambahkan import redirect, UserCreationForm, dan messages. Lalu mengisi fungsi register agar fungsi tersebut dapat menampilkan form register untuk user, lalu memberikan message jika user berhasil daftar, lalu mengarahkan user ke halaman login.
3. Membuat halaman register dengan membuat file register.html di folder main/templates . Lalu isi file tersebut dengan form yang memiliki method POST dan buat juga button untuk daftar.
4. Melakukan routing halaman register di urls.py milik main dengan melakukan import fungsi register dan menambahkan path register.
5. Membuat fungsi login_user dengan parameter request pada views.py di folder main. Lalu tambahkan import authenticate dan login. Lalu mengisi fungsi login_user agar fungsi tersebut dapat menampilkan form login untuk user, lalu memberikan message jika user berhasil login, lalu mengarahkan user ke halaman main milik user.
6. Membuat halaman login dengan membuat file login.html di folder main/templates . Lalu isi file tersebut dengan form yang memiliki method POST, button untuk login, dan message yang dapat mengarahkan ke halaman register jika user belum memiliki akun.
7. Melakukan routing halaman login di urls.py milik main dengan melakukan import fungsi login_user dan menambahkan path login.
8. Membuat fungsi logout_user dengan parameter request pada views.py di folder main. Lalu tambahkan import logout. Lalu mengisi fungsi logout_user agar fungsi tersebut dapat menghentikan sesi user yang telah login tersebut dan mengarahkan user ke halaman login.
9. Tambahkan button logout pada main.html
10. Melakukan routing halaman logout di urls.py milik main dengan melakukan import fungsi logout_user dan menambahkan path logout.
11. Membuat dua akun dummy dan memasukkan 3 dummy data pada tiap akun.
12. Menambahkan User pada model dengan import User pada models.py .
13. Menambahkan atribut user pada kelas Item.
14. Memodifikasi fungsi create_item pada views.py di main dengan melakukan save item.
15. Mengubah fungsi show_main dimana items akan difilter berdasarkan user.
16. Menambahkan import datetime, HttpResponseRedirect, dan reverse pada views.py. Lalu menambahkan cookies last_login pada login_user dan menambahkan bagian last_login pada show_main. Lalu ubah fungsi logout_user untuk menghapus cookie last_login ketika user logout. Lalu menambahkan messages last_login di main.html .
17. Lalu makemigrations dan migrate karena adanya perubahan model.
18. Lalu menambahkan conditionals untuk melakukan increase, decrease, dan remove Item pada tiap Item di views.py dan menyesuaikannya di main.html .
19. Melakukan push ke github.


# TUGAS 3
### Fiona Ratu Maheswari
### 2206024575

**Apa perbedaan antara form POST dan form GET dalam Django?**

Terdapat beberapa perbedaan antara form POST dan form GET dalam Django.
1. Pada form POST, data formulir akan dikirmkan ke dalam tubuh permintaan HTML-nya sehingga tidak terlihat pada URL, contohnya adalah www.contoh.com/formulir . Sedangkan pada form GET, data formulir akan dikirimkan ke parameter query string dalam URL sehingga isinya akan terlihat pada URL nya, contohnya adalah www.contoh.com/formulir?nama=John&email=john@contoh.com&password=secretpassword .
2. Jika dilihat dari segi keamanan, form POST lebih aman karena tidak menampilkan datanya pada URL. Sedangkan, form GET lebih berisiko karena menampilkan datanya pada URL.
3. Tidak ada batasan panjang URL pada form POST. Sedangkan pada form GET, terdapat batasan panjang URL.

**Apa perbedaan utama antara XML, JSON, dan HTML dalam konteks pengiriman data?**

1. XML (eXtensible Markup Language):
XML sering digunakan dalam pertukaran data antara aplikasi yang tidak terkait secara langsung. XML memiliki syntax yang kaku dan kompleks, menggunakan tag dengan tanda kurung siku untuk mendefinisikan elemen data dan atribut. Hal ini membuat XML cocok untuk menyimpan data yang memiliki struktur yang kompleks dan memerlukan pemrosesan yang tepat. Contoh penggunaan XML termasuk konfigurasi aplikasi, pertukaran data enterprise, dan penyimpanan data dalam basis data. Parsing XML memerlukan lebih banyak kode karena strukturnya yang kompleks.

2. JSON (JavaScript Object Notation):
JSON memiliki format data yang ringan, mudah dibaca, dan mudah ditulis. Ini sering digunakan dalam komunikasi antara server dan peramban web, pengembangan API, dan penyimpanan data terstruktur. JSON menggunakan format pasangan nama-nilai (key-value pairs) yang sederhana dan mirip dengan objek dalam banyak bahasa pemrograman. Parsing JSON lebih mudah karena formatnya yang ringan dan mirip dengan objek dalam bahasa pemrograman. Hal ini membuat JSON menjadi pilihan umum untuk pertukaran data dalam konteks web dan layanan web.

3. HTML (Hypertext Markup Language):
HTML berperan penting dalam menyusun halaman web dengan menentukan tampilan dan struktur konten yang ditampilkan dalam peramban web. HTML memiliki syntax yang khusus, yang terdiri dari elemen, atribut, dan nilai yang menggambarkan cara elemen-elemen konten diatur dan ditampilkan dalam halaman web. Parsing HTML dilakukan oleh peramban web.

**Mengapa JSON sering digunakan dalam pertukaran data antara aplikasi web modern?**

JSON sering digunakan dalam pertukaran data antara aplikasi web modern karena memiliki beberapa kelebihan sebagai berikut. Pertama, JSON memiliki format yang mudah dibaca, sehingga JSON cocok untuk komunikasi antara server dan peramban web. Kedua, JSON menggunakan struktur data yang mirip dengan objek dalam banyak bahasa pemrograman, sehingga memudahkan pemrosesan data di kedua sisi. Hal ini sangat penting dalam pengembangan aplikasi web yang sering mengirim dan menerima data dalam waktu nyata. Selain itu, hampir semua bahasa pemrograman modern memiliki dukungan bawaan untuk mengurai (parsing) data JSON. JSON juga memungkinkan pengguna untuk menggunakan data dengan kompleksitas yang bervariasi.

**Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step**

1. Membuat forms.py pada direktori main dan mengisinya dengan atribut apa saja yang akan diminta untuk Item.
2. Melakukan impor modul HttpResponseRedirect, ItemForm, dan reverse. Lalu membuat fungsi create_item dengan menggunakan ItemForm.
3. Mengubah fungsi show_main lebih tepatnya pada bagian context dengan menambahkan 'items': items .
4. Melakukan impor fungsi create_item pada urls.py di direktoti main dan menambahkan path untuk create_item.
5. Membuat berkas create_item.html di direktori main/templates dan mengisinya dengan form yang akan ditampilkan pada halaman create_item.
6. Mengedit main.html agar nantinya data dapat ditampilkan pada halaman main.
7. Melakukan impor HttpResponse dan serializers pada views.py.
8. Membuat fungsi show_xml, show_json, show_xml_by_id, serta show_json_by_id pada views.py.
9. Mengisi fungsi show_xml dengan data = Item.objects.all() lalu return fungsi HttpResponse dimana parameternya content_type="application/xml".
10. Mengisi fungsi show_json dengan data = Item.objects.all() lalu return fungsi HttpResponse dimana parameternya content_type="application/json".
11. Mengisi fungsi show_xml_by_id dengan data = Item.objects.filter(pk=id) lalu return fungsi HttpResponse dimana parameternya content_type="application/xml".
13. Mengisi fungsi show_xml_by_json dengan data = Item.objects.filter(pk=id) lalu return fungsi HttpResponse dimana parameternya content_type="application/json".
14. Melakukan impor fungsi show_xml, show_json, show_xml_by_id, serta show_json_by_id pada urls.py di direktori main.
15. Menambahan path pada urlpatterns pada urls.py.
16. Mencoba kelima fungsi pada postman dengan membuat request baru lalu masukan URL localhost + path fungsi.

**1. Hasil POSTMAN dalam format HTML**

![Hasil_Main_Preview](Hasil-main.png)

![Hasil_Main_1](Hasil-main-1.png)

![Hasil_Main_2](Hasil-main-2.png)

![Hasil_Main_3](Hasil-main-3.png)

**2. Hasil POSTMAN dalam format XML**

![Hasil_XML](Hasil-XML.png)

**3. Hasil POSTMAN dalam format JSON**

![Hasil_JSON](Hasil-JSON.png)

**4. Hasil POSTMAN dalam format XML by id**

![Hasil_XML_by_ID](Hasil-XML-by-ID.png)

**5. Hasil POSTMAN dalam format JSON by id**

![Hasil_JSON_by_ID](Hasil-JSON-by-ID.png)


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