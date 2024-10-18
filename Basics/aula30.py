"""
Constante = "variáveis" que não vão mudar
Muitas condições no mesmo IF (RUIM)
    <- Contagem de complexidade (RUIM)
"""

velocidade = 61
local_carro = 100

RADAR_1 = 60
LOCAL_1 = 100
RADAR_RANGE = 1

vel_carro_pass_radar_1 = velocidade > RADAR_1

if vel_carro_pass_radar_1:
    print('Velocidade carro passou do radar 1')

if local_carro >= (LOCAL_1 - RADAR_RANGE) and \
        local_carro <= (LOCAL_1 + RADAR_RANGE) and \
            vel_carro_pass_radar_1:
    print('carro multado em radar 1')