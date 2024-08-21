Dibawah ini adalah CLI untuk mengkonfigurasi settings didalam Android.
*Test On Redmi note 9 pro Android 14 HyperOs

* Dalam CLI settings, terbagi menjadi 3 Kategori:
1. system
2. global
3. secure

untuk melihat variabel dan nilai - nilai yang tertera, perlu menggunakan perintah "settings list <Kategori>" 
contoh:
```settings list system```
Untuk melihat konfigurasi varibel dan nilai yang ada pada pengaturan system

* Mendelete/menghapus/mendisable
Gunakan perintah "settings delete <kategori> <kata_kunci>"
Contoh:
```settings delete system double_click_power_key```
Untuk mematikan fitur Flashlight dengan menekan tombol power 2x

* Memasukkan nilai/mengaktifkan
Gunakan perintah "settings put <kategori> <kata_kunci> <nilai>"
Contoh:
```settings put system double_click_power_key turn_on_torch```
Untuk mengaktifkan fitur Flashlight dengan menekan tombol power 2x

Berikut ini adalah sedikit 'kata_kunci dan nilai' yang saya perlukan didalam kategori `system` atau tepatnya didalam "Settings > Pintasan Gerakan" . jika kurang, anda bisa mencarinya sendiri.
1. Mengaktifkan/matikan Flashlight dengan menekan tombol power 2x
Menu ini berada pada "Pintasan Gerakan"
- double_click_power_key turn_on_torch

2. Gesture bawah Screenshoot tiga jari
- three_gesture_down screen_shot

3. Gesture tiga jari tekan lama
- three_gesture_long_press partial_screen_shot
