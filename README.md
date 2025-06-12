# API Klasifikasi Penyakit Mental Berbasis TensorFlow

Proyek ini menyediakan API FastAPI untuk mengklasifikasikan kondisi penyakit mental berdasarkan 17 fitur numerik input. API ini menggunakan model *deep learning* yang dilatih dengan TensorFlow dan *scaler* scikit-learn untuk pra-pemrosesan data input.

## Daftar Isi

- [Gambaran Umum Proyek](#gambaran-umum-proyek)
- [Fitur Utama](#fitur-utama)
- [Model dan Skala](#model-dan-skala)
- [Struktur Proyek](#struktur-proyek)
- [Instalasi dan Penggunaan](#instalasi-dan-penggunaan)
- [Endpoints API](#endpoints-api)
- [Dependensi](#dependensi)

## Gambaran Umum Proyek

API ini dirancang untuk memprediksi salah satu dari empat label kondisi mental ("Normal", "Depression", "Bipolar Type-1", "Bipolar Type-2") berdasarkan serangkaian 17 fitur numerik. Ini berfungsi sebagai *backend* untuk aplikasi *screening* atau diagnostik, memberikan prediksi dengan tingkat kepercayaan.

## Fitur Utama

* **API Prediksi**: Menyediakan *endpoint* `/predict` untuk menerima 17 fitur numerik dan mengembalikan klasifikasi kondisi mental.
* **Model TensorFlow**: Menggunakan model *deep learning* yang disimpan dalam format `.h5` untuk inferensi.
* **Scaler Scikit-learn**: Menggunakan `StandardScaler` yang telah dilatih (`scaler.save`) untuk menormalisasi fitur input sebelum diberikan ke model.
* **Penanganan Kesalahan**: Memvalidasi jumlah fitur input dan memberikan pesan kesalahan yang sesuai jika tidak valid.
* **Tingkat Kepercayaan**: Mengembalikan tingkat kepercayaan prediksi.

## Model dan Skala

API ini bergantung pada dua file pra-terlatih:

1.  **`best_model_tf.h5`**: Ini adalah file model TensorFlow/Keras yang telah dilatih untuk tugas klasifikasi. Model ini mengharapkan input fitur yang telah diskalakan.
2.  **`scaler.save`**: Ini adalah objek `StandardScaler` dari scikit-learn, disimpan menggunakan `joblib`. *Scaler* ini digunakan untuk mengubah fitur input mentah menjadi skala yang sama dengan yang digunakan selama pelatihan model.

**Penting:** Kedua file ini harus ada di direktori *root* proyek Anda (atau di jalur yang dapat diakses) saat aplikasi dijalankan. Jika tidak ditemukan, API akan menimbulkan `RuntimeError`.

## Struktur Proyek

```
.
├── main.py
├── requirements.txt
├── README.md           # File ini.
└── best_model_tf.h5    # Model TensorFlow yang telah dilatih.
└── scaler.save         # Scaler scikit-learn yang telah dilatih.
```

## Instalasi dan Penggunaan

Untuk menjalankan API ini secara lokal di komputer Anda:

1.  **Kloning repositori:**
    ```bash
    git clone <URL_REPOSITORI_ANDA>
    cd <nama_folder_repositori>
    ```

2.  **Tempatkan file model:**
    Pastikan `best_model_tf.h5` dan `scaler.save` berada di direktori *root* proyek Anda.

3.  **Buat dan aktifkan lingkungan virtual (disarankan):**
    ```bash
    python -m venv venv
    # Di Windows
    .\venv\Scripts\activate
    # Di macOS/Linux
    source venv/bin/activate
    ```

4.  **Instal dependensi:**
    ```bash
    pip install -r requirements.txt
    ```

5.  **Jalankan aplikasi FastAPI:**
    ```bash
    uvicorn main:app --reload
    ```

    API akan berjalan di `http://127.0.0.1:8000`. Anda dapat mengakses dokumentasi API interaktif di `http://127.0.0.1:8000/docs` atau `http://127.0.0.1:8000/redoc`.

## Endpoints API

### `POST /predict`

Melakukan prediksi kondisi penyakit mental berdasarkan 17 fitur numerik yang diberikan.

**Body Permintaan (JSON):**

```json
{
  "features": [
    0.5, 0.2, 0.8, 0.1, 0.9, 0.3, 0.7, 0.0, 0.6, 0.4,
    0.2, 0.9, 0.5, 0.7, 0.1, 0.3, 0.8
  ]
}
```

* `features`: (list of float, **wajib**) Daftar yang berisi tepat 17 nilai numerik (float) yang merepresentasikan fitur input.

**Contoh Respons (JSON):**

```json
{
  "kondisi": "Depression",
  "confidence": 0.9876
}
```

* `kondisi`: (string) Label kondisi mental yang diprediksi ("Normal", "Depression", "Bipolar Type-1", atau "Bipolar Type-2").
* `confidence`: (float) Tingkat kepercayaan model terhadap prediksi tersebut, dibulatkan hingga 4 angka di belakang koma.

**Respons Kesalahan:**

* **Status Code 400 Bad Request**: Jika jumlah fitur dalam input tidak sama dengan 17.
    ```json
    {
      "detail": "Harus 17 angka."
    }
    ```

## Dependensi

Proyek ini membutuhkan pustaka Python berikut, yang dapat ditemukan di `requirements.txt`:

* `fastapi`
* `uvicorn`
* `tensorflow`
* `scikit-learn`
* `joblib`
* `numpy`
