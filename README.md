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
>>>>>>> 79f70ef (tugas4)
