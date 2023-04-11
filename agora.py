class Carro:
    def __init__(self, modelo, consumo, cambio, marchas, injecao,
                 amortecedores, radiador, freio_abs, turbo, vidros, cintos, airbag,
                 controle_estabilidade, sensor_fadiga, sensor_frenagem,
                 sensor_ponto_cego, camera_re, camera_3d, farol_led,
                 farol_milha, fechamento_mala, sensor_calibragem, ar_condicionado,
                 painel_digital, modo_sport, tracao_4x4, rotacao_independente,
                 torque_instantaneo, reducao_consumo):
        self.modelo = modelo
        self.consumo = consumo
        self.cambio = cambio
        self.marchas = marchas
        self.injecao = injecao
        self.amortecedores = amortecedores
        self.radiador = radiador
        self.freio_abs = freio_abs
        self.turbo = turbo
        self.vidros = vidros
        self.cintos = cintos
        self.airbag = airbag
        self.controle_estabilidade = controle_estabilidade
        self.sensor_fadiga = sensor_fadiga
        self.sensor_frenagem = sensor_frenagem
        self.sensor_ponto_cego = sensor_ponto_cego
        self.camera_re = camera_re
        self.camera_3d = camera_3d
        self.farol_led = farol_led
        self.farol_milha = farol_milha
        self.fechamento_mala = fechamento_mala
        self.sensor_calibragem = sensor_calibragem
        self.ar_condicionado = ar_condicionado
        self.painel_digital = painel_digital
        
        self.modo_sport = modo_sport
        self.tracao_4x4 = tracao_4x4
        self.rotacao_independente = rotacao_independente
        self.torque_instantaneo = torque_instantaneo
        self.reducao_consumo = reducao_consumo
 
 
if __name__ == '__main__':
    def criar() -> Carro:
        modelo = input('Insira o modelo do Carro: ')
        consumo = input('Insira o combustivel do Carro (Gasolina, Diesel, Elétrico ou Híbrido): ')
        if consumo.lower() == 'diesel':
            cambio = 'Manual'
        elif consumo.lower() == 'elétrico':
            cambio = 'Automático'
        else:
            cambio = input('Insira o tipo do cambio (manual ou automático): ')
        # Restrição
        marchas = '6 marchas'
        injecao = 'Eletrônica'
        amortecedores = 'Reforçado'
        radiador = input("Radiador tubular (Sim, Não): ")
        freio_abs = 'Sim'
        turbo = input("Turbo (Sim, Não): ")
 
        # Opções para segurança
        print("\nEscolha as opções para a segurança:")
        vidros = 'Não' if consumo.lower() == 'gasolina' else input("Vidros reforçados (Sim, Não): ")
        cintos = 'Sim'
        airbag = 'Sim'
        controle_estabilidade = 'não' if consumo.lower() == 'diesel' else input("Controle de estabilidade (Sim, Não): ")
        sensor_fadiga = input("Sensor de fadiga (Sim, Não): ")
        sensor_frenagem = input("Sensor de frenagem (Sim, Não): ")
        sensor_ponto_cego = input("Sensor de ponto cego (Sim, Não): ")
 
        # Opções para acessórios
        print("\nEscolha as opções para os acessórios:")
        camera_re = input("Câmera de ré (Sim, Não): ")
        camera_3d = input("Câmera 3D (Sim, Não): ")
        farol_led = 'Sim'
        farol_milha = 'Sim' if consumo.lower() == 'diesel' else input("Farol de milha (Sim, Não): ")
        fechamento_mala = input("Fechamento automático da mala (Sim, Não): ")
        sensor_calibragem = 'Sim' if consumo.lower() == 'elétrico' else input("Sensor de calibragem dos pneus (Sim, Não): ")
        ar_condicionado = 'Sim'
        painel_digital = 'Sim' if consumo.lower() == 'elétrico' else input("Painel digital (Sim, Não): ")
 
        # Opções para ações
        print("\nEscolha as opções para as ações:")
        modo_sport = 'Sim'
        tracao_4x4 = 'Sim' if consumo.lower() == 'diesel' else input("Tração 4x4 (Sim, Não): ")
        rotacao_independente = 'Sim' if consumo.lower() == 'diesel' else input("Rotação independente dos pneus (Sim, Não): ")
        torque_instantaneo = 'Sim' if consumo.lower() == 'elétrico' else input("Torque instantâneo (Sim, Não): ")
        reducao_consumo = input("Redução de consumo (Sim, Não): ")

        return Carro(modelo, consumo, cambio, marchas, injecao, amortecedores, radiador, freio_abs, turbo,
            vidros, cintos, airbag, controle_estabilidade, sensor_fadiga, sensor_frenagem, sensor_ponto_cego,
            camera_re, camera_3d, farol_led, farol_milha, fechamento_mala, sensor_calibragem,
            ar_condicionado, painel_digital, modo_sport, tracao_4x4, rotacao_independente, torque_instantaneo,
            reducao_consumo)
 

    carro = criar()
 
   
    print(f'\nOlá, você acabou de criar um {carro.modelo} movido a {carro.consumo}')
    print(f'Tipo de Câmbio: {carro.cambio}')
    print(f'Quantidade de marchas {carro.marchas}')
    print(f'Injeção: {carro.injecao}')
    print(f'Amortecedores: {carro.amortecedores}')
    print(f'{carro.radiador} para Radiador Tubular')
    print(f'{carro.freio_abs} para Freios ABS')
    print(f'{carro.turbo} para Turbo')
    print(f'{carro.vidros} para Vidros Reforçados')
    print(f'{carro.cintos} para Cintos de 3 pontas')
    print(f'{carro.airbag} para Airibag')
    print(f'{carro.controle_estabilidade} para controle de estabilidade')
    print(f'{carro.sensor_fadiga} para Sensor de Fadiga')
    print(f'{carro.sensor_frenagem} para Sensor de Frenagem')
    print(f'{carro.sensor_ponto_cego} para Sensor de ponto cego')
    print(f'{carro.camera_re} para câmera de ré')
    print(f'{carro.camera_3d} para câmera 3D')
    print(f'{carro.farol_led} para Farol de Led')
    print(f'{carro.farol_milha} para Farol de Milha')
    print(f'{carro.fechamento_mala} para Fechamento Automática da Mala')
    print(f'{carro.sensor_calibragem} para Sensor de Calibragem dos Pneus')
    print(f'{carro.ar_condicionado} para Ar Condicionado')
    print(f'{carro.painel_digital} para Painel Digital')
    print(f'{carro.modo_sport} para Modo Sport')
    print(f'{carro.tracao_4x4} para Tração')
    print(f'{carro.rotacao_independente} para Rotação Independente dos Pneus')
    print(f'{carro.torque_instantaneo} para Torque Instantâneo')
    print(f'{carro.reducao_consumo} para Redução de Consumo')