import requests
import json

# API'nizin temel adresini buraya girin.
# API'niz kendi bilgisayarınızda (localhost) çalışıyorsa:
# api_base_url = "http://127.0.0.1:8001"
# API'niz başka bir bilgisayarda (yerel ağda) çalışıyorsa, o bilgisayarın IP adresini kullanın:
api_base_url = "http://127.0.0.1:9005" # Lütfen bu satırı kendi senaryonuza göre güncelleyin!
                                      

# Mevcut GET, POST, PUT fonksiyonları burada kalacak
# (get_records, insert_record, update_record)

def get_records(limit=10):
    """API'den kayıtları çeker."""
    url = f"{api_base_url}/records/?limit={limit}"
    print(f"\nGET isteği gönderiliyor: {url}")
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        print("GET yanıtı:", json.dumps(data, indent=2))
        return data
    except requests.exceptions.RequestException as e:
        print(f"GET isteği hatası: {e}")
        if hasattr(e, 'response') and e.response is not None:
            print(f"Yanıt gövdesi: {e.response.text}")
        return None

def insert_record(record_data):
    """API'ye yeni bir kayıt ekler."""
    url = f"{api_base_url}/records/"
    print(f"\nPOST isteği gönderiliyor: {url} ile veri: {record_data}")
    try:
        response = requests.post(url, json=record_data)
        response.raise_for_status()
        data = response.json()
        print("POST yanıtı:", json.dumps(data, indent=2))
        return data
    except requests.exceptions.RequestException as e:
        print(f"POST isteği hatası: {e}")
        if hasattr(e, 'response') and e.response is not None:
            print(f"Yanıt gövdesi: {e.response.text}")
        return None

def update_record(record_id, record_data):
    """API'deki mevcut bir kaydı günceller."""
    url = f"{api_base_url}/records/{record_id}"
    print(f"\nPUT isteği gönderiliyor: {url} ile veri: {record_data}")
    try:
        response = requests.put(url, json=record_data)
        response.raise_for_status()
        data = response.json()
        print("PUT yanıtı:", json.dumps(data, indent=2))
        return data
    except requests.exceptions.RequestException as e:
        print(f"PUT isteği hatası: {e}")
        if hasattr(e, 'response') and e.response is not None:
            print(f"Yanıt gövdesi: {e.response.text}")
        return None


# YENİ İSTEMCİ FONKSİYONLARI
def set_param_tcu_client(record_id, param_name, param_value):
    """
    API'deki set_param_tcu fonksiyonunu çağırır.
    """
    url = f"{api_base_url}/records/{record_id}/param"
    payload = {"param_name": param_name, "param_value": param_value}
    print(f"\nPUT isteği (set_param_tcu) gönderiliyor: {url} ile veri: {payload}")
    try:
        response = requests.put(url, json=payload)
        response.raise_for_status() # 200 OK olmayan durumlar için hata fırlat
        data = response.json()
        print("set_param_tcu yanıtı:", json.dumps(data, indent=2))
        return data.get("success", False) # success alanını dön, yoksa False
    except requests.exceptions.RequestException as e:
        print(f"set_param_tcu isteği hatası: {e}")
        if hasattr(e, 'response') and e.response is not None:
            print(f"Yanıt kodu: {e.response.status_code}")
            print(f"Yanıt gövdesi: {e.response.text}")
        return False

def get_param_tcu_client(record_id, param_name):
    """
    API'deki get_param_tcu fonksiyonunu çağırır.
    """
    url = f"{api_base_url}/records/{record_id}/param/{param_name}"
    print(f"\nGET isteği (get_param_tcu) gönderiliyor: {url}")
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        print("get_param_tcu yanıtı:", json.dumps(data, indent=2))
        return data
    except requests.exceptions.RequestException as e:
        print(f"get_param_tcu isteği hatası: {e}")
        if hasattr(e, 'response') and e.response is not None:
            print(f"Yanıt kodu: {e.response.status_code}")
            print(f"Yanıt gövdesi: {e.response.text}")
        return None

if __name__ == "__main__":
    print("--- API Fonksiyon Çağrıları Başlıyor ---")

    # Önce bir kayıt ekleyelim ki üzerinde işlem yapabilelim
    print("\n>>> Yeni kayıt ekleme (test için):")
    initial_data = {
        "bit_rate": 10.0,
        "op_mode": 0,
        "tctone_f1_hz": 100.0
    }
    insert_response = insert_record(initial_data)
    test_record_id = None
    if insert_response and "id" in insert_response:
        test_record_id = insert_response["id"]
        print(f"Test için eklenen kaydın ID'si: {test_record_id}")
    else:
        print("Test kaydı eklenemedi, yeni fonksiyonlar test edilemeyecek.")
        # Burada isterseniz veritabanında zaten kayıt varsa onu kullanma mantığı ekleyebilirsiniz.
        # Örneğin: test_record_id = 1
        exit() # Test kaydı olmadan devam etme

    # set_param_tcu fonksiyonunu test etme
    if test_record_id:
        print(f"\n>>> set_param_tcu ile 'bit_rate' değerini güncelleme (ID: {test_record_id}):")
        success = set_param_tcu_client(test_record_id, "bit_rate", 101.0)
        print(f"set_param_tcu başarılı mı?: {success}")

        print(f"\n>>> set_param_tcu ile 'op_mode' değerini güncelleme (ID: {test_record_id}):")
        success = set_param_tcu_client(test_record_id, "op_mode", 2)
        print(f"set_param_tcu başarılı mı?: {success}")

        # Geçersiz bir parametre adı denemesi
        print(f"\n>>> set_param_tcu ile geçersiz bir parametre denemesi (ID: {test_record_id}):")
        success = set_param_tcu_client(test_record_id, "invalid_param", "some_value")
        print(f"set_param_tcu başarılı mı?: {success}") # Beklenen: False veya hata mesajı

        # Yanlış tipte değer denemesi (örn: float beklerken string gönderme)
        print(f"\n>>> set_param_tcu ile yanlış tipte değer denemesi (ID: {test_record_id}):")
        success = set_param_tcu_client(test_record_id, "bit_rate", "not_a_number")
        print(f"set_param_tcu başarılı mı?: {success}") # Beklenen: False veya hata mesajı

    # get_param_tcu fonksiyonunu test etme
    if test_record_id:
        print(f"\n>>> get_param_tcu ile 'bit_rate' değerini çekme (ID: {test_record_id}):")
        response_data = get_param_tcu_client(test_record_id, "bit_rate")
        if response_data:
            print(f"Çekilen 'bit_rate' değeri: {response_data.get('value')}")
            print(f"Kolon Haritalaması (Column Mapping): {json.dumps(response_data.get('column_mapping'), indent=2)}")

        print(f"\n>>> get_param_tcu ile 'op_mode' değerini çekme (ID: {test_record_id}):")
        response_data = get_param_tcu_client(test_record_id, "op_mode")
        if response_data:
            print(f"Çekilen 'op_mode' değeri: {response_data.get('value')}")

        # Geçersiz bir parametre adı denemesi
        print(f"\n>>> get_param_tcu ile geçersiz bir parametre denemesi (ID: {test_record_id}):")
        response_data = get_param_tcu_client(test_record_id, "non_existent_param")
        if response_data:
            print(f"Çekilen değer: {response_data.get('value')}") # Beklenen: None veya hata mesajı

        # Olmayan bir kayıt ID'si ile deneme
        print(f"\n>>> get_param_tcu ile olmayan bir kayıt ID'si denemesi:")
        response_data = get_param_tcu_client(99999, "bit_rate") # Genellikle bulunmayan bir ID
        if response_data:
            print(f"Çekilen değer: {response_data.get('value')}") # Beklenen: None veya hata mesajı


    print("\n--- API Fonksiyon Çağrıları Tamamlandı ---")

