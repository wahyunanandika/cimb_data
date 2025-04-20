import joblib

def serialize_data(data, filename):
    """
    Menyimpan objek ke file menggunakan joblib.
    
    Parameters:
    data: objek yang akan disimpan (misalnya, model atau encoder)
    filename: nama file untuk menyimpan objek (contoh: 'model.pkl')
    """
    try:
        joblib.dump(data, filename)
        print(f"Data successfully saved to {filename}")
    except Exception as e:
        print(f"Error while saving data: {e}")

import joblib

def deserialize_data(filename):
    """
    Memuat objek dari file yang disimpan sebelumnya menggunakan joblib.
    
    Parameters:
    filename: nama file tempat objek disimpan (contoh: 'model.pkl')
    
    Returns:
    Objek yang dimuat dari file
    """
    try:
        data = joblib.load(filename)
        print(f"Data successfully loaded from {filename}")
        return data
    except Exception as e:
        print(f"Error while loading data: {e}")
        return None

