class Carro:
    def __init__(self, consumo, cambio, marchas, injecao,
                 amortecedores, radiador, freio_abs, turbo, vidros, cintos, airbag,
                 controle_estabilidade, sensor_fadiga, sensor_frenagem,
                 sensor_ponto_cego, camera_re, camera_3d, farol_led,
                 farol_milha, fechamento_mala, sensor_calibragem, ar_condicionado,
                 painel_digital, modo_sport, tracao_4x4, rotacao_independente,
                 torque_instantaneo, reducao_consumo):
        # Mecânica
        self.consumo = consumo
        self.cambio = cambio
        self.marchas = marchas
        self.injecao = injecao
        self.amortecedores = amortecedores
        self.radiador = radiador
        self.freio_abs = freio_abs
        self.turbo = turbo
        
        # Segurança
        self.vidros = vidros
        self.cintos = cintos
        self.airbag = airbag
        self.controle_estabilidade = controle_estabilidade
        self.sensor_fadiga = sensor_fadiga
        self.sensor_frenagem = sensor_frenagem

        # Acessórios
        self.sensor_ponto_cego = sensor_ponto_cego
        self.camera_re = camera_re
        self.camera_3d = camera_3d
        self.farol_led = farol_led
        self.farol_milha = farol_milha
        self.fechamento_mala = fechamento_mala
        self.sensor_calibragem = sensor_calibragem
        self.ar_condicionado = ar_condicionado
        self.painel_digital = painel_digital
        
        # Ações (métodos)
        self.modo_sport = modo_sport
        self.tracao_4x4 = tracao_4x4
        self.rotacao_independente = rotacao_independente
        self.torque_instantaneo = torque_instantaneo
        self.reducao_consumo = reducao_consumo


opcoes = {
    'consumo': ['gasolina', 'diesel', 'elétrico', 'híbrido'],
    'câmbio': ['manual', 'automatico'],
    'quantidade de marchas': ['5', '6'],
    'tipo de injeção': ['eletrônica', 'convencional'],
    'armotecedores': ['reforçados', 'comuns'],
    'radiador tubular': ['sim', 'não'],
    'freios abs': ['sim', 'não'],
    'turbo': ['sim', 'não'],
    'vidros reforçados': ['sim', 'não'],
    'cintos 3 pontas': ['sim', 'não'],
    'airbag': ['sim', 'não'],
    'controle de estabilidade': ['sim', 'não'],
    'sensor de fadiga': ['sim', 'não'],
    'sensor de frenagem': ['sim', 'não'],
    'sensor de ponto cego': ['sim', 'não'],
    'câmera de ré': ['sim', 'não'],
    'câmera 3D': ['sim', 'não'],
    'farol de LED': ['sim', 'não'],
    'farol de milha': ['sim', 'não'],
    'fechamento automático de malas': ['sim', 'não'],
    'sensor de calibragem dos pneus': ['sim', 'não'],
    'ar condicionado': ['sim', 'não'],
    'painel digital': ['sim', 'não'],
    'modo sport': ['sim', 'não'],
    'tração 4x4': ['sim', 'não'],
    'rotação independente de pneus': ['sim', 'não'],
    'torque instântaneo': ['sim', 'não'],
    'redução de consumo': ['sim', 'não']
}

if __name__ == '__main__':
    print('Monte o seu carro. Escolha as características que você deseja no seu carro:')
    respostas = []
    for index, caracteristica in enumerate(opcoes):
        opcao = input(f"{index + 1} - {caracteristica.capitalize()} ({', '.join(opcoes[caracteristica])}): ")
        while opcao.lower() not in opcoes[caracteristica]:
            print('Opção inválida!')
            opcao = input(f"{index + 1} - {caracteristica.capitalize()} ({', '.join(opcoes[caracteristica])}): ")
        respostas.append(opcao)
    print(f'\nOlá, você acabou de criar um carro com as seguintes características:')
    for index, caracteristica in enumerate(opcoes):
        print(f"{index + 1} - {caracteristica.capitalize()}: {respostas[index]}")
