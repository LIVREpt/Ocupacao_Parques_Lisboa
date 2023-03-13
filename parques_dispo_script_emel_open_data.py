# Parques de Estacionamento - Extrair disponibilidade 
  
## EMEL OPEN DATA

import requests
from requests.structures import CaseInsensitiveDict
import pandas as pd
from datetime import datetime, timedelta
import time

# Obter dados do emel open data: https://emel.city-platform.com/opendata/

url = "https://emel.city-platform.com/opendata/parking/lots"

headers = CaseInsensitiveDict()
headers["accept"] = "application/json"
headers["api_key"] = "f90859a793cda8a701dd7c25adf5ae2c"


resp = requests.get(url, headers=headers)

#print(resp.status_code)

json = resp.json()
df = pd.json_normalize(json)

# Passar para date e criar coluna datetime
df['data_ocupacao'] = pd.to_datetime(df['data_ocupacao'], format='%Y-%m-%dT%H:%M:%S')
df['data_ocupacao_hora'] = df['data_ocupacao'].dt.hour
df['data_ocupacao_data'] = df['data_ocupacao'].dt.date


# Exportar
from datetime import datetime
df.to_csv((datetime.now()+timedelta(hours=1)).strftime('data_sources/data_transformed/parques_estacionamento_emel_opendata-%Y-%m-%d-%H-%M-%S.csv'), encoding='utf8', index=False)
