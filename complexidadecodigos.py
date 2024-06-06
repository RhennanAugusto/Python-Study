velocidade = 70
local_carro = 60

RADAR_1 = 60
LOCAL_1 = 100
RADAR_RANGE = 1

velocidade_carro_passar_radar_ = velocidade > RADAR_1
carro_passou_radar_= local_carro >= (LOCAL_1 -RADAR_RANGE) and local_carro <= (LOCAL_1 + RADAR_RANGE) and velocidade > RADAR_1
carro_multado_radar_1 = carro_passou_radar_ and velocidade_carro_passar_radar_

if velocidade_carro_passar_radar_:
    print("Velocidade do carro passou do radar 1")

if carro_multado_radar_1:
    print("carro multado em radar 1")