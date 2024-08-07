import streamlit as st

def marigold():
    # Paragraf deskripsi
    #st.write("""Menjelaskan Detail bunga Marigold""")

    # Menyisipkan gambar
    st.image("https://raw.githubusercontent.com/Faizalilyas/WebTanamanRefugia/main/Bunga/merigold.jpg", caption="Bunga Marigold", use_column_width=True)

    #import streamlit as st

    # Judul utama
    st.title("Serba-serbi Marigold")

    # Sub header Klasifikasi
    st.header("Klasifikasi")

    st.write("""
        Kingdom: Plantae  
        Subkingdom: Tracheobionta  
        Superdivisi: Spermatophyta  
        Divisi: Magnoliophyta  
        Kelas: Magnoliopsida  
        Subkelas: Asteridae  
        Ordo: Asterales  
        Famili: Asteraceae  
        Genus: *Tagetes*  
        Spesies: *Tagetes erecta* L.
        """)

    # Sub header Morfologi
    st.header("Morfologi")

    # Deskripsi morfologi
    st.write(
        "Tanaman marigold merupakan herba semusim (annual plant) dengan tinggi mencapai "
        "0,5-1,5 m dari permukaan tanah dan memiliki perakaran tunggang. Anggota genus Tagetes "
        "mempunyai bunga komposit berwarna kuning, jingga, atau merah yang menarik, terletak "
        "tunggal pada batang atau bergerombol. Batang marigold tipe pertumbuhan tegak dan bercabang-cabang. "
        "Batang dan daun marigold ditumbuhi oleh bulu-bulu halus dengan warna daun hijau tua, berbentuk lanset, "
        "tepi daun beringgit atau bergelombang dengan ujung meruncing. Panjang daun berkisar antara 5 cm sampai "
        "10 cm dan merupakan daun majemuk. Daunnya tersusun berseberangan pada batangnya dan biasanya dipotong "
        "halus. Karakteristik bracts (struktur mirip daun) membentuk dasar berbentuk cangkir di bawah setiap kepala bunga."
    )

    # Sub header Sejarah
    st.header("Sejarah")

    # Deskripsi sejarah
    st.write(
        "Marigold atau genus Tagetes ialah genus dari sekitar 50 spesies tumbuhan tahunan dari keluarga aster "
        "(Asteraceae). Marigold (*Tagetes erecta L.*) atau dikenal sebagai bunga tahi kotok, gumitir, gemitir merupakan "
        "tanaman yang berasal dari Benua Amerika Utara bagian barat daya, Amerika tropis, dan Amerika Selatan. Nama marigold "
        "juga merujuk pada marigold pot (genus Calendula) dan tanaman yang tidak berkerabat dari beberapa famili. Eksistensi "
        "bunga marigold (*Tagetes erecta L.*) di Indonesia adalah sebagai spesies introduksi asli Meksiko atau wilayah bagian "
        "Amerika Selatan dan Amerika Tengah yang tumbuh baik di daerah tropis dan sub tropis. Marigold bahkan mampu beradaptasi "
        "dalam kondisi kekeringan serta memiliki periode berbunga lebih pendek dari pertengahan musim panas ke musim dingin."
    )

    st.header("Trivia!")
    st.markdown("""
        Nama lain tumbuhan ini “Tahi kotok” loh 😱💩""")

    st.header("Deskripsi dan Manfaat")

    st.subheader("Deskripsi")
    st.write(
        "**Bagian tanaman yang digunakan:** Bunga\n\n"
        "**Senyawa aktif:** Lutein dan Zeaxantin\n\n"
        "Marigold memiliki berbagai kandungan kimia yang sangat bermanfaat, diantaranya "
        "alfa dan beta karoten dan xantofil yaitu lutein dan zeaxantin, selain itu terkandung "
        "flavonoid. Karotenoid bisa menjadi antioksidan, menyembuhkan demam ringan, sakit tenggorokan "
        "ringan, pelembab alami, dan pengusir nyamuk alami. Flavonoid adalah metabolit sekunder dari "
        "polifenol yang memiliki berbagai efek bioaktif termasuk antivirus, anti-inflamasi, antipenuaan, "
        "antioksidan, kardioprotektif, antidiabetes, dan antikanker. Dengan berbagai variasi manfaatnya, "
        "marigold memiliki potensi untuk dikembangkan menjadi obat herbal, refugia, dan bahan obat antinyamuk "
        "mengingat marigold mudah dibudidayakan serta secara ekonomis dan ekologis menguntungkan (Kurniati, 2021)."
    )

    st.subheader("Manfaat")
    st.markdown("""
        Berikut adalah rangkuman manfaat Tagetes erecta, yaitu:

        * Kejang panas pada anak (ISPA)
        * Radang tenggorokan
        * Sariawan
        * Sakit gigi
        * Radang mata (konjungtivitis)
        * Batuk rejan (pertussis) dan bronkitis
        * Perut kembung
        * Gondongan (parotitis)
        * Radang kulit bernanah (pioderma)
        * Pembengkakan payudara (mastitis)
        * Mual
        * Pegal linu (Reumatism)
        * Membantu kesehatan Mata
        * Melindungi kulit
        * Membantu kesehatan jantung
        """)

    st.header("Cara Pemakaian")
    st.subheader("Pemakaian dalam")
    st.markdown("""
    5-15 g herba bunga kering direbus lalu airnya diminum
    """)

    st.subheader("Pemakaian luar")
    st.markdown("""
    Bunga dicuci dan tumbuk sampai halus campur beras putih seperlunya kemudian tempelkan pada tempat yang sakit 
    seperti pegal linu, radang payudara, gondongan dll.
    """)

    st.subheader("Batuk Rejan")
    st.markdown("""
    Rebus 15 gram bunga kering dengan 2 gelas air hingga tersisa 1 gelas, 
    lalu tambahkan gula merah secukupnya. Saring dan minum setengah gelas pagi dan sore.""")

    st.subheader("Sakit Gigi")
    st.markdown("""
    Rebus 15 gram bunga tahi kotok kering dengan 2 gelas air, kemudian saring dan minum setengah gelas setiap hari sampai sembuh.
    """)

    st.subheader("Sakit Mata")
    st.markdown("""
    Rebus satu kuntum bunga tahi kotok segar dengan air secukupnya, lalu gunakan air rebusan tersebut untuk mencuci mata yang sakit.
    """)

    st.subheader("Bronkitis")
    st.markdown("""
    Rebus 15 gram bunga tahi kotok kering dengan 2 gelas air hingga tersisa 1 gelas, kemudian tambahkan kencur dan gula 
    aren secukupnya. Saring dan minum setiap hari
    """)


    st.markdown("""
    ## Referensi

    Kurniati, F. (2021). POTENSI BUNGA MARIGOLD (*Tagetes erecta* L.) SEBAGAI SALAH SATU KOMPONEN PENDUKUNG PENGEMBANGAN 
    PERTANIAN. *MEDIA PERTANIAN, 6*(1).  
    [https://doi.org/10.37058/mp.v6i1.3010](https://doi.org/10.37058/mp.v6i1.3010)

    NaturMed Scientific. (2024, May 25). *Ekstrak Marigold (*Tagetes erecta*).* Naturmed Scientific.  
    [https://naturmedscientific.com/id/produk/ekstrak-marigold-tagetes-erecta/](https://naturmedscientific.com/id/produk/ekstrak-marigold-tagetes-erecta/)

    Rubi. (2017, November 4). *Cocok Botol: Deskripsi, Klasifikasi dan Manfaat Tanaman Cocok Botol (*Tagetes erecta*).* Hijau.  
    [https://rubi77botani.wordpress.com/2017/11/04/deskripsi-dan-klasifikasi-tanaman-cocok-botol/](https://rubi77botani.wordpress.com/2017/11/04/deskripsi-dan-klasifikasi-tanaman-cocok-botol/)

    The Editors of Encyclopaedia Britannica. (1998, July 20). *Marigold.* *Encyclopedia Britannica.*  
    [https://www.britannica.com/plant/marigold](https://www.britannica.com/plant/marigold)
    """)

def TaiwanBeauty():
    # Paragraf deskripsi
    #st.write("""Menjelaskan Detail bunga Marigold""")

    # Menyisipkan gambar
    st.image("https://raw.githubusercontent.com/Faizalilyas/WebTanamanRefugia/main/Bunga/taiwanbeauty.jpg", caption="Bunga Taiwan Beauty", use_column_width=True)

    #import streamlit as st

    # Judul utama
    st.title("Serba-serbi Taiwan Beauty")

    # Sub header Klasifikasi
    st.subheader("Klasifikasi")

    # Klasifikasi Tumbuhan
    st.write("""

    Kingdom: Plantae  
    Subkingdom: Tracheobionta    
    Superdivisi: Spermatophyta   
    Divisi: Magnoliophyta  
    Kelas: Magnoliopsida  
    Subkelas: Rosidae  
    Ordo: Myrtales  
    Famili: Lythraceae  
    Genus: *Cuphea*  
    Spesies: *Cuphea hyssopifolia* Kunth.
    """)

    # Sub header Morfologi
    st.header("Morfologi")

    # Deskripsi morfologi
    st.write(
        "Taiwan Beauty termasuk tanaman semak yang tumbuh dengan ketinggian sekitar 30-40 cm. "
        "Tanaman ini memiliki daun berukuran kecil, bertekstur halus, berwarna hijau mengkilap "
        "dan tumbuh disepanjang tangkai tanaman. Bunga taiwan beauty berdiameter sekitar 0,5 cm "
        "dengan warna bunga bervariasi yaitu ungu, putih, kuning dan pink. Bunga taiwan beauty akan terus mekar sepanjang tahun."
    )

    # Sub header Sejarah
    st.header("Sejarah")

    # Deskripsi sejarah
    st.write(
        "Taiwan beauty merupakan tanaman yang berasal dari Amerika dan telah menyebar ke seluruh "
        "daerah tropis dan subtropis. Tanaman Ini sering ditanam masyarakat sebagai tanaman hias "
        "di daerah tropis, tanaman pagar, penutup tanah, serta pembatas antar tanaman."
    )

    st.header("Trivia!")
    st.markdown("""
            Nama lain tanaman ini “Seribu nyamuk”, loh! 🦟""")

    st.header("Deskripsi dan Manfaat")

    st.subheader("Deskripsi")
    st.write("""
    *Cuphea hyssopifolia* adalah tanaman yang kaya akan senyawa fenolik dan memiliki potensi sebagai antioksidan (Elgindi *et al.*, 2012). Tanaman Cuphea umumnya digunakan untuk nilai pengobatan tradisional. 
    Di negara asalnya, tanaman dari spesies ini dikumpulkan dan digunakan sebagai anti protozoa, pembersih darah, diuretik, *emmenagog*, *hipotensif*, pencahar, purgatif, antivirus, antinociceptive, antimikroba, antiinflamasi, penyakit kardiovaskular, dan masalah menstruasi. Beberapa laporan farmakologis menyatakan berbagai potensi lain berdasarkan kandungan senyawa yang dikandungnya, seperti senyawa fenolik, triterpenoid, flavonoid, tannin, lipid, asam lemak tak jenuh, dan steroid (Das *et al.*, 2018).

    **Kandungan senyawa:**  
    Utama: Flavonoid dan fenolik  
    Senyawa fenolik (asam valoneat dilakton;  
    1,3–O–digalloyl-4,6-hexahydroxydiphenoyl-β-D-4C1-glucopyarnose; asam galat; genistein-7-O-β-D-4C1-glucopyranoside; myricetin–3–O–β-D-4C1-glucopyranoside; 3,4,5-trimetoksi asam benzoat; asam vanilat), cuphin D1, cuphin D2, oenothein B, woodfordin C, *diterpen* dan flavonoid (friedelan-3β-ol; asam ursolat; metil galat; quercetin-3-O-α-rhamnopyranoside; 1,2, 3,4,6-penta-O-galloyl-β-D-glukosa; dan *manitol*).
    """)

    st.subheader("Manfaat")
    st.markdown("""
        Berikut adalah rangkuman manfaat Taiwan Beauty, yaitu:

        * Menurunkan demam, kolesterol tinggi, dan trigliserida
        * Mengatasi batuk
        * Dermatitis
        * Keseleo
        * Masuk angin dan kedinginan
        * Antioksidan
        """)

    st.header("Cara Penggunaan")
    st.subheader("Demam Menggigil")
    st.markdown("""
    * Siapkan daun secukupnya lalu cuci hingga bersih.
    * Rendam daun dan tunggu beberapa lama.
    * *Saring hasil rendaman lalu minum untuk melegakan demam yang menggigil.
    """)

    st.subheader("Menurunkan Kolesterol")
    st.markdown("""
    * Ambil daun dan batang taiwan beauty lalu cuci hingga bersih.
    * Haluskan daun dan batang hingga menjadi pasta.
    * Oleskan pasta ke seluruh badan.
    """)

    st.markdown("""
    ## Referensi

    Das, A., Chaudary, S. K., Bhat, H. R., & Shakya, A. (2018). *Cuphea carthagenensis*: A review of its ethnobotany, pharmacology and phytochemistry. *Bulletin of Arunachal Forest Research, 33*(2), 1–14.  
    [https://doi.org/ISSN 0970-9487](https://doi.org/ISSN 0970-9487)

    Elgindi, M., Ayoub, N., Milad, R., & Mekky, R. (2012). Antioxidant and Cytotoxic Activities of *Cuphea hyssopifolia* Kunth (Lythraceae) Cultivated in Egypt. *Journal of Pharmacognosy and Phytochemistry, 1*(4), 67–77.  
    [https://doi.org/ISSN 2278-4136](https://doi.org/ISSN 2278-4136)

    Socfindo Conservation. (2024). *Cuphea hyssopifolia*. Socfindo Conservation.  
    [https://www.socfindoconservation.co.id/plant/718](https://www.socfindoconservation.co.id/plant/718)
    """)

def Vincamajor():
    # Paragraf deskripsi
    #st.write("""Menjelaskan Detail bunga Marigold""")

    # Menyisipkan gambar
    st.image("https://raw.githubusercontent.com/Faizalilyas/WebTanamanRefugia/main/Bunga/vinca%20mayor.jpg", caption="Bunga Vinca Major", use_column_width=True)

    #import streamlit as st

    # Judul utama
    st.title("Serba-serbi Vinca Major")

    # Sub header Klasifikasi
    st.subheader("Klasifikasi")

    # Klasifikasi Tumbuhan
    st.write("""
    Kingdom: Plantae  
    Subkingdom: Tracheobionta  
    Superdivisi: Spermatophyta  
    Divisi: Magnoliophyta  
    Kelas: Magnoliopsida  
    Subkelas: Asteridae  
    Ordo: Gentianales  
    Famili: Apocynaceae  
    Genus: *Vinca*  
    Spesies: *Vinca major* L.
    """)

    # Sub header Morfologi
    st.header("Morfologi")

    # Deskripsi morfologi
    st.write(
        "Termasuk tumbuhan semak pendek dengan tinggi tanaman 25-50 cm, vinca major memiliki bunga berwarna ungu "
        "bergradasi putih pada bagian tengah dengan 5 kelopak bunga panjang antara 1-2,8 cm menjadikan bunga ini memang "
        "terlihat berbeda. Warna daun bunga ini hijau dengan urat-urat daun yang pucat. Tanaman ini dapat tumbuh "
        "di daerah dataran rendah hingga dataran tinggi yang ketinggiannya mencapai 800 meter dpl. Cabang tanaman ini "
        "dapat tumbuh ke samping dengan tinggi antara 0,2-1 m. "
        "Pada bagian batangnya terkadang terdapat rambut halus. Sedangkan buahnya adalah buah kering yang memiliki "
        "panjang 2-4,7 cm dengan banyak biji hitam yang kecil-kecil."
    )

    # Sub header Sejarah
    st.header("Sejarah")

    # Deskripsi sejarah
    st.write(
        "Bunga vinca dikenal juga dengan sebutan Periwinkle ini ada di hampir seluruh daerah tropis yang ada di dunia, "
        "seperti india, Indonesia, China, Australia dan benua Amerika, tepatnya Amerika Selatan dan Amerika Utara. "
        "Di Indonesia sendiri, bunga ini dikenal dengan nama bunga Tapak Dara atau Vinca. Sebagai tanaman hias, "
        "bunga ini memang banyak  dijumpai di halaman-halaman rumah."
    )

    st.header("Trivia!")
    st.markdown("""
            Nama lainnya “Periwinkle”! 🧚🏻‍♂️""")

    st.header("Deskripsi dan Manfaat")

    st.subheader("Deskripsi")
    st.write("""
    
    Tanaman ini biasanya berbunga antara bulan April dan Mei. Yang menarik, tanaman ini bisa berkembang biak tanpa biji!
    Vinca major dapat menyebar lewat batangnya yang tumbuh akar pada setiap ruas. Karena itulah, tanaman ini bisa tumbuh
     dengan sangat cepat. Namun, pertumbuhannya yang cepat bisa menjadi masalah karena dapat menghalangi tanaman lain 
     untuk tumbuh. Selain itu, Vinca major bisa menjadi inang bagi bakteri penyebab penyakit Pierce pada tanaman anggur.
      Vinca major juga memiliki banyak khasiat. Tanaman ini bersifat astringen, pahit, deterjen, sedatif, stomachic, dan
       tonik. Kandungan alkaloid "vincamine" dalam tanaman ini digunakan oleh industri farmasi sebagai stimulan otak dan
        vasodilator. Selain itu, "reserpine" yang ada dalam tanaman ini bisa membantu menurunkan tekanan darah tinggi.      
        Secara internal, Vinca major digunakan untuk mengobati menstruasi berlebihan, perdarahan uterus abnormal, 
        keputihan, dan pengerasan arteri. Namun, tanaman ini tidak boleh digunakan oleh pasien yang mengalami sembelit. 
        Secara eksternal, tanaman ini bermanfaat untuk mengobati keputihan, mimisan, sakit tenggorokan, dan sariawan. 
        Biasanya, tanaman ini dipotong saat berbunga dan dikeringkan untuk digunakan di kemudian hari. Bunga segarnya 
        memiliki efek purgatif ringan, tetapi efek ini hilang setelah bunga dikeringkan. Obat homeopati juga bisa dibuat
         dari daun segar untuk mengobati perdarahan. Walaupun tanaman ini memiliki manfaat yang luar biasa, dalam kadar 
         yang berlebihan akan menyebabkan reaksi toksisitas.   
              
    **Kandungan senyawa:**  
    * Vincamine sebagai stimulan dan vasodilator      
    * Reserpine sebagai menurunkan tekanan darah  
    *Kandungan lain yang diketahui secara skrining fitokimia:* alkaloid, saponin, sterol tak jenuh, asam organik, dan fenol.
    """)

    st.subheader("Manfaat")
    st.markdown("""
        Berikut adalah rangkuman manfaat Vinca Major, yaitu:

        * Stimulan
        * Vasodilator
        * Menurunkan tekanan darah
        * Pendarahan besar saat menstruasi
        * Konstipati
        * Sakit tenggorokan
        * Sakit gigi
        * Luka
        * Tonsillitis
        * Mencegah kelainan otak
        * Inang bakteri penyakit Pierce pada anggur
        """)

    st.markdown("**Perhatian!**")
    st.markdown("""
    Vinca major tidak boleh dikonsumsi oleh ibu hamil dan menyusui. Selain itu, hindari mengonsumsi tanaman ini dengan 
    obat-obatan antihipertensi. Untuk menggunakan tanaman ini harap sebaiknya berdiskusi dengan dokter dan farmasis.
    """)

    st.markdown("""
    ### Referensi

    **Cal-IPC. (2024). _Vinca major Profile – California Invasive Plant Council_. Cal-IPC.**
    [https://www.cal-ipc.org/plants/profile/vinca-major-profile/](https://www.cal-ipc.org/plants/profile/vinca-major-profile/)

    **Farnsworth, N. R., Fong, H. H. S., Blomster, R. N., & Draus, F. J. (1962). _Studies on Vinca major (Apocynaceae) II. Journal of Pharmaceutical Sciences_, 51(3), 217–224.**
    [https://doi.org/10.1002/jps.2600510307](https://doi.org/10.1002/jps.2600510307)

    **MissouriBotanicalGarden. (2024). _Vinca major_. Plant Finder.**
    [https://www.missouribotanicalgarden.org/PlantFinder/PlantFinderDetails.aspx?taxonid=276113](https://www.missouribotanicalgarden.org/PlantFinder/PlantFinderDetails.aspx?taxonid=276113)

    **Naturalmedicinalherbs. (2024). _medicinal herbs: GREATER PERIWINKLE. Vinca Major_.**
    [https://www.naturalmedicinalherbs.net/herbs/v/vinca-major=greater-periwinkle.php](https://www.naturalmedicinalherbs.net/herbs/v/vinca-major=greater-periwinkle.php)

    **North Carolina Extension Gardener. (2024). _Vinca major (Big Leaf Periwinkle, Blue Buttons, Blue Periwinkle, Greater Periwinkle, Periwinkle)_. North Carolina Extension Gardener Plant Toolbox.**
    [https://plants.ces.ncsu.edu/plants/vinca-major/](https://plants.ces.ncsu.edu/plants/vinca-major/)

    **PlantRight. (2024). _Vinca major – PlantRight_. PlantRight.**
    [https://plantright.org/invasive/vinca-major/](https://plantright.org/invasive/vinca-major/)

    **RHS. (2024). _Vinca major_. Royal Horticultural Society.**
    [https://www.rhs.org.uk/plants/18969/vinca-major/details](https://www.rhs.org.uk/plants/18969/vinca-major/details)

    **RxList. (2021, June 11). _Periwinkle: Health benefits, side effects, uses, dose & precautions_. RxList.**
    [https://www.rxlist.com/supplements/periwinkle.htm](https://www.rxlist.com/supplements/periwinkle.htm)
    """)

def Miana():
    # Paragraf deskripsi
    #st.write("""Menjelaskan Detail bunga Marigold""")

    # Menyisipkan gambar
    st.image("https://raw.githubusercontent.com/Faizalilyas/WebTanamanRefugia/main/Bunga/miana.jpg", caption="Bunga Miana", use_column_width=True)

    #import streamlit as st

    # Judul utama
    st.title("Serba-serbi Miana")

    # Sub header Klasifikasi
    st.subheader("Klasifikasi")

    # Klasifikasi Tumbuhan
    st.write("""
    Plectranthus scutellarioides  
    Kingdom: Plantae  
    Subkingdom: Tracheobionta  
    Superdivisi: Spermatophyta  
    Divisi: Magnoliophyta  
    Kelas: Magnoliopsida  
    Subkelas: Asteridae  
    Ordo: Lamiales  
    Famili: Lamiaceae  
    Genus: *Solenostemon*  
    Spesies: *Solenostemon scutellarioides* L.
  
    """)

    # Sub header Morfologi
    st.header("Morfologi")

    # Deskripsi morfologi
    st.write(
        "Tanaman miana merupakan tumbuhan dengan akar tunggang yang warna akarnya kuning keputih-putihan. Batang miana "
        "bentuk bersegi dapat tumbuh hingga ketinggian 1 meter dengan warna batang hijau pucat dan sifatnya lunak. "
        "Daun miana berbentuk hati dan merupakan daun tunggal. Bunga miana merupakan bunga majemuk berbentuk tandan "
        "di ujung batang. Kelopaknya berbentuk corong berwarna hijau muda. Mahkota bunga berbentuk bibir berwarna ungu "
        "keputih-putihan. Memiliki dua benang sari berwarna putih dan putik kecil yang berwarna ungu. Buah miana yang "
        "masih muda berwarna hijau dan berubah menjadi cokelat pada saat matang atau berusia tua."
    )

    # Sub header Sejarah
    st.header("Sejarah")

    # Deskripsi sejarah
    st.write(
        "Miana merupakan tanaman asli India dan Thailand. Distribusi tanaman miana terdiri dari wilayah Asia-Tropis, "
        "Australasia, Burma, Asia Tenggara, malenesia, Polynesia, Cina Selatan, Solomons dan Amerika Selatan."
    )

    st.header("Trivia!")
    st.markdown("""
                Punya banyak banget nama lain!""")

    st.header("Deskripsi dan Manfaat")

    st.subheader("Deskripsi")
    st.write("""
    Tanaman ini punya banyak sekali nama panggilan di berbagai daerah, loh! Orang Sunda menyebutnya "jawer kotok," 
    sementara di Jawa, tanaman ini dikenal sebagai "iler." Di Madura, nama yang digunakan adalah "dhinkamandhinan," 
    dan di Batak, tanaman ini disebut "si gresing." Orang Palembang mengenalnya sebagai "adang-adang," sedangkan 
    di Sumatera Barat, tanaman ini disebut "pilado." Di Minahasa, tanaman ini dikenal dengan nama "serewung," dan di 
    Kota Manado, namanya adalah "majana." Orang Bugis menyebutnya "panci-panci." Bahkan, di Filipina, tanaman ini 
    dikenal sebagai "mayana" atau "maliana."  
    
    Selain namanya yang banyak, manfaatnya juga gak kalah banyak, ya 😊  
    Hal ini karena miana memiliki banyak senyawa kimia yang bermanfaat untuk kesehatan, diantaranya:  
    **Kandungan senyawa:**  
    * Flavonoid: quercetin, kaempferol, dan mirisetin.  
    * Terpenoid: timol, karvakrol, dan eugenol.  
    * Vitamin C  
    * Vitamin E
    """)

    st.subheader("Manfaat")
    st.markdown("""
    - **Kesehatan**: Batuk, pilek, asma, jerawat, bisul, dan diare
    - **Kecantikan**
        - Merawat kulit karena sifat antioksidan dan antiinflamasi
        - Mencerahkan kulit karena ada vitamin C
        - Mengatasi rambut rontok karena flavonoid dan fitosterol
        - Merawat rambut kering dan kusam karena adanya minyak alami
    - **Kuliner**
        - Rasanya yang sedikit pahit dapat dibuat untuk tambahan salad, sup, dan _tumisan_
        - Bunga miana dapat dijadikan lalapan dan teh
    - **Antioksidan**: flavonoid, terpenoid, vitamin C, dan vitamin E
    - **Antiinflamasi**
        - Menghambat produksi sitokin yang mana merupakan penyebab peradangan
        - Menghambat enzim COX-2 yang juga pemicu peradangan
        - Meningkatkan produksi kortisol yang merupakan hormon yang berfungsi sebagai antiinflamasi
    - **Antibakteri**: bakteri penyebab jerawat, seperti _Staphylococcus aureus_, dan _Escherichia coli_. Senyawa antibakteri yang dimaksud adalah minyak atsiri, flavonoid, dan terpenoid
    - **Antivirus**: virus _antifluensa_
    - **Antifungal**: kurap, panu, dan kandidiasis
    - **Peluruh dahak**: akibat senyawa saponin yang bersifat mukolitik, flavonoid yang bersifat ekspektoran, dan minyak atsiri (senyawa timol dan karvakrol).
    """)

    st.header("Cara Penggunaan")
    st.subheader("Bisul")
    st.markdown("""
    1. Campurkan 10 lembar daun miana segar dan ditumbuk halus dengan air secukupnya  
    2. Dibalutkan ke bisul sebanyak 2-3 kali sehari  
    
    Cara lain untuk pengobatan bisul adalah dengan:  
    1. Panaskan daun miana segar dengan api (jangan sampai gosong, ya!)
    2. Tempelkan pada bisul dan dikompres selama beberapa menit

    """)

    st.subheader("Batuk dan nyeri")
    st.markdown("""
    1. Rebus daun miana segar sebanyak 7-10 lembar daun
    2. Saring airnya dan diminum selagi hangat

    """)

    st.markdown("""
    ### Referensi

    Ahmad, A. R., Handayani, V., Malik, Abd., Ririn, Widiastuti, H., Mardatillah, & Mamas, M. (2021). _Tumbuhan berpotensi obat: Desa Sanrobone, Kabupaten Takalar_. Nas Media Pustaka.

    Arief Hariana, R. Syamsul Hidayat, Bambang Mursito, Pinus Lingga, & PS, T. P. (2015). _Kitab resep HERBAL_. Penebar Swadaya Grup.

    Handoko, S. T., Heriyawati, D. F., & Zayadi, H. (2022). _Prosiding UNISMA: Model KKN tematik untuk mewujudkan masyarakat tangguh guna percepatan pembangunan di era pandemi Covid-19_. Media Nusa Creative (MNC Publishing).

    Pramono, JE. D. (2024). _143 Tip Cerdas Seputar Kesehatan, Rumah, dan Masakan_. DeMedia.

    sisca. (2024, April 30). _5 Manfaat Tanaman Miana yang Jarang Diketahui dan Penting untuk Anda Ketahui_. Birds n Bees. [https://www.birdsnbees.co.id/manfaat-tanaman-miana/](https://www.birdsnbees.co.id/manfaat-tanaman-miana/)
    """)

def Zinnia():
    # Paragraf deskripsi
    #st.write("""Menjelaskan Detail bunga Marigold""")

    # Menyisipkan gambar
    st.image("https://raw.githubusercontent.com/Faizalilyas/WebTanamanRefugia/main/Bunga/zenia.jpg", caption="Bunga Zinnia", use_column_width=True)

    #import streamlit as st

    # Judul utama
    st.title("Serba-serbi Bunga Kertas (Zinnia)")

    # Sub header Klasifikasi
    st.subheader("Klasifikasi")

    # Klasifikasi Tumbuhan
    st.write("""
    Kingdom: Plantae  
    Subkingdom: Tracheobionta  
    Superdivisi: Spermatophyta  
    Divisi: Magnoliophyta  
    Kelas: Magnoliopsida  
    Subkelas: Asteridae  
    Ordo: Asterales  
    Famili: Asteraceae  
    Genus: *Zinnia*  
    Spesies: *Zinnia violacea* Cav.
    """)

    # Sub header Morfologi
    st.header("Morfologi")

    # Deskripsi morfologi
    st.write(
        "Tanaman kembang kertas atau Zinnia termasuk tanaman semusim. Habitus tanaman ini memiliki batang berdiri tegak "
        "dengan tinggi 10–100 cm yang berwarna kehijauan dan kekuningan. Daun tanaman ini berbentuk lanset, jorong dan "
        "memanjang dengan pangkal daun berbentuk rompang atau rata dan tumpul serta memiliki ujung daun runcing. "
        "Bunga kembang kertas berbentuk floret dengan diameter bunga hingga mencapai 10 cm. Bentuk bunga terdiri dari "
        "disk dan petal yang mana bagian disk terletak di bagian tengah dengan warna kuning-jingga atau ungu kecoklatan."
        " Sementara bagian petal terletak di bagian disk yang tersusun menyebar dengan jumlah mulai dari 8–20. Warna "
        "pada petal beraneka macam mulai dari putih, kuning, merah, jingga, pink, ungu, ungu kemerahan, namun di alam "
        "sering dijumpai dengan warna merah. Bentuk kembang kertas sendiri terdiri dari bentuk tunggal, tumpuk, dan "
        "pompom yang didasarkan atas lapisan petal pada bagian disk bunga."
    )

    # Sub header Sejarah
    st.header("Sejarah")

    # Deskripsi sejarah
    st.write(
        "Tanaman ini berasal dari Meksiko, tetapi tumbuh sebagai tanaman hias di banyak tempat dan menyebar di beberapa"
        " tempat, termasuk di Amerika Tengah dan Selatan, Hindia Barat, Amerika Serikat, Australia dan Italia. Spesies "
        "ini pertama kali ditemukan pada tahun 1789 di Tixtla, Guerrero oleh Sessé dan Mociño. Tanaman ini kemudian "
        "secara resmi diberi nama Zinnia violacea oleh Cavanilles pada tahun 1791. Zinnia yang paling banyak "
        "dibudidayakan, dilaporkan telah lolos dari budidaya dan tampaknya dinaturalisasi di sepuluh negara bagian timur"
        " dan selatan tetapi tidak umum di kawasan flora."
    )

    st.header("Trivia!")
    st.markdown("""
                “Sacrificial crop” """)

    st.header("Deskripsi dan Manfaat")

    st.subheader("Deskripsi")
    st.write("""
    Tanaman ini selain cantik, juga memiliki peran besar untuk tanaman di sekitarnya, loh! Udah kayak pesan moral aja 
    ya, yaitu “bermanfaat buat sekitar” :v  
    
    Oke, kembali ke topik. Tanaman ini bisa disebut sebagai "sacrificial crop" atau tanaman pengorbanan. Sesuai dengan 
    julukannya, tanaman ini menarik serangga taman yang tidak diinginkan. Meskipun terdengar seperti hal yang negatif, 
    ini sebenarnya bisa dimanfaatkan. Salah satu hama taman terburuk adalah kumbang Jepang. Serangga ini sering datang 
    dalam jumlah besar dan bisa menghancurkan tanaman sayuran atau buah dalam beberapa hari.  
    
    Nah, tanaman zinnia bisa digunakan sebagai tanaman pengorbanan. Tanaman pengorbanan adalah tanaman yang digunakan 
    untuk menarik hama seperti kumbang Jepang agar menjauhi tanaman sayuran yang lebih diinginkan. Misalnya, jika kamu 
    punya tanaman kacang hijau atau tanaman sayuran lain yang disukai hama, tanam zinnia di dekatnya. Hama akan lebih 
    tertarik pada zinnia dan seringkali akan meninggalkan tanaman panganmu. Tanaman yang biasa jadi pendamping tanaman 
    ini adalah tomat, kentang, kembang kol, nasturtium, kosmos, dan bunga matahari.  
    
    Manfaat lain dari tanaman ini belum banyak diketahui. Namun, beberapa penelitian ilmiah menunjukkan bahwa tanaman 
    ini memiliki polifenol dan alkaloid yang memiliki potensi sebagai antioksidan. Senyawa fenolik seperti asam 
    klorogenat, apigenin, kaempferol, dan glikosida kuersetin terdeteksi melalui analisis NMR. Jadi, selain membantu 
    melindungi tanaman lain, tanaman ini juga punya potensi manfaat kesehatan (Burlec *et al*., 2019). 

    """)

    st.subheader("Manfaat")
    st.markdown("""
        Berikut adalah rangkuman manfaat Bunga Kertas (Zinnia), yaitu:
        * Mengundang pollinator, serangga yang membantu polinasi (penyerbukan) seperti lebah, kupu-kupu, dan sebagainya
        * Warnanya yang cerah dapat dijadikan tanaman hias
        """)

    st.markdown("""
    ## Referensi

    **Burlec, A. F., Pecio, Ł., Mircea, C., Cioancă, O., Corciovă, A., Nicolescu, A., Oleszek, W., & Hăncianu, M.** 
    (2019). *Chemical Profile and Antioxidant Activity of Zinnia elegans Jacq. Fractions*. *Molecules, 24*(16), 2934. 
    https://doi.org/10.3390/molecules24162934

    **Gardenalchemyseed.** (2024). *Growing zinnias- benefits and instructions*. Garden Alchemy Seeds and More. 
    [https://gardenalchemyseeds.ca/pages/growing-zinnias-benefits-and-instructions](https://gardenalchemyseeds.ca/pages/growing-zinnias-benefits-and-instructions)

    **PennState.** (2024). *Zinnias for the home garden*. PennState Extension. [https://extension.psu.edu/zinnias-for-the-home-garden](https://extension.psu.edu/zinnias-for-the-home-garden)

    **SimpleGardenLife.** (2022, June 18). *Why you should grow zinnias in your vegetable garden - 6 benefits*. Simple Garden Life. [https://simplegardenlife.com/grow-zinnias-in-your-vegetable-garden/](https://simplegardenlife.com/grow-zinnias-in-your-vegetable-garden/)
    """)

def Asoka():
    # Paragraf deskripsi
    #st.write("""Menjelaskan Detail bunga Marigold""")

    # Menyisipkan gambar
    st.image("https://raw.githubusercontent.com/Faizalilyas/WebTanamanRefugia/main/Bunga/asoka.jpg", caption="Bunga Asoka", use_column_width=True)

    #import streamlit as st

    # Judul utama
    st.title("Serba-serbi Asoka")

    # Sub header Klasifikasi
    st.subheader("Klasifikasi")

    # Klasifikasi Tumbuhan
    st.write("""
    Kingdom: Plantae  
    Subkingdom: Tracheobionta  
    Superdivisi: Spermatophyta  
    Divisi: Magnoliophyta  
    Kelas: Magnoliopsida  
    Subkelas: Rosidae  
    Ordo: Fabales  
    Famili: Caesalpiniaceae  
    Genus: *Saraca*  
    Spesies: *Saraca indica*

    """)

    # Sub header Morfologi
    st.header("Morfologi")

    # Deskripsi morfologi
    st.write(
        "Asoka termasuk tanaman perdu yang tegak, berbatang kasar, berkayu keras, bercabang banyak, berwarna abu-abu. "
        "Berakar tunggang warna kecokelatan. Daun penumpu berbentuk bulat telur segitiga, meruncing, daun berhadapan,"
        " bertangkai pendek, bentuk memanjang bulat telur terbalik, dengan pangkal dan ujung tumpul, tepi rata sedikit "
        "bergerigi, daun berwarna hijau tua, berkilau, tangkai daun sangat pendek. Bunga majemuk tersusun dalam malai "
        "rata yang bertangkai, duduk atau bertangkai pendek. Setiap bunga berbentuk tabung dengan 4-5 helai terbuka. "
        "Cuping mahkota lanset atau bulat telur-lanset. Bunga berwarna merah atau merah muda, dan kuning. Tanaman asoka "
        "memiliki buah yang berdaging, bulat, berwarna merah gelap sampai ungu kehitaman, terdiri dari 2 biji."
    )

    # Sub header Sejarah
    st.header("Sejarah")

    # Deskripsi sejarah
    st.write(
        "Tanaman Asoka berasal dari Asia Selatan dan Tenggara, terutama di  India Selatan dan Sri Lanka. Tersebar luas "
        "ke seluruh daerah tropis dan subtropis seperti Indonesia, Malaysia, Filipina, Vietnam, Kamboja, Laos, "
        "dan Thailand. Dikenal juga sebagai Melati India Barat, sering digunakan dalam upacara agama Hindu dan "
        "pengobatan tradisional India. Bunga ini memiliki nama ilmiah Saraca asoca dan termasuk dalam keluarga Fabaceae."
        " Bunga ini telah dibudidayakan selama berabad-abad dan telah menjadi bagian penting dari budaya dan tradisi di "
        "banyak negara di Asia."
    )

    st.header("Trivia!")
    st.markdown("""
                Merupakan pohon suci bagi umat Hindu  dan diasosiasikan dengan cinta serta kesucian.""")

    st.header("Deskripsi dan Manfaat")

    st.subheader("Deskripsi")
    st.write("""
    Tanaman asoka dikenal dengan banyak nama, seperti glodokan tiang di Indonesia dan Flame of the Wood atau api dari 
    hutan di Eropa karena warnanya yang cerah dan mencolok. Tanaman ini mengandung berbagai senyawa bermanfaat seperti 
    glikosida, flavonoid, tanin, dan saponin. Karena kandungan tersebut, asoka memiliki beragam manfaat kesehatan.  
    
    Tanaman ini digunakan sebagai spasmogenik, oksitosik, uterotonik, anti-bakteri, anti-implantasi, anti-tumor, 
    anti-progestasional, dan antiestrogenik untuk mengatasi menorrhagia serta memiliki potensi sebagai anti-kanker. 
    Dalam teks Ayurveda India kuno, Saraca asoca (Roxb.) de Wilde (Saraca indica L.) yang termasuk dalam keluarga 
    Caesalpiniaceae, dianggap sebagai obat mujarab.  
    
    Asoka sangat efektif dalam mengatasi berbagai komplikasi dan infeksi ginekologi, serta disentri berdarah, nyeri 
    rahim, infeksi bakteri, masalah kulit, tumor, infestasi cacing, serta masalah jantung dan sirkulasi. Dengan begitu 
    banyak manfaat yang dimilikinya, tidak heran jika asoka dianggap sebagai salah satu tanaman obat yang sangat berharga.
    """)

    st.subheader("Manfaat")
    st.markdown("""
        Berikut adalah rangkuman manfaat Asoka, yaitu:

        * Disentri berdarah
        * Nyeri rahim
        * Infeksi bakteri
        """)

    st.markdown("""
    ## Referensi

    Pradhan, P., Joseph, L., Gupta, V., Chulet, R., Arya, H., Verma, R., & Bajpai, A. (2009). *Saraca asoca (Ashoka): A Review*. *Journal of Chemical and Pharmaceutical Research, 1*(1), 62–70.

    Singh, S., Krishna, T. H. A., Kamalraj, S., Kuriakose, G. C., Valayil, J. M., & Jayabaskaran, C. (2015). *Phytomedicinal importance of Saraca asoca (Ashoka): an exciting past, an emerging present and a promising future*. *Current Science, 109*(10), 1790–1800. https://doi.org/10.18520/v109/i10/1790-1801
    """)

def Cosmos():
    # Paragraf deskripsi
    #st.write("""Menjelaskan Detail bunga Marigold""")

    # Menyisipkan gambar
    st.image("https://raw.githubusercontent.com/Faizalilyas/WebTanamanRefugia/main/Bunga/cosmos.jpg", caption="Bunga Cosmos", use_column_width=True)

    #import streamlit as st

    # Judul utama
    st.title("Serba-serbi Bunga Cosmos")

    # Sub header Klasifikasi
    st.subheader("Klasifikasi")

    # Klasifikasi Tumbuhan
    st.write("""
    Kingdom: Plantae  
    Subkingdom: Tracheobionta  
    Superdivisi: Spermatophyta  
    Divisi: Magnoliophyta  
    Kelas: Magnoliopsida  
    Subkelas: Asteridae  
    Ordo: Asterales  
    Famili: Asteraceae  
    Genus: *Cosmos*  
    Spesies: *Cosmos caudatus* Kunth.
    """)

    # Sub header Morfologi
    st.header("Morfologi")

    # Deskripsi morfologi
    st.write(
        "Kenikir (*Cosmos caudatus*) merupakan tanaman perdu yang memiliki akar tunggang, batang kokoh, kuat, tegak, "
        "bercabang banyak dengan tinggi tanaman 75–100 cm. Daun kenikir tergolong daun majemuk, ujung runcing, tumbuh "
        "bersilang berhadapan, tepi rata, panjang 15-25 cm, dan berwarna hijau. Bunga kenikir tergolong bunga majemuk "
        "yang tumbuh di ujung batang. Mahkota bunga terdiri dari 8 helai daun dan berwarna merah muda."
    )

    # Sub header Sejarah
    st.header("Sejarah")

    # Deskripsi sejarah
    st.write(
        "*Cosmos* atau tumbuhan yang sering disebut kenikir merupakan tumbuhan yang berasal dari Amerika kemudian menyebar"
        " luas ke daerah tropis dengan nama binomial *Cosmos caudatus*. Nama ini disampaikan oleh Karl Sigismund Kunth "
        "tahun 1820. Kenikir merupakan salah satu spesies dari genus Cosmos yang terdiri dari 26 spesies dari "
        "keluarga/famili Asteraceae/Compositae. Kenikir pada umumnya ditemukan di pembatas sawah, tepi ladang dan semak "
        "belukar. Tanaman kenikir tahan terhadap cuaca panas dan dapat tumbuh di tempat yang terkena sinar matahari langsung."
    )

    st.header("Trivia!")
    st.markdown("""
                Biasa disebut daun kenikir atau Ulam Raja!""")

    st.header("Deskripsi dan Manfaat")

    st.subheader("Deskripsi")
    st.write("""
    Bunga Cosmos atau biasa disebut “daun kenikir” atau “Ulam Raja”. Menurut Yani (2023) dan Cheng dkk (2015), tanaman 
    ini banyak sekali memiliki kandungan vitamin C (asam askorbat), quercetin, vitamin B1 (tiamin), vitamin B2 
    (riboflavin), dan asam klorogenat. 
    """)

    st.subheader("Manfaat")
    st.markdown("""
        Berikut adalah manfaat Cosmos, yaitu:

        * Mencegah penyakit kronis karena kandungan antioksidan yang tinggi
        * Mencegah gangguan pencernaan karena kandungan flavonoid antioksidannya
        * Mencegah hipertensi karena efek diuretiknya
        * Menurunkan risiko penyakit diabetes karena menghambat proses penyerapan glukosa dalam sistem pencernaan
        * Mencegah osteoporosis dan mendukung pembentukan dan perbaikan kondisi tulang dalam tubuh
        * Mempunyai efek antiinflamasi dan antimikroba
        """)

    st.header("Cara Penggunaan")
    st.markdown("""
    Bisa dimakan langsung sebagai lalapan atau direbus
    """)

    st.markdown("""
    ## Referensi

    Barakatun-Nisak, M. Y., Cheng, S.-H., Anthony, J., & Ismail, A. (2015). Potential medicinal benefits of Cosmos caudatus (Ulam Raja): A scoping review. 
    *Journal of Research in Medical Sciences, 20*(10), 1000. https://doi.org/10.4103/1735-1995.172796  
    
    Yani, I. F. (2021, February 1). *4 Manfaat Daun Kenikir, Sayuran yang Kerap Disantap Sebagai Lalapan*. 
    Hello Sehat. https://hellosehat.com/herbal-alternatif/herbal/manfaat-daun-kenikir-untuk-kesehatan/
    """)

def SugarBerry():
    # Paragraf deskripsi
    #st.write("""Menjelaskan Detail bunga Marigold""")

    # Menyisipkan gambar
    st.image("https://raw.githubusercontent.com/Faizalilyas/WebTanamanRefugia/main/Bunga/sugarberry.jpg", caption="Bunga Sugar Berry", use_column_width=True)

    #import streamlit as st

    # Judul utama
    st.title("Serba-serbi Sugar Berry")

    # Sub header Klasifikasi
    st.subheader("Klasifikasi")

    # Klasifikasi Tumbuhan
    st.write("""
    Kingdom: Plantae        
    Subkingdom: Tracheobionta       
    Superdivisi: Spermatophyta      
    Divisi: Magnoliophyta       
    Kelas: Magnoliopsida        
    Subkelas: Caryophyllidae        
    Ordo: Caryophyllales  
    Famili: Amaranthaceae  
    Genus: *Gomphrena*  
    Spesies: *Gomphrena globosa* L.
    """)

    # Sub header Morfologi
    st.header("Morfologi")

    # Deskripsi morfologi
    st.write(
        "*Sugar berry* atau disebut bunga kenop memiliki akar tunggang berwarna kuning kecokelatan. Batang berwarna hijau "
        "kemerahan, berambut, membesar pada ruas percabangannya. Bunga berbentuk kancing bernuansa ungu, pink, merah, "
        "orange, magenta, biru, lavender hingga putih. Daun berbentuk bulat telur dengan ujung meruncing, dimana bagian "
        "atas berambut putih dan kasar, bawah berambut halus. Buah berbentuk segitiga, terbungkus lapisan tipis berwarna"
        " putih, berbiji kotak."
    )

    # Sub header Sejarah
    st.header("Sejarah")

    # Deskripsi sejarah
    st.write(
        "Tanaman sugar berry atau bunga kenop berasal dari Panama, Brazil, dan Guatemala yang kemudian menyebar ke Asia "
        "sebagai tanaman yang digunakan dalam pengobatan tradisional juga tanaman hias karena memiliki bentuk dan warna "
        "bunga yang tahan lama dan unik."
    )

    st.header("Trivia!")
    st.markdown("""
                """)

    st.header("Deskripsi dan Manfaat")

    st.subheader("Deskripsi")
    st.write("""
    Bunga ini memiliki kandungan senyawa kimia berupa Saponin, polifenol, betacyanin (amaranthin), minyak atsiri, 
    flavonoid, fenolik, gomphresin I, II, III, V dan VI, tanin galat, steroid/triterpenoid, kumarin.
    """)

    st.subheader("Manfaat")
    st.markdown("""
        Melawan sel kanker, detoksifikasi, menurunkan tekanan darah tinggi, mengatasi masalah prostat, mencegah penuaan 
        dini, antioksidan, antiasmatik, antiradang mata, antidiare, sesak nafas, mengobati luka, penglihatan kurang 
        terang, bronkitis, dan sakit kepala.
        """)

    st.markdown("""
    ## Referensi

    Socfindo Conservation. (2024). *Gomphrena globosa*. Bunga Kenop. https://www.socfindoconservation.co.id/plant/397

    """)


def JenggerAyam():
    # Paragraf deskripsi
    # st.write("""Menjelaskan Detail bunga Marigold""")

    # Menyisipkan gambar
    st.image("https://raw.githubusercontent.com/Faizalilyas/WebTanamanRefugia/main/Bunga/jengger%20ayam.jpg",
             caption="Bunga Jengger Ayam", use_column_width=True)

    # import streamlit as st

    # Judul utama
    st.title("Serba-serbi Jengger Ayam")

    # Sub header Klasifikasi
    st.subheader("Klasifikasi")

    # Klasifikasi Tumbuhan
    st.write("""
    Kingdom: Plantae  
    Subkingdom: Tracheobionta  
    Superdivisi: Spermatophyta  
    Divisi: Magnoliophyta  
    Kelas: Magnoliopsida  
    Subkelas: Caryophyllidae  
    Ordo: Caryophyllales  
    Famili: Amaranthaceae  
    Genus: *Celosia*  
    Spesies: *Celosia cristata* L.
    """)

    # Sub header Morfologi
    st.header("Morfologi")

    # Deskripsi morfologi
    st.write(
        """
        * **Akar** tunggang.
        * **Batang** tebal dan kuat, bercabang, beralur.
        * **Daun** bulat telur sampai memanjang, ujung meruncing, berselang-seling.
        * **Bunga** majemuk berbentuk bulir, tebal berdaging, bentuk seperti jengger ayam.
        * **Buah** bulat telur, merah kehijauan, retak sewaktu masak.
        * **Biji** berukuran kecil dan berwarna hitam.
        """
    )

    # Sub header Sejarah
    st.header("Sejarah")

    # Deskripsi sejarah
    st.write(
        "Jengger ayam diperkirakan berasal dari Afrika, India, dan Amerika Utara juga tersebar luas di beberapa daerah "
        "di Asia. Jengger ayam atau jewer kotok (*Celosia cristata*) adalah varietas dari *celosia argentea*. Spesies ini "
        "diidentifikasi tahun 1753 oleh Linnaeus, kemudian diidentifikasi ulang sebagai varietas (bukan spesies) dari "
        "*Celosia argentea* oleh Kuntze pada 1891 menjadi *Celosia argentea var. cristata*."
    )

    # st.header("Trivia!")
    # st.markdown("""
    #             """)

    st.header("Deskripsi dan Manfaat")

    st.subheader("Deskripsi")
    st.write("""
    Jengger Ayam, yang dikenal dengan berbagai nama lokal seperti Banda ulu (Toba), Bayem cenggeng (Jawa), dan Jawer 
    kotok (Sunda), merupakan tanaman yang kaya akan kandungan senyawa bioaktif. Bunganya mengandung kaempferitrin, 
    amaranthin, pinitol amarantin, dan isocelosianin. Daunnya mengandung saponin, flavonoida, dan polifenol. Biji 
    Jengger Ayam mengandung fenolik, celosialdehyde, saponin (cristatin, celosin A-D), flavonoid, steroid, dan 
    triterpenoid. Kandungan-kandungan ini menjadikan Jengger Ayam potensial untuk berbagai aplikasi kesehatan dan 
    pengobatan tradisional.
    """)

    st.subheader("Manfaat")
    st.markdown("""
        Jengger Ayam, yang juga dikenal dengan berbagai nama lokal seperti Banda ulu (Toba), Bayem cenggeng (Jawa), dan 
        Jawer kotok (Sunda), memiliki banyak manfaat. Beberapa manfaatnya termasuk mengatasi gigitan serangga, gangguan 
        penglihatan, anti radang (antiinflamasi), kencing nanah, haid tidak teratur, kejang perut, diare, disentri, 
        keputihan, mata merah, serta menghentikan pendarahan seperti mimisan, batuk darah, muntah darah, air kemih 
        berdarah, wasir berdarah, dan pendarahan rahim. Selain itu, tanaman ini juga dapat mengobati infeksi saluran 
        kencing dan meredakan demam.
        """)

    st.markdown("""
    ## Referensi
    
    Socfindo Conservation. (2024). *Celosia cristata*. Jengger Ayam. https://www.socfindoconservation.co.id/plant/303
    """)


def LilyHujan():
    # Paragraf deskripsi
    # st.write("""Menjelaskan Detail bunga Marigold""")

    # Menyisipkan gambar
    st.image("https://raw.githubusercontent.com/Faizalilyas/WebTanamanRefugia/main/Bunga/Lily%20hujan.jpg",
             caption="Bunga Lily Hujan", use_column_width=True)

    # import streamlit as st

    # Judul utama
    st.title("Serba-serbi Miana")

    # Sub header Klasifikasi
    st.subheader("Klasifikasi")

    # Klasifikasi Tumbuhan
    st.write("""
    Kingdom: Plantae  
    Subkingdom: Tracheobionta  
    Superdivisi: Spermatophyta  
    Divisi: Magnoliophyta  
    Kelas: Liliopsida  
    Subkelas: Liliidae  
    Ordo: Liliales  
    Famili: Amaryllidaceae  
    Genus: *Zephyranthes*  
    Spesies: *Zephyranthes candida* (Lindl.) Herb. 
    """)

    # Sub header Morfologi
    st.header("Morfologi")

    # Deskripsi morfologi
    st.write("""
        * **Akar** serabut, berwarna putih.  
        * **Batang** semu, memiliki umbi lapis, diameter 2–4 cm, putih sedikit kecokelatan.
        * **Daun** tunggal, muncul di roset akar, tidak bertangkai, bentuk garis, ukuran panjang 20-30 cm, pertulangan 
        sejajar, permukaan licin, tebal, berwarna hijau. Berbentuk memanjang menyerupai daun bawang.
        * **Bunga** tunggal, berbentuk terompet, berkelamin ganda. Kelopak tipis, berlekatan. Benang sari berjumlah 6, 
        berwarna kuning. Mahkota berlepasan, berjumlah 6 helai, berwarna putih kekuningan.
        * **Buah** memiliki 3 ruang, bentuk lonjong, ukuran panjang 0,5–1 cm dan berwarna hijau.
        * **Biji** berjumlah banyak, pipih, hitam, mengkilat.
        """
    )

    # Sub header Sejarah
    st.header("Sejarah")

    # Deskripsi sejarah
    st.write(
        "Lili hujan berasal dari Meksiko, Kolombia, dan Amerika Tengah. Dibudidayakan secara luas di Amerika bagian selatan, bagian selatan "
        "USA, kepulauan Ryukyu, Bhutan, Nepal, dan Kepulauan Solomon. Dinamakan 'lili hujan' karena umumnya tumbuh dan mekar setelah musim hujan."
    )

    # st.header("Trivia!")
    # st.markdown("""
    #             """)

    st.header("Deskripsi dan Manfaat")

    st.subheader("Deskripsi")
    st.write("""
    *Zephyranthes* candida, atau yang dikenal sebagai lili hujan (Autumn lily), memiliki nama lokal di Jawa sebagai Bawang
     sebrang dan Bunga lili putih. Tanaman ini dapat dibudidayakan melalui dua metode, yaitu secara generatif 
     menggunakan biji, dan secara vegetatif dengan pemisahan umbi atau anakan.  
     Secara kimiawi, Zephyranthes candida mengandung beberapa alkaloid seperti 12-acetylplicamine, 
     N-deformyl-secoplicamine, plicamine, 4a-epi-plicamine, secoplicamine, dan lycorine. Selain itu, tanaman ini juga 
     memiliki β-sitosterol, stigmasterol, β-dauscosterin, dan heptacosane.

    """)

    st.subheader("Manfaat")
    st.markdown("""
    Meredakan kejang pada anak-anak, membantu menghilangkan bekas luka, gigitan serangga, obat pusing, mengatasi sulit 
    tidur, menurunkan demam (Socfindo Conservation, 2024). Menurut Kaliammal *et al* (2021) bunga lili hujan memiliki 
    aktivitas antiinflamasi, antidiabetes, antioksidan, dan antikanker. 
    """)


    st.markdown("""
    ### Referensi

    Kaliammal, R., Parvathy, G., Maheshwaran, G., Velsankar, K., Kousalya Devi, V., Krishnakumar, M., & Sudhahar, S. 
    (2021). Zephyranthes candida flower extract mediated green synthesis of silver nanoparticles for biological 
    applications. *Advanced Powder Technology*, 32(11), 4408–4419. https://doi.org/10.1016/j.apt.2021.09.045

    Socfindo Conservation. (2024). *Zephyranthes candida*. Socfindo Conservation. https://www.socfindoconservation.co.id/plant/635

    
    """)


def Pancawarna():
    # Paragraf deskripsi
    # st.write("""Menjelaskan Detail bunga Marigold""")

    # Menyisipkan gambar
    st.image("https://raw.githubusercontent.com/Faizalilyas/WebTanamanRefugia/main/Bunga/pancawarna.jpg",
             caption="Bunga Pancawarna", use_column_width=True)

    # import streamlit as st

    # Judul utama
    st.title("Serba-serbi Bunga Pancawarna")

    # Sub header Klasifikasi
    st.subheader("Klasifikasi")

    # Klasifikasi Tumbuhan
    st.write("""
    Kingdom: Plantae  
    Subkingdom: Tracheobionta  
    Superdivisi: Spermatophyta  
    Divisi: Magnoliophyta  
    Kelas: Magnoliopsida  
    Subkelas: Rosidae  
    Ordo: Rosales  
    Famili: Hydrangeaceae  
    Genus: *Hydrangea*  
    Spesies: *Hydrangea macrophylla*  
    """)

    # Sub header Morfologi
    st.header("Morfologi")

    # Deskripsi morfologi
    st.write(
        """
        * **Akar** serabut, kecokelatan.  
        * **Batang** tegak, kuat, berkayu, hijau.
        * **Daun** tunggal, bertangkai, letak berhadapan bersilang. Helaian daun lebar dan tebal, bulat telur, pangkal 
        dan ujungnya runcing, tepi bergerigi, tulang daun menyirip, permukaan daun hijau tua dan bagian bawah hijau kekuningan.
        * **Bunga** majemuk, keluar dari ujung tangkai, membentuk rangkaian membulat, diameter mencapai 20 cm. 
        Berwarna hijau (kuncup), berubah menjadi putih, sewaktu mekar berwarna biru muda atau merah jambu.
        """
    )

    # Sub header Sejarah
    st.header("Sejarah")

    # Deskripsi sejarah
    st.write(
        "Hortensia merupakan tumbuhan berbunga yang berasal dari Asia (Jepang, Tiongkok, Himalaya, Indonesia), Amerika "
        "Utara, dan Amerika Selatan. Sebagian besar spesies berasal dari Jepang dan Tiongkok. "
    )

    # st.header("Trivia!")
    # st.markdown("""
    #             """)

    st.header("Deskripsi dan Manfaat")

    st.subheader("Deskripsi")
    st.write("""
    Bunga pancawarna atau hortensia (Hydrangea macrophylla) adalah bunga cantik yang memiliki nama lain Bunga Tiga 
    Bulan di daerah Melayu, Bunga Masamba di Sulawesi Selatan, dan Kembang Bokor. Adapun budidaya tanaman ini bisa 
    dilakukan secara generatif (biji) dan vegetatif (stek batang dan stek tunas). Stek batang yang dipilih adalah 
    batang yang memiliki panjang 15 cm, tidak memiliki bunga, dan merupakan pertumbuhan baru.   
  
    **Kandungan bahan kimia:** Isocoumarin, secoiridoid glucosida, phyllodulcin, polifenol, flavonoid, 
    triterpenoid/steroid, antrakinon, zeorin, betulinic acid, uridine, thymidine, adenosine, nicotinamide, 
    methyl pyroglutamate, hydrangenol.
    """)

    st.subheader("Manfaat")
    st.markdown("""
    * Daun muda dapat dikonsumsi setelah masak. Daun dapat dijadikan teh dan penyedap makanan
    * Mengobati diare, malaria, diabetes, kebotakan rambut, demam, gelisah (ansietas), sakit tenggorokan, memiliki aktivitas sebagai antikanker dan antiradang, mengatasi masalah infeksi saluran kemih, pembesaran prostat, dan batu ginjal.
    * Memiliki sifat antioksidan, antiinflamasi; dan berpotensi menurunkan gula darah, melindungi liver, dan membantu melawan kanker
    """)

    st.markdown("""
    ### Referensi

    Lang, A. (2021, February 25). *Hydrangea root: Supplements, uses, and benefits*. 
    Healthline Media. https://www.healthline.com/nutrition/hydrangea-root

    Socfindo Conservation. (2024). *Hydrangea macrophylla*. Socfindo Conservation. https://www.socfindoconservation.co.id/plant/237

    """)


def Krokot():
    # Paragraf deskripsi
    # st.write("""Menjelaskan Detail bunga Marigold""")

    # Menyisipkan gambar
    st.image("https://raw.githubusercontent.com/Faizalilyas/WebTanamanRefugia/main/Bunga/krokot%20bunga.jpg",
             caption="Krokot Bunga", use_column_width=True)

    # import streamlit as st

    # Judul utama
    st.title("Serba-serbi Krokot")

    # Sub header Klasifikasi
    st.subheader("Klasifikasi")

    # Klasifikasi Tumbuhan
    st.write("""
    Kingdom: Plantae  
    Subkingdom: Tracheobionta  
    Superdivisi: Spermatophyta  
    Divisi: Magnoliophyta  
    Kelas: Magnoliopsida  
    Subkelas: Caryophyllidae  
    Ordo: Caryophyllales  
    Famili: Portulacaceae  
    Genus: *Portulaca*  
    Spesies: *Portulaca biloba* Urb.
   
    """)

    # Sub header Morfologi
    st.header("Morfologi")

    # Deskripsi morfologi
    st.write(
        """
        Akar krokot terdiri dari akar tunggang berwarna putih yang mana akarnya panjang dan tebal serta banyak akar 
        lateral yang berserat. Batang memiliki warna hijau kemerahan, bulat, halus, berdaging, beruas, tidak memiliki 
        bulu selain ketiak. Daun tunggal, berdaging, tebal, pangkal dan ujung tumpul, tepi daun rata warna hijau, 
        panjang 1-3 cm, dan lebar 1-2 cm. Bunga majemuk, letaknya di ujung cabang, kecil, kelopak berwarna hijau, 
        mahkota berbentuk jantung warna kuning, kepala putiknya berjumlah tiga sampai lima berwarna putih, atau kuning. 
        Buah berbentuk kotak, berbiji banyak, hijau. Biji bentuk bulat, kecil mengkilat, dan hitam.
        """
    )

    # Sub header Sejarah
    st.header("Sejarah")

    # Deskripsi sejarah
    st.write(
        "Krokot diperkirakan berasal dari daratan Amerika tropis (Brazil) yang tersebar di daerah tropis dan daerah "
        "bermusim empat. Tanaman krokot ini tumbuh liar dan mudah kita jumpai di segala tempat mulai dari persawahan, "
        "ladang, dan tepi jalan. Dalam bahasa inggris tanaman krokot ini mempunyai nama common purslane, little hogweed."
    )

    # st.header("Trivia!")
    # st.markdown("""
    #             """)

    st.header("Deskripsi dan Manfaat")

    st.subheader("Deskripsi")
    st.write("""
    Bunga krokot (*Portulaca biloba*) merupakan tanaman genus *Portulaca* yang biasa dikonsumsi. Spesies jenis P. *biloba* 
    belum banyak diteliti, tetapi jenis P. *oleracea* yang juga masih dalam jenis bunga krokot (Purslane) memiliki 
    kandungan senyawa berupa Alkaloid, steroid/terpenoid, tanin, saponin, flavonoid, asam organik (asam oksalat, asam 
    kafein, asam malat, asam sitrat), asam lemak omega 3, kumarin, glikosida jantung, antrakuinon, asam linoleat, 
    glikosida monoterpen, vitamin C, vitamin A, glutation, oleoresins-I dan II, N-trans-feruloil tiramin, sakarida, 
    triterpenoid, dan sebagainya (Socfindo Conservation, 2024; Ramadan *et al*., 2017).

    """)

    st.subheader("Manfaat")
    st.markdown("""
    Tanaman ini memiliki efek antidiabetes dan dapat dikonsumsi sebagai makanan. Selain itu, tanaman ini juga digunakan 
    untuk mengobati radang akut usus buntu, disentri, diare akut, radang payudara, keputihan, gangguan sistem saluran 
    kencing, buang air kecil berdarah, sakit kuning, cacingan, sesak napas, luka, serta membantu mengatasi kondisi tubuh
     yang lemah, lesu, dan pegal.
    """)

    st.markdown("""
    ### Referensi

    Ramadan, B. K., Schaalan, M. F., & Tolba, A. M. (2017). Hypoglycemic and pancreatic protective effects of Portulaca 
    oleracea extract in alloxan induced diabetic rats. *BMC Complementary and Alternative Medicine, 17*(1). 
    https://doi.org/10.1186/s12906-016-1530-1
    
    Socfindo Conservation. (2024). *Portulaca oleracea*. Socfindo Conservation. https://www.socfindoconservation.co.id/plant/239

    """)


def Genjik():
    # Paragraf deskripsi
    # st.write("""Menjelaskan Detail bunga Marigold""")

    # Menyisipkan gambar
    st.image("https://raw.githubusercontent.com/Faizalilyas/WebTanamanRefugia/main/Bunga/genjik.jpg",
             caption="Bunga Genjik", use_column_width=True)

    # import streamlit as st

    # Judul utama
    st.title("Serba-serbi Genjik")

    # Sub header Klasifikasi
    st.subheader("Klasifikasi")

    # Klasifikasi Tumbuhan
    st.write("""
    Kingdom: Plantae  
    Subkingdom: Tracheobionta  
    Superdivisi: Spermatophyta  
    Divisi: Magnoliophyta  
    Kelas: Magnoliopsida  
    Subkelas: Asteridae  
    Ordo: Asterales  
    Famili: Asteraceae  
    Genus: *Eupatorium*  
    Spesies: *Eupatorium triplinerve* Vahl.   
    """)

    # Sub header Morfologi
    st.header("Morfologi")

    # Deskripsi morfologi
    st.write(
        """
        Tanaman prasman (Eupatorium triplinerve V), merupakan salah satu tanaman berbentuk semak, dengan tinggi tumbuhan 
        45 cm, daunnya tunggal berhadapan, helaian daun berbentuk lanset, warnanya hijau keunguan. Batangnya merupakan 
        batang berkayu, beruas-ruas, bentuk batang bulat, arah tumbuh batang serong dan warnanya merah keunguan. 
        Memiliki akar tunggang, berwarna kecoklatan dan permukaan akar bergerigi.
        * **Akar** tunggang  
        * **Batang** berbulu, berwarna kemerahan, tunas muda berwarna keputihan, beruas-ruas, bercabang.
        * **Daun** tunggal, berhadapan, berbentuk lanset, ujung daun runcing, pangkal meruncing, tepi rata, permukaan licin.
        * **Bunga** majemuk, bentuk tabung, keluar dari ujung batang. Berkelopak lepas yang terdiri atas lima daun 
        kelopak dan berwarna hijau keunguan. Mahkota berbentuk bintang, kecil, berbulu putih, berwarna ungu kemerahan.
        * **Buah** berupa buah kendaga, lonjong dan sempit, panjang 2 mm, bersudut lima.
        """
    )

    # Sub header Sejarah
    st.header("Sejarah")

    # Deskripsi sejarah
    st.write(
        "Prasman berasal dari Brazil hingga Suriname dan telah banyak dibudidayakan di berbagai negara seperti Afrika, "
        "India, China, Filipina, dan Indonesia. Prasman sering ditanam masyarakat sebagai tanaman penutup tanah di "
        "perkebunan, tanaman pagar, tanaman hias juga tanaman obat. Prasman juga menghasilkan minyak yang dapat "
        "digunakan untuk wewangian (parfum), serta daunnya dapat digunakan untuk membuat teh dengan rasa yang pedas. "
        "Di India daun prasman digunakan sebagai obat malaria."
    )

    # st.header("Trivia!")
    # st.markdown("""
    #             """)

    st.header("Deskripsi dan Manfaat")

    st.subheader("Deskripsi")
    st.write("""
    Genjik atau Daun Prasman (*Eupatorium triplinerve*) merupakan tanaman yang memiliki 2 sinonim, yaitu *E. triplinerve 
    M. Vahl* dan *E. ayapana Vent*. Prasman tumbuh dengan baik di ketinggian 16 00 m dpl di dataran rendah dan dataran tinggi. 
    Mereka dapat berkembang biak secara generatif melalui biji atau secara vegetatif buatan melalui stek akar. 
    Tanaman prasman berkembang biak dengan cepat. Minyak atsiri dari daun prasman terdiri dari senyawa kumarin, turunan, 
    dan thimohdrokinono, yang memiliki aroma dan warna hijau muda yang khas.

    """)

    st.subheader("Manfaat")
    st.markdown("""
    Tanaman prasman biasanya digunakan untuk menutup tanah di perkebunan karet dan teh. Mereka juga digunakan sebagai 
    tanaman obat untuk mengobati demam, diare, pilek, batuk, asma, sariawan, kurang nafsu makan, sakit kepala, haid 
    tidak teratur, dan sakit kepala. Selain itu, tanaman ini memiliki potensi antinosiseptif dan antioksidan yang sudah 
    diujikan pada tikus (Melo *et al*., 2013). Ekstrak metanol terfraksinasi dari tanaman ini memiliki efek antimikroba 
    (Matos Lopes *et al*., 2014). Ekstrak petroleum-eter dari tanaman ini juga memiliki potensi antinosiseptif serta 
    antiinflamasi (Parimala *et al*., 2012). Kumarin dan konstituen polar dari tanaman ini juga memiliki potensi 
    alpha-glucosidase inhibitor (Viet Huong *et al*., 2020). 
    """)

    st.markdown("""
    ### Referensi

    bibitbunga. (2024). *Tanaman prasman*. Bibit Bunga. https://bibitbunga.com/product/prasman/
    
    Matos Lopes, T. R., de Oliveira, F. R., Malheiros, F. F., de Andrade, M. A., Monteiro, M. C., & Baetas Gonçalves, 
    A. C. (2014). Antimicrobial bioassay-guided fractionation of a methanol extract ofEupatorium triplinerve. 
    *Pharmaceutical Biology*, 53(6), 897–903. https://doi.org/10.3109/13880209.2014.948634
    
    Melo, A. S., Monteiro, M. C., da Silva, J. B., de Oliveira, F. R., Vieira, J. L. F., de Andrade, M. A., Baetas, 
    A. C., Sakai, J. T., Ferreira, F. A., Cunha Sousa, P. J. da, & Maia, C. do S. F. (2013). Antinociceptive, 
    neurobehavioral and antioxidant effects of Eupatorium triplinerve Vahl on rats. *Journal of Ethnopharmacology*, 147(2), 
    293–301. https://doi.org/10.1016/j.jep.2013.03.002
    
    Parimala, K., Cheriyan, B. V., & VIswanathan, S. (2012). Antinociceptive and anti-inflammatory activity of 
    petroleum- ether extract of eupatorium triplinerve vahl. *International Journal of Life Science & Pharma Search*, 2(3), 12–18.
    
    Viet Huong, D. T., Giang, P. M., & Trang, V. M. (2020). Coumarins and Polar Constituents from Eupatorium 
    triplinerve and Evaluation of Their α-Glucosidase Inhibitory Activity. *Journal of Chemistry*, 2020(1), 1–8. 
    https://doi.org/10.1155/2020/8945063


    """)


def Begonia():
    # Paragraf deskripsi
    # st.write("""Menjelaskan Detail bunga Marigold""")

    # Menyisipkan gambar
    st.image("https://raw.githubusercontent.com/Faizalilyas/WebTanamanRefugia/main/Bunga/begonia.jpg",
             caption="Bunga Begonia", use_column_width=True)

    # import streamlit as st

    # Judul utama
    st.title("Serba-serbi Begonia")

    # Sub header Klasifikasi
    st.subheader("Klasifikasi")

    # Klasifikasi Tumbuhan
    st.write("""
    Kingdom: Plantae  
    Subkingdom: Tracheobionta  
    Superdivisi: Spermatophyta  
    Divisi: Magnoliophyta  
    Kelas: Magnoliopsida  
    Subkelas: Dilleniidae  
    Ordo: Violales  
    Famili: Begoniaceae  
    Genus: *Begonia*    
    Spesies: *Begonia cucullata* Willd.
    """)

    # Sub header Morfologi
    st.header("Morfologi")

    # Deskripsi morfologi
    st.write(
        """
        * **Akar** tunggang, berwarna putih kotor.  
        * **Batang** hijau kemerahan, jarang berbulu ketika muda, berbulu ketika dewasa.
        * **Daun** tunggal, duduk seperti roset akar, bentuk asimetris, ujung hampir bulat, daun bagian atas mengkilap, 
        hijau pucat di bawah berbulu halus, tepi bergerigi, pertulangan menjari.
        * **Bunga** majemuk, bentuk malai, tangkai panjang 80-90 cm, daun pelindung satu, tipis, panjang 5-6 cm, lebar 
        3-4 cm, berbulu halus, benang sari terbagi tiga, berpasang-pasangan, mahkota bersayap tiga, satu lebar, dua lainnya pendek, putih sampai merah jambu.
        * **Buah** kapsul, panjang 24-30 mm, bersayap 3 tidak sama besar.
        * **Biji** berbentuk bulat, berukuran kecil, dan berwarna putih.
        """
    )

    # Sub header Sejarah
    st.header("Sejarah")

    # Deskripsi sejarah
    st.write(
        "*Begonia cucullata* merupakan tanaman asli Amerika Selatan, yang tersebar mulai dari Bolivia hingga Brazil dan "
        "Argentina Utara. Umumnya dibudidayakan sebagai tanaman hias yang biasanya diletakkan di dalam pot. Secara "
        "tradisional, tanaman ini memiliki khasiat sebagai obat. Di Paraguay, getahnya dimanfaatkan untuk mengobati "
        "sakit tenggorokan. Selain itu, daun dan bunganya dapat dikonsumsi, baik mentah maupun dimasak."
    )

    # st.header("Trivia!")
    # st.markdown("""
    #             """)

    st.header("Deskripsi dan Manfaat")

    st.subheader("Deskripsi")
    st.write("""
    Tanaman begonia (*Begonia cucullata*) biasa disebut Riang-riang di Sumatera Utara. Tidak hanya itu, nama lain dari 
    tanaman ini juga adalah Hariang. Begonia tumbuh liar di hutan tropis basah dan memiliki kandungan flavonoid, 
    fenolik, asam oksalat, dan antioksidan. Budidaya secara vegetatif bisa melalui stek daun dan juga secara generatif melalui biji.

    """)

    st.subheader("Manfaat")
    st.markdown("""
    Mengobati luka, kutil, demam, batuk, sakit perut, pembengkakan limpa, sakit gigi dan gusi, sakit tenggorokan, 
    cegukan, diare, disentri, malaria, dan berfungsi sebagai analgesik, antiinflamasi, pencahar, dan diuretik. 
    """)

    st.markdown("""
    ### Referensi

    Socfindo Conservation. (2024). *Begonia cucullata*. Socfindo Conservation. https://www.socfindoconservation.co.id/plant/401
    """)


def Adas():
    # Paragraf deskripsi
    # st.write("""Menjelaskan Detail bunga Marigold""")

    # Menyisipkan gambar
    st.image("https://raw.githubusercontent.com/Faizalilyas/WebTanamanRefugia/main/Bunga/adas.jpg",
             caption="Adas", use_column_width=True)

    # import streamlit as st

    # Judul utama
    st.title("Serba-serbi Adas")

    # Sub header Klasifikasi
    st.subheader("Klasifikasi")

    # Klasifikasi Tumbuhan
    st.write("""
    Kingdom: Plantae  
    Subkingdom: Tracheobionta  
    Superdivisi: Spermatophyta  
    Divisi: Magnoliophyta  
    Kelas: Magnoliopsida  
    Subkelas: Rosidae  
    Ordo: Apiales  
    Famili: Apiaceae  
    Genus: *Foeniculum*  
    Spesies: *Foeniculum foeniculum* L.
    """)

    # Sub header Morfologi
    st.header("Morfologi")

    # Deskripsi morfologi
    st.write(
        """ 
        * **Batang** berbentuk galah dengan alur sejajar, bercabang banyak.
        * **Daun** berbentuk silinder terbuka, panjang 2-15 cm.
        * **Bunga** majemuk dengan 6-40 gagang bunga, mahkota kuning, keluar dari ujung batang.
        * **Buah** lonjong, berusuk, panjang 6-10 mm, lebar 3-4 mm, saat muda berwarna hijau, dan berwarna cokelat agak 
        hijau atau kuning sampai sepenuhnya cokelat saat tua atau matang.
        """
    )

    # Sub header Sejarah
    st.header("Sejarah")

    # Deskripsi sejarah
    st.write(
        "Berasal dari Eropa Selatan dan daerah Mediterania. Secara liar, tumbuh di garis pantai Mediterania dan Mesir, "
        "kemudian dibudidayakan secara meluas di seluruh dunia. Adas banyak digunakan sebagai bumbu penyedap masakan "
        "dan tanaman obat. Tanaman ini juga menghasilkan minyak esensial, yang digunakan sebagai bahan deterjen dan "
        "kosmetik seperti sabun, krim, lotion, dan parfum mewah."
    )

    # st.header("Trivia!")
    # st.markdown("""
    #             """)

    st.header("Deskripsi dan Manfaat")

    st.subheader("Deskripsi")
    st.write("""
    Tanaman Adas (*Foeniculum vulgare*) juga disebut sebagai Adas pedas (Aceh), Hades (Sunda), Adas landa, Adas landi, 
    Adas welanda (Jawa), Adhas (Madura), Papang, Pampas (Manado), Papas (Alfuru), Wala wunga (Sumba), Adasa rempasu 
    (Makassar), dan Denggu-denggu (Gorontalo). Tanaman ini dapat diperbanyak dengan biji atau anakan.

    Bahan kimia yang terkandung dalam daun termasuk funikularin, nelumbosida, pinen, felandren, kaempferol-3-glukuronida, 
    limonen, dan kuersetin-3-glukuronida. Flavonoid, terpenoid, alkaloid, fenol, sterol, estragole, asam gallik, dan 
    L-limonene adalah bagian dari biji.

    """)

    st.subheader("Manfaat")
    st.markdown("""
    Minyak esensial untuk deterjen dan kosmetik (sabun, krim, lotion, dan parfum mewah) dan bumbu penyedap masakan 
    digunakan untuk mengobati batuk, sakit perut, sariawan, susah tidur, haid tidak teratur, peluruh air seni, pencahar, 
    albuminuria (protein albumin tinggi dalam urin), meningkatkan nafsu makan, dan mengobati infeksi jamur. 
    """)

    st.markdown("""
    ### Referensi

    Socfindo Conservation. (2024). *Foeniculum vulgare*. Socfindo Conservation. https://www.socfindoconservation.co.id/plant/145
    """)

def main():
    st.title("Jenis Tanaman Kebun Refugia")
    st.sidebar.image("https://raw.githubusercontent.com/Faizalilyas/WebTanamanRefugia/main/Bunga/Logo%20Refugia.jpg", use_column_width=True)
    tab = st.sidebar.radio("**Macam-macam Tanaman di Kebun Refugia**", ["Marigold", "Taiwan Beauty", "Vinca Major", "Miana",
                                                               "Bunga Kertas","Asoka","Bunga Cosmos", "Sugar Berry", "Jengger Ayam",
                                                               "Lily Hujan", "Bunga Pancawarna", "Krokot", "Genjik", "Begonia", "Adas"])

    if tab == "Marigold":
        st.header("Bunga Marigold")
        marigold()
    elif tab == "Taiwan Beauty":
        st.header("Taiwan Beauty")
        TaiwanBeauty()
    elif tab == "Vinca Major":
        st.header("Vinca Major")
        Vincamajor()
    elif tab == "Miana":
        st.header("Miana")
        Miana()
    elif tab == "Bunga Kertas":
        st.header("Bunga kertas")
        Zinnia()
    elif tab == "Asoka":
        st.header("Asoka")
        Asoka()
    elif tab == "Bunga Cosmos":
        st.header("Bunga Cosmos")
        Cosmos()
    elif tab == "Sugar Berry":
        st.header("Sugar Berry")
        SugarBerry()
    elif tab == "Jengger Ayam":
        st.header("Jengger Ayam")
        JenggerAyam()
    elif tab == "Lily Hujan":
        st.header("Lily Hujan")
        LilyHujan()
    elif tab == "Bunga Pancawarna":
        st.header("Bunga Pancawarna")
        Pancawarna()
    elif tab == "Krokot":
        st.header("Krokot")
        Krokot()
    elif tab == "Genjik":
        st.header("Genjik")
        Genjik()
    elif tab == "Begonia":
        st.header("Begonia")
        Begonia()
    elif tab == "Adas":
        st.header("Adas")
        Adas()

if __name__ == "__main__":
    main()
