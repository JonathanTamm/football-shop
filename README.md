https://jonathan-immanuel41-footballshop.pbp.cs.ui.ac.id/

TUGAS INDIVIDU 2
**Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).**
Dimulai dari memmbuat direktori baru yang bernama football-shop lalu buka terminal di dalam direktori tersebut. Buat virtual environment di dalam terminal yang berguna untuk mengisolasi package serta dependencies dari aplikasi agar tidak bertabrakan dengan versi lain yang ada pada laptop. Selanjutnya, buat berkas requirements.txt di dalam direktori yang sama, lalu tambahkan dan lakukan instalasi beberapa dependencies. Setelah itu, buat proyek Djanggo bernama football_shop, file .env, dan file .env.prod di direktori yang sama. Selanjutnya, buat aplikasi baru dengan nama main, di dalam main buat direktori bernama template lalu di dalamnya buat berkas bernama main.html. Isi berkas main.html dan buka di peramban web untuk ngecek tampilannya. Setelah itu, modifikasi berkas models.py di dalam direktori main sesuai dengan ketentuan yang ada di Tutorial 2 untuk mendefinisikan model baru. Selanjutnya kita akan menghubungkan view dengan template dengan cara memodifikasi berkas views.py dan template(main.html). Setelah itu, kita perlu mengonfigurasikan routing URL dengan membuat berkas urls.py di dalam direktori main lalu mengisi berkas urls.py. Modifikasi file settings.py (untuk menggunakan environment variables, menambahkan string ke ALLOWED_HOSTS, menambahkan konfigurasi PRODUCTION tepat di atas code DEBUG, dan ubah konfigurasi database, mendaftarkan 'main' di INSTALLED_APPS). 
Setelah itu migrate manage.py, lalu jalankan server Djanggo dan cek pada peramban web untuk melihat animasi roket sebagai tanda aplikasi Django berhasil dijalankan. Lalu lakukan git init, git add, git commit, dan git push ke git dan pws(agar aplikasi yang sudah dibuat dapat diakses melalui Internet)



**Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html.**
![alt text](image.png)
referensi : PPT 03 - MTV Django Architecture (Slide 3)

Ketika user membuka halaman web Djanggo, browser akan mengirimkan HTTP Request. Request ini akan masuk ke urls.py yang befungsi mencari pola URL mana yang cocok dengen request tersebut. Setelah itu, request akan diteruskan ke views.py, tempat logika utama aplikasi berjalan. Di view, aplikasi kemungkinan mengambil atau menyimpan data. Oleh karena itu, view akan berkomunikasi dengan models.py yang berfungsi untuk menghubungkan ke database. Model inilah yang nantinya akan mengatur bagaimana data disimpan, diubah, dan diambil kembali. Ketika data sudah siap, view akan mengirimkannya ke template berupa file HTML. Template ini bertugas menampilkan data dengan format yang rapi dan bisa dipahami user. Hasil render dari template akan kembali ke view, lalu dikirimkan sebagai HTTP Response ke browser.

    

**Jelaskan peran settings.py dalam proyek Django!**
-> settings.py berperan sebagai pusat konfigurasi, dimana settings.py menyimpan berbagai pengaturan penting yang menentukan bagaimana aplikasi dijalankan, seperti mode debug, daftar host yang diizinkan, daftar aplikasi yang digunakan, middleware, konfigurasi database, validasi password, bahasa, zona waktu, hingga pengaturan file statis. settings.py ini diibaratkan seperti otak konfigurasi yang menghubungkan Django dengan lingkungan pengembangan maupun produksi sehingga aplikasi dapat berjalan dengan baik

**Bagaimana cara kerja migrasi database di Django?**
-> Migrasi database di Django bekerja dengan mencatat perubahan pada model ke dalam file migrasi, lalu mengeksekusinya agar struktur tabel di database selalu sinkron dengan definisi model sehingga developer tidak perlu menulis query SQL secara manual

**Menurut Anda, dari semua framework yang ada, mengapa framework Django dijadikan permulaan pembelajaran pengembangan perangkat lunak?**
-> Django dijadikan permulaan pembelajaran karena sudah menyediakan fitur lengkap sejak awal, memiliki struktur yang rapi, dokumentasi yang baik, dan mampu mengenalkan praktik software engineering dengan cara yang terarah sehingga cocok digunakan baik untuk proyek kecil maupun skala besar

**Apakah ada feedback untuk asisten dosen tutorial 1 yang telah kamu kerjakan sebelumnya?**
-> Asistensi dosen pada tutorial 1 sangat membantu dan baik, asdos membantu dan mengarahkan kita ketika terjadi error maupun ketika bertanya. Penjelasan yang diberikan asdos juga sangat jelas dan runtut dengan bahasa yang mudah dipahami


TUGAS INDIVIDU 3
# Jelaskan mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform?
Data delivery sangat penting karena seluruh proses pertukaran informasi antara server dan pengguna terjadi melalui mekanisme ini. Tanpa ini, data tidak bisa diakses atau diperbarui secara real-time sehingga aplikasi tidak dapat menampilkan informasi yang akurat. Data delivery juga memastikan integrasi antar layanan berjalan lancar, baik itu ke aplikasi mobile maupun web. Jadi, keberadaan data delivery menjadi kunci agar platform dapat berfungsi secara konsisten, aman, dan responsif.

# Menurutmu, mana yang lebih baik antara XML dan JSON? Mengapa JSON lebih populer dibandingkan XML?
Menurut saya, JSON lebih baik untuk dunia modern saat ini. JSON memiliki struktur yang lebih ringkas, mudah dibaca manusia, dan parsingnya lebih cepat dibandingkan XML. JSON juga mendukung tipe data seperti angka, boolean, array, dan objek yang lebih natural untuk dipetakan ke bahasa pemrograman yang populer saat ini. Dalam aplikasi web juga JSON jauh lebih praktis dibandingkan XML.

# Jelaskan fungsi dari method is_valid() pada form Django dan mengapa kita membutuhkan method tersebut?
Method is_valid() digunakan untuk memeriksa apakah data yang dikirim melalui form memenuhi semua aturan yang sudah didefinisikan. Dengan memanggil method is_valid(), Django akan ngecek tipe data, panjang input, dan logika lain yang kita tentukan. Jika valid, kita bisa mengambil data bersih melalui cleaned_data. Tanpa pemanggilan method ini, ada risiko data tidak valid atau berbahaya masuk ke database.

# Mengapa kita membutuhkan csrf_token saat membuat form di Django? Apa yang dapat terjadi jika kita tidak menambahkan csrf_token pada form Django? Bagaimana hal tersebut dapat dimanfaatkan oleh penyerang?
csrf_token berfungsi untuk melindungi aplikasi dari serangan Cross-Site Request Forgery (CSRF). Token ini memastikan setiap permintaan benar-benar berasal dari halaman kita, bukan dari situs lain. Jika kita tidak menambahkan csrf_token, orang yang berniat jahat bisa membuat situs palsu yang diam-diam mengirim permintaan data ke server kita dengan memanfaatkan cookie milik korban, misalnya untuk menghapus data atau mengubah password tanpa sepengetahuan pemilik akun. Dengan token ini, server dapat memverifikasi bahwa permintaan aman dan asli.

# Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
Dimulai dengan menambahkan empat fungsi views baru agar data bisa dilihat dalam format XML, JSON, juga XML dan JSON berdasarkan ID tertentu. Setelah itu saya membuat routing URL di urls.py agar setiap view tadi bisa diakses lewat alamat yang tepat. Langkah berikutnya saya membuat halaman utama yang menampilkan semua data berita dan menambahkan tombol Add untuk pindah ke halaman form, serta tombol Detail pada setiap berita agar bisa membuka halaman detailnya. Setelah halaman utama selesai, saya membuat halaman form create_news.html untuk menambahkan berita baru ke dalam database. Lalu saya menyiapkan halaman news_detail.html yang menampilkan detail lengkap dari setiap berita ketika tombol Detail diklik. Setelah semua fitur itu selesai, saya menguji satu per satu untuk memastikan semuanya berjalan lancar dan akhirnya menjawab pertanyaan yang diminta pada README di folder utama.

# Apakah ada feedback untuk asdos di tutorial 2 yang sudah kalian kerjakan?
Ya, asdos sangat responsif dan sangat baik dalam menjelaskan tutorial 2 ketika kita bertanya.


XML
![alt text](xml.png)

JSON
![alt text](json.png)

XML by ID
![alt text](xmlbyid.png)

JSON by ID
![alt text](jsonbyid.png)
<<<<<<< HEAD
=======


TUGAS INDIVIDU 4
# Apa itu Django AuthenticationForm? Jelaskan juga kelebihan dan kekurangannya.
AuthenticationForm adalah form bawaan Django yang dipakai untuk proses login standar, menerima username dan password, dan menyediakan get_user() jika valid.
Kelebihan :
-Aman karena sudah diuji dan mengikuti praktik Django
-Integrasinya lancar dengan Django auth dan mudah dipakai bersama authenticate(), login(), dan AuthenticationMiddleware.
-Menangani validasi dan pesan error, jadi kita tidak perlu menulis validasi sendiri

Kekurangan:
-Terbatas username dan password, serta jika ingin login menggunakan email, nomor telepon, atau OTP, perlu kustomisasi
-Field tambahan, seperti captcha harus ditambah manual
-Tampilan error perlu disesuaikan sendiri agar cocok dengan UI/UX

# Apa perbedaan antara autentikasi dan otorisasi? Bagaiamana Django mengimplementasikan kedua konsep tersebut?
Autentikasi
-Menentukan siapa itu user dan  memverifikasi identitas user 
Contoh: ketika user ingin login dengan username dan password
-Ada fungsi authenticate() untuk memeriksa kredensial, login() untuk menyimpan status login, dan AuthenticationMiddleware untuk menempelkan request user pada setiap request

Otorisasi
-Menentukan apa yang boleh dilakukan user yang sudah terautentikasi (hak akses, izin, atau peran)
Contoh: apakah user boleh menghapus produk, melihat admin dashboard, atau mengedit item orang lain
-Ada sistem permission, Group, is_staff, is_superuser, decorator seperti @login_required. Untuk validasi akses tingkat objek, biasanya menambahkan logika sendiri

Kesimpulannya, autentikasi untuk memverifikasi identitas, sedangkan otorisasi untuk memutuskan hak akses setelah identitas terverifikasi

# Apa saja kelebihan dan kekurangan session dan cookies dalam konteks menyimpan state di aplikasi web?
Cookies itu disimpan langsung di browser pengguna sehingga lebih sederhana dan bisa bertahan antar kunjungan (selama belum kadaluarsa), serta gampang dibaca atau ditulis menggunakan JavaScript untuk hal ringan seperti tema tampilan. Tapi ukurannya kecil (sekitar 4 KB), bisa dimodifikasi kalau tidak ditandatangani, rentan dicuri lewat XSS kalau tidak menggunakan HttpOnly, dan selalu ikut terkirim ke server setiap request sehingga menambah trafik.

Dalam session, browser hanya menyimpan ID session di cookie, sedangkan data aslinya aman di server. Ini memungkinkan menyimpan data besar atau sensitif seperti status login. Kekurangannya, server jadi harus menyimpan dan mengelola semua session, membersihkan yang lama, dan kalau aplikasi discale ke banyak server perlu berbagi storage sehingga jadi lebih kompleks dan butuh resource ekstra.

# Apakah penggunaan cookies aman secara default dalam pengembangan web, atau apakah ada risiko potensial yang harus diwaspadai? Bagaimana Django menangani hal tersebut?
Cookie tidak otomatis aman, ada beberapa risiko seperti XSS (script jahat bisa baca cookie jika tidak pakai HttpOnly), CSRF (serangan kirim request palsu), pencurian session saat koneksi tidak pakai HTTPS, dan perubahan isi cookie jika tanpa tanda tangan.

Untuk mengetasi itu, secara bawaan SESSION_COOKIE_HTTPONLY aktif, jadi cookie session tidak bisa diakses JavaScript. Django juga menyertakan middleware CSRF dan token {% csrf_token %} untuk mencegah CSRF. Dengan menyalakan SESSION_COOKIE_SECURE dan CSRF_COOKIE_SECURE, cookie hanya dikirim lewat HTTPS. Session disimpan di server melalui SESSION_ENGINE, jadi cookie hanya berisi ID acak, bukan data penting. Jika butuh menyimpan data di cookie, Django menyediakan opsi signed cookies yang ditandatangani dengan SECRET_KEY supaya tidak bisa diubah sembarangan.

# Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
Diawali dengan membuat fungsi register, login, dan logout, pendaftaran memakai UserCreationForm supaya password otomatis di-hash dan langsung login dengan auth_login, login memakai AuthenticationForm untuk validasi bawaan, dan logout dengan auth_logout sambil menghapus cookie last_login. Karena tugas meminta contoh penggunaan cookie, saya menyimpan waktu login terakhir sebagai cookie sederhana yang hanya berisi timestamp dan diset HttpOnly supaya aman, lalu menampilkannya bersama username dan daftar produk user di halaman utama jika pengguna sudah login. Semua form saya lindungi dengan {% csrf_token %} dan routing saya atur dengan URL, serta mengatur LOGIN_REDIRECT_URL dan LOGIN_URL di settings agar alur tetap rapi. Lalu, saya menambahkan dua akun contoh beserta masing-masing tiga produk. Setelah itu saya uji dengan login, melihat data produk, memeriksa cookie last_login, lalu logout untuk memastikan cookie terhapus dan halaman yang butuh login memang terlindungi.




TUGAS INDIVIDU 5
# Jika terdapat beberapa CSS selector untuk suatu elemen HTML, jelaskan urutan prioritas pengambilan CSS selector tersebut!
Browser akan memilih aturan berdasarkan tingkat specificity (yang mana yang paling penting). Inline style yang ditulis langsung di atribut elemen memiliki prioritas tertinggi.Setelah itu, aturan dengan ID lebih kuat daripada class dan class lebih kuat daripada aturan biasa untuk tag HTML. Kalau ada dua aturan dengan tingkat kekuatan yang sama, maka yang ditulis paling akhir di file CSS yang akan dipakai.


# Mengapa responsive design menjadi konsep yang penting dalam pengembangan aplikasi web? Berikan contoh aplikasi yang sudah dan belum menerapkan responsive design, serta jelaskan mengapa!
Responsive design sangat penting karena pengguna mengakses web melalui berbagai perangkat dengan ukuran layar berbeda, mulai dari smartphone hingga monitor yang memiliki layar besar. Dengan responsive design, tampilan web akan menyesuaikan secara otomatis sehingga pengalaman pengguna tetap nyaman. 
Contoh: 
YouTube (sudah menerapkan), dimana tampilan pada layar kecil maupun besar tetap rapi dan nyaman dipandang. Sebaliknya, situs-situs lama sering kali belum menerapkan responsive design (sekarang sudah jarang ditemui) sehingga ketika dibuka di HP tampilannya mengecil, sulit dibaca, dan membuat interaksi pengguna menjadi tidak nyaman.


# Jelaskan perbedaan antara margin, border, dan padding, serta cara untuk mengimplementasikan ketiga hal tersebut!
Margin merupakan jarak di luar elemen yang memisahkan satu elemen dengan elemen lain di sekitarnya (ruang di luar border). Border adalah garis pembatas yang mengelilingi elemen dan berada di antara margin dan padding (pembatas antara margin dan padding). Padding adalah ruang di dalam border yang memisahkan isi konten dengan garis border (ruang antara isi konten dengan border)

implementasi:
-Margin diimplementasikan untuk memberi jarak antar elemen. Misalnya, kalau ada dua kotak yang berdempetan, kita bisa kasih margin supaya ada spasi di antaranya
div {
  margin: 20px; 
}
-Border diimplementasikan untuk memberi garis tepi pada elemen. Kita bisa atur ketebalan, gaya garis, dan warnanya
div {
  border: 2px black;
}
-Padding diimplementasikan untuk memberi jarak antara isi elemen dengan garis tepi border. Jadi konten tidak menempel langsung ke pinggir kotak
div {
  padding: 10px;
}

<!DOCTYPE html>
<html>
<head>
<style>
.box {
  margin: 20px;
  border: 2px black;
  padding: 10px;
}
</style>
</head>
<body>

<div class="box">
  ini adalah contoh kotak dengan margin, border, dan padding
</div>

</body>
</html>


# Jelaskan konsep flex box dan grid layout beserta kegunaannya!
Flex box dan Grid adalah fitur di CSS yang digunakan untuk menyusun tata letak (layout) halaman web. Flex box dipakai untuk menyusun elemen secara satu arah saja (1 dimensi), baik baris ataupun kolom. Misalnya kita mau buat beberapa tombol rata tengah di satu baris, flex box sangat cocok. Sementara grid dipakai untuk menyusun elemen dalam dua arah sekaligus (baris dan kolom) (2 dimensi), jadi sangat cocok untuk layout yang lebih rumit seperti dashboard atau galeri foto. Singkatnya, flex box bagus untuk mengatur deretan elemen sederhana, sedangkan grid bagus untuk struktur halaman yang lebih kompleks.

# Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial)!
Pertama, saya menyiapkan struktur project Django beserta aplikasi yang diperlukan. Setelah itu, saya menambahkan halaman login, register, home, detail, create, dan edit. Untuk navigasi antarhalaman, saya menambahkan navbar pada template utama. Styling halaman saya lakukan menggunakan Tailwind CSS yang diatur melalui static files Django sehingga tampilan lebih rapi dan nyaman dilihat. Model yang digunakan adalah product untuk merepresentasikan data dan setiap fitur seperti tambah, ubah, dan hapus produk dihubungkan ke view yang sesuai.



TUGAS INDIVIDU 6
# Apa perbedaan antara synchronous request dan asynchronous request?
Perbedaan antara synchronous request dan asynchronous request terletak pada cara keduanya menangani waktu tunggu terhadap respons dari server. Pada synchronous request, proses pemanggilan akan berhenti sementara hingga server selesai memproses permintaan dan mengembalikan respons sehingga eksekusi kode berikutnya terblokir selama proses tersebut berlangsung yaang mengakibatkan pengguna harus menunggu hingga seluruh proses selesai sebelum dapat melanjutkan interaksi, sedangkan asynchronous request berjalan di latar belakang tanpa menghentikan eksekusi utama. UI tetap responsif karena browser tidak perlu menunggu respons dari server untuk melanjutkan tugas lain. Ketika hasil sudah diterima, data tersebut baru diproses melalui callback, promise, atau async. Pendekatan asynchronous ini membuat pengalaman pengguna menjadi lebih lancar dan efisien, terutama pada aplikasi web yang sering berinteraksi dengan server.


# Bagaimana AJAX bekerja di Django (alur request–response)?
Pada Django, alur kerja AJAX dimulai ketika JavaScript di sisi frontend mengirimkan permintaan asinkron ke endpoint yang sudah didefinisikan di urls.py. Permintaan ini diterima oleh fungsi views di Django yang kemudian melakukan proses seperti validasi data, pengambilan atau penyimpanan data melalui models. Setelah proses selesai, views akan mengembalikan respon dalam bentuk JsonResponse yang berisi data yang diminta atau status error jika terjadi kesalahan. Data JSON tersebut kemudian diterima kembali oleh JavaScript di frontend dan digunakan untuk memperbarui elemen tertentu di halaman tanpa perlu memuat ulang seluruh halaman. 

# Apa keuntungan menggunakan AJAX dibandingkan render biasa di Django?
Keuntungan utama menggunakan AJAX dibandingkan render biasa di Django adalah kemampuannya untuk memperbarui hanya bagian tertentu dari halaman tanpa perlu melakukan reload seluruh halaman. Hal ini membuat proses terasa jauh lebih cepat dan efisien karena data yang dikirim dan diterima lebih sedikit sehingga penggunaan bandwidth menjadi lebih hemat. Selain itu, AJAX memungkinkan pengguna mendapatkan feedback instan dan melakukan interaksi secara real time

# Bagaimana cara memastikan keamanan saat menggunakan AJAX untuk fitur Login dan Register di Django?
Pertama, selalu sertakan CSRF token dalam setiap permintaan AJAX agar Django dapat memverifikasi bahwa request tersebut benar-benar berasal dari aplikasi yang sah, bukan dari situs lain. Gunakan HTTPS untuk mengenkripsi data sensitif seperti username dan password sehingga tidak mudah disadap. Semua proses validasi dan sanitasi input harus dilakukan di sisi server menggunakan mekanisme bawaan Django karena keamanan di sisi klien bisa dengan mudah dimanipulasi. Pastikan juga cookie yang digunakan memiliki atribut Secure, HttpOnly, dan SameSite untuk mencegah pencurian sesi dan serangan CSRF lanjutan. Selain itu, terapkan rate limiting atau lockout mechanism untuk mencegah serangan brute force dan tambahkan captcha bila perlu. Terakhir, kembalikan pesan error yang bersifat umum, misalnya “Email atau password salah”, agar tidak membocorkan detail tentang kredensial pengguna.

# Bagaimana AJAX mempengaruhi pengalaman pengguna (User Experience) pada website?
AJAX berperan penting dalam meningkatkan pengalaman pengguna di sebuah website karena memungkinkan pertukaran data dengan server tanpa perlu memuat ulang seluruh halaman. Dengan AJAX, bagian tertentu dari halaman dapat diperbarui secara dinamis sehingga interaksi terasa lebih cepat, responsif, dan efisien. Pengguna tidak perlu menunggu lama setiap kali melakukan tindakan karena perubahan langsung terlihat di layar tanpa proses refresh. Hal ini membuat alur penggunaan menjadi lebih mulus dan nyaman. Selain itu, penggunaan AJAX juga membantu menghemat bandwidth karena hanya data yang diperlukan yang dikirim dan diterima, bukan seluruh isi halaman. Namun, jika tidak diterapkan dengan baik, AJAX dapat menimbulkan masalah seperti kesulitan dalam navigasi atau pengindeksan oleh mesin pencari.