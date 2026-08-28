# grupo FGA SISTEMAS - Gustavo rm570720 - Felipe Eloy rm 573404 - Fabricio rm573450 - Andery rm569922
# Sprint 3 - Camera App (versao console)

galeria = []
contador_id = 1

# Dicionario atualizado com os elementos da interface visual
camera = {
    "modo": "FOTO",
    "qualidade": "12MP",
    "flash": False,
    "timer": "OFF",
    "zoom": "1.0x"
}

configuracoes = {
    "grade": False,
    "modo noturno": False,
    "estabilizacao": True,
    "hdr": False,
    "som da camera": True,
    "localizacao": False
}


def ler_numero(msg):
    while True:
        valor = input(msg)
        if valor.isdigit():
            return int(valor)
        else:
            print("Digite apenas numeros, tente de novo.")


def mostrar_camera():
    # Icones do topo
    str_flash = "[⚡]" if camera["flash"] else "[⚡̸]"
    str_timer = f"⏱️ {camera['timer']}"
    
    print("\n==========================================")
    print(f" {camera['qualidade']}         {str_flash}        {str_timer}  ⚙️")
    print("------------------------------------------")
    print(" |                                       |")
    print(" |                                       |")
    print(f" |               ┌───┐            {camera['zoom']} |")
    print(" |               │   │             │     |")
    print(" |               └───┘             ●     |")
    print(" |                                       |")
    print("------------------------------------------")
    
    # Carrossel de Modos
    modos = ["RETRATO", "VÍDEO", "FOTO", "CÂMERA LENTA", "CINEMA"]
    linha_modos = "  "
    for m in modos:
        if m == camera["modo"]:
            linha_modos += f"[{m}] "  # Modo selecionado em destaque
        else:
            linha_modos += f"{m} "
    print(linha_modos)
    print("------------------------------------------")
    print("  [🖼️ Galeria]      [ ⚪ CAPTURAR ]      [🔍 Zoom]")
    print("==========================================")


def menu_principal():
    print("\nComandos Rápidos:")
    print("1 - ⚪ Tirar Foto / Gravar Vídeo")
    print("2 - ↔️ Alternar Modo (Foto, Vídeo, Retrato, etc.)")
    print("3 - ⚡ Ligar/Desligar Flash")
    print("4 - ⏱️ Ajustar Timer")
    print("5 - 🔍 Alternar Zoom (1.0x / 2.0x)")
    print("6 - 🖼️ Abrir Galeria")
    print("7 - ⚙️ Configurações")
    print("0 - 🔴 Desligar Câmera")


def trocar_modo(camera):
    print("\nEscolha o modo:")
    print("1 - RETRATO")
    print("2 - VÍDEO")
    print("3 - FOTO")
    print("4 - CÂMERA LENTA")
    print("5 - CINEMA")

    opcao = ler_numero("Opcao: ")

    if opcao == 1:
        camera["modo"] = "RETRATO"
        camera["qualidade"] = "12MP"
    elif opcao == 2:
        camera["modo"] = "VÍDEO"
        camera["qualidade"] = "4K 24FPS"
    elif opcao == 3:
        camera["modo"] = "FOTO"
        camera["qualidade"] = "12MP"
    elif opcao == 4:
        camera["modo"] = "CÂMERA LENTA"
        camera["qualidade"] = "1080P 240FPS"
    elif opcao == 5:
        camera["modo"] = "CINEMA"
        camera["qualidade"] = "4K 60FPS"
    else:
        print("Opcao invalida.")

    return camera


def alternar_flash(camera):
    camera["flash"] = not camera["flash"]
    status = "LIGADO" if camera["flash"] else "DESLIGADO"
    print(f"Flash {status}.")
    return camera


def ajustar_timer(camera):
    print("\nOpcoes de Temporizador:")
    print("1 - Desligado (OFF)")
    print("2 - 3 segundos")
    print("3 - 10 segundos")
    
    opcao = ler_numero("Opcao: ")
    if opcao == 1:
        camera["timer"] = "OFF"
    elif opcao == 2:
        camera["timer"] = "3s"
    elif opcao == 3:
        camera["timer"] = "10s"
    else:
        print("Opcao invalida.")
        
    return camera


def alternar_zoom(camera):
    # Alterna diretamente entre 1.0x e 2.0x sem menu extra
    if camera["zoom"] == "1.0x":
        camera["zoom"] = "2.0x"
    else:
        camera["zoom"] = "1.0x"
        
    print(f"Zoom alterado para: {camera['zoom']}")
    return camera


def capturar_midia(camera, galeria, contador_id):
    if camera["timer"] != "OFF":
        print(f"Aguardando temporizador de {camera['timer']}...")

    nome = input("Digite um nome para a captura (ou ENTER para padrao): ")
    if nome == "":
        nome = f"IMG_{contador_id}" if camera["modo"] in ["FOTO", "RETRATO"] else f"VID_{contador_id}"

    tipo = "foto" if camera["modo"] in ["FOTO", "RETRATO"] else "video"

    item = {
        "id": contador_id,
        "nome": nome,
        "tipo": tipo,
        "modo": camera["modo"],
        "qualidade": camera["qualidade"],
        "zoom": camera["zoom"]
    }

    galeria.append(item)
    contador_id += 1
    print(f"📸 Capturado com sucesso: {nome} [{tipo.upper()}]")

    return galeria, contador_id


def ver_galeria(galeria):
    print("\n----- 🖼️ GALERIA DE MÍDIAS -----")
    if len(galeria) == 0:
        print("A galeria esta vazia.")
    else:
        for item in galeria:
            print(f"ID: {item['id']} | Nome: {item['nome']} | Tipo: {item['tipo']} | Modo: {item['modo']} | Zoom: {item['zoom']}")
        
        print("\n1 - Apagar item")
        print("0 - Voltar")
        opcao = ler_numero("Opcao: ")
        if opcao == 1:
            apagar_item(galeria)


def apagar_item(galeria):
    id_apagar = ler_numero("Digite o ID do item que quer apagar: ")
    achou = False
    
    for i in range(len(galeria)):
        if galeria[i]["id"] == id_apagar:
            galeria.pop(i)
            achou = True
            print("Item removido.")
            break

    if not achou:
        print("ID nao encontrado.")


def tela_configuracoes(configuracoes):
    while True:
        print("\n----- ⚙️ CONFIGURAÇÕES -----")
        chaves = list(configuracoes.keys())

        for idx, chave in enumerate(chaves, 1):
            status = "LIGADO" if configuracoes[chave] else "DESLIGADO"
            print(f"{idx} - {chave.title()}: {status}")

        print(f"{len(chaves) + 1} - Voltar")
        opcao = ler_numero("Escolha uma opcao: ")

        if opcao == len(chaves) + 1:
            break
        elif 1 <= opcao <= len(chaves):
            chave_sel = chaves[opcao - 1]
            configuracoes[chave_sel] = not configuracoes[chave_sel]
        else:
            print("Opcao invalida.")


def main():
    global camera, galeria, contador_id, configuracoes

    rodando = True
    while rodando:
        mostrar_camera()
        menu_principal()
        opcao = ler_numero("Comando: ")

        if opcao == 1:
            galeria, contador_id = capturar_midia(camera, galeria, contador_id)
        elif opcao == 2:
            camera = trocar_modo(camera)
        elif opcao == 3:
            camera = alternar_flash(camera)
        elif opcao == 4:
            camera = ajustar_timer(camera)
        elif opcao == 5:
            camera = alternar_zoom(camera)
        elif opcao == 6:
            ver_galeria(galeria)
        elif opcao == 7:
            tela_configuracoes(configuracoes)
        elif opcao == 0:
            print("Desligando camera...")
            rodando = False
        else:
            print("Opcao invalida.")


main()