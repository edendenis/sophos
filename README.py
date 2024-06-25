#!/usr/bin/env python
# coding: utf-8

# # Como configurar/instalar o `Sophos Antivírus` no Linux Ubuntu
# 
# ## Resumo
# 
# Neste documento estão contidos os principais comandos e configurações para configurar/instalar o `Sophos Antivírus` no Linux Ubuntu.
# 
# ## _Abstract_
# 
# _In this document are contained the main commands and settings to set up/install the `Sophos Antivírus` on Linux Ubuntu._

# ## Descrição [2]
# 
# ### `Sophos Antivírus`
# 
# O `Sophos Antivírus` é uma parte fundamental das soluções de segurança cibernética da `Sophos`, projetado para proteger computadores e redes contra ameaças de malware. Reconhecido por sua eficácia na detecção e prevenção de vírus, ransomware, trojans e outras formas de software malicioso, o `Sophos Antivírus` utiliza tecnologias avançadas, incluindo aprendizado de máquina e análise de comportamento, para identificar e neutralizar ameaças em tempo real. Ele oferece recursos de varredura em tempo real, atualizações automáticas de definições de vírus e um conjunto de ferramentas de gerenciamento centralizado, tornando-o uma escolha confiável para empresas que buscam proteger seus sistemas e dados contra ataques cibernéticos. O `Sophos Antivírus` também está disponível para uso pessoal, fornecendo uma camada adicional de segurança para computadores pessoais e dispositivos.

# ## 1. Como configurar/instalar o `Sophos Antivírus` no `Linux Ubuntu` [1]
# 
# Para instalar o `Sophos Antivírus` no `Linux Ubuntu`, você pode seguir estes passos:
# 
# 1. Abra o `Terminal Emulator`. Você pode fazer isso pressionando: `Ctrl + Alt + T`
# 

# 2. Certifique-se de que seu sistema esteja limpo e atualizado.
# 
#     2.1 Limpar o `cache` do gerenciador de pacotes `apt`. Especificamente, ele remove todos os arquivos de pacotes (`.deb`) baixados pelo `apt` e armazenados em `/var/cache/apt/archives/`. Digite o seguinte comando: `sudo apt clean` 
#     
#     2.2 Remover pacotes `.deb` antigos ou duplicados do cache local. É útil para liberar espaço, pois remove apenas os pacotes que não podem mais ser baixados (ou seja, versões antigas de pacotes que foram atualizados). Digite o seguinte comando: `sudo apt autoclean`
# 
#     2.3 Remover pacotes que foram automaticamente instalados para satisfazer as dependências de outros pacotes e que não são mais necessários. Digite o seguinte comando: `sudo apt autoremove -y`
# 
#     2.4 Buscar as atualizações disponíveis para os pacotes que estão instalados em seu sistema. Digite o seguinte comando e pressione `Enter`: `sudo apt update`
# 
#     2.5 **Corrigir pacotes quebrados**: Isso atualizará a lista de pacotes disponíveis e tentará corrigir pacotes quebrados ou com dependências ausentes: `sudo apt --fix-broken install`
# 
#     2.6 Limpar o `cache` do gerenciador de pacotes `apt`. Especificamente, ele remove todos os arquivos de pacotes (`.deb`) baixados pelo `apt` e armazenados em `/var/cache/apt/archives/`. Digite o seguinte comando: `sudo apt clean` 
#     
#     2.7 Para ver a lista de pacotes a serem atualizados, digite o seguinte comando e pressione `Enter`:  `sudo apt list --upgradable`
# 
#     2.8 Realmente atualizar os pacotes instalados para as suas versões mais recentes, com base na última vez que você executou `sudo apt update`. Digite o seguinte comando e pressione `Enter`: `sudo apt full-upgrade -y`
#     

# Para instalar o `Sophos Antivirus` no `Linux Ubuntu` via `Terminal Emulator`, você precisa seguir alguns passos um pouco mais detalhados, pois o processo envolve baixar o instalador do site da `Sophos` e executá-lo. Aqui está um guia geral sobre como fazer isso:
# 
# 1. **Baixe o Sophos Antivirus:** Primeiro, visite o site oficial da Sophos e baixe a versão mais recente do `Sophos Antivirus` para `Linux Ubuntu`. Como isso envolve aceitar os termos de licença, não é possível fazer o download diretamente via terminal. Você terá que fazer isso através de um navegador: `https://www.sophos.com/en-us/support/downloads/endpoint-client`
# 
# 2. **Mova o Arquivo Baixado para uma Pasta de Sua Escolha:** Depois de baixar, mova o arquivo para uma pasta no seu sistema `Ubuntu` onde você deseja realizar a instalação (por exemplo, sua pasta de usuário ou uma pasta específica para `~/Downloads`).
# 
# 3. **Extraia o Instalador:** Abra o terminal e navegue até a pasta onde o arquivo foi salvo. Depois, extraia o instalador com um comando como: `tar -xzvf <nome_do_arquivo>.tgz`
# 
#     Substitua <nome_do_arquivo> pelo nome real do arquivo que você baixou, por exemplo: `tar -xzvf sav-linux-9-i386.tgz`
# 
# 4. **Execute o Script de Instalação:** Após extrair, entre na pasta criada e execute o script de instalação:
# 
#     ```
#     cd <nome_da_pasta>
#     sudo ./install.sh
#     ```
# 
#     Novamente, substitua <nome_da_pasta> pelo nome real da pasta, por exemplo:
# 
#     ```
#     cd sophos-av/
#     sudo ./install.sh
#     ```
# 
# 5. **Siga as Instruções de Instalação:** O script de instalação irá iniciar. Siga as instruções na tela para concluir a instalação. Você pode precisar responder algumas perguntas sobre configurações de instalação e aceitar os termos de licença.
# 
# 6. **Verifique a Instalação e o Status do Antivírus:** Para verificar se o Sophos está instalado corretamente e funcionando, você pode usar: `sudo /opt/sophos-av/bin/savdstatus`
# 
# 7. **Atualize a Base de Dados de Vírus:** Após a instalação, é uma boa prática atualizar a base de dados de vírus do Sophos. Você pode fazer isso com um comando como: `sudo /opt/sophos-av/bin/savupdate`
# 
# 8. **Executar o `savscan`:** Digite o seguinte comando para executar uma verificação completa do sistema. Isso irá escanear todos os arquivos no diretório raiz `(/`): `sudo /opt/sophos-av/bin/savscan / > ~/arquivo_de_log_do_sophos.txt`
# 
#     Este comando pode levar algum tempo para ser concluído, dependendo do tamanho do seu sistema de arquivos.
# 
#     8.1 Para logar a saída em um arquivo, você pode redirecionar a saída para um arquivo de log: `sudo /opt/sophos-av/bin/savscan / > ~/arquivo_de_log_do_sophos.txt`
# 
# Este é um guia geral, e os passos exatos podem variar um pouco dependendo da versão específica do Sophos e do Ubuntu que você está usando. Sempre é uma boa ideia consultar a documentação oficial da Sophos para as instruções mais atualizadas.

# ### 1.1 Código completo para configurar/instalar
# 
# Para instalar o `Sophos` no Linux Ubuntu sem precisar digitar linha por linha, você pode seguir estas etapas:
# 
# 1. Abra o terminal. Você pode fazer isso pressionando: `Ctrl + Alt + T`
# 
# 2. Digite o seguinte comando e pressione `Enter`:
# 
#     ```
#     NÃO há.
#     ```
# 

# ## 2. Agendar varreduras automáticas
# 
# Para agendar uma varredura automática com o `Sophos Antivírus` no Ubuntu, você pode usar o `cron`, um agendador de tarefas do Linux. Aqui está um guia passo a passo de como fazer isso:
# 
# 1. **Abra o Crontab:** Para editar o arquivo crontab para o seu usuário, abra o terminal e digite: `crontab -e`
# 
# 2. **Escolha um Editor:**
# 
#     Se for a primeira vez que você está usando o `crontab`, ele pode pedir para você escolher um editor. Geralmente, `nano` é a opção mais fácil para iniciantes.
# 
# 3. **Adicione a Tarefa Agendada:** No editor, adicione uma linha para agendar a tarefa. O formato é: `m h dom mon dow command`
# 
#     Onde:
# 
#     - `m` é o minuto (0 a 59)
#     - `h` é a hora (0 a 23)
#     - `dom` é o dia do mês (1 a 31)
#     - `mon` é o mês (1 a 12)
#     - `dow` é o dia da semana (0 a 6, onde 0 é domingo)
# 
#     Por exemplo, para agendar uma varredura todos os dias às 13 horas, você escreveria: `0 13 * * * /opt/sophos-av/bin/savscan / -ss > /var/log/sophos-scan.log`
# 
#     Este comando executa uma varredura no diretório raiz `(/`) todos os dias às 13 horas. O parâmetro `-ss` faz com que o `savscan` funcione em modo silencioso, reportando apenas quando encontrar ameaças.
# 
# 4. **Salve e Saia:** Se você estiver usando o `nano`, você pode salvar e sair pressionando `CTRL + X`, depois `Y` para confirmar as alterações, e `Enter` para sair.
# 
# 5. **Verifique se o Agendamento foi Criado:** Para verificar se a tarefa foi agendada corretamente, você pode listar suas tarefas cron com: `crontab -l`
# 
# 6. **Configurações Adicionais:** Dependendo da sua configuração e necessidades, você pode querer redirecionar a saída do comando para um arquivo de log ou enviar por e-mail. Por exemplo: `0 13 * * * /opt/sophos-av/bin/savscan / -ss > /var/log/sophos-scan.log`
# 
# Lembre-se de substituir os caminhos e opções de acordo com a sua configuração específica e necessidades. Este é um guia básico e pode precisar de ajustes para se adequar ao seu ambiente específico.

# ## 3 Desativar o `Sophos Antivirus` [1]
# 
# Para desativar temporariamente o `Sophos Antivirus` no `Linux Ubuntu`, você geralmente precisa parar os serviços relacionados ao Sophos. Isso pode ser feito através do terminal. Aqui estão os passos básicos:
# 
# 1. **Abrir o Terminal:** Você pode abrir o terminal pressionando: `Ctrl + Alt + T`
# 
# 2. **Parar o Serviço do `Sophos Antivirus`:** O `Sophos Antivirus` no `Linux` geralmente roda como um serviço. Para pará-lo, use o comando: `sudo systemctl stop sav-protect.service`
# 
#     Este comando irá parar o serviço principal do `Sophos Antivirus`.
# 
# 3. **Parar Outros Serviços Relacionados (se necessário):** Dependendo da configuração, pode haver outros serviços Sophos em execução. Para verificar todos os serviços Sophos, use: `systemctl list-units --type=service | grep sophos`
# 
#     3.1 **Se houver outros serviços Sophos, você pode pará-los individualmente usando:** `sudo systemctl stop [nome_do_serviço]`
# 
# 4. **Verificar o Status do Serviço:** Para confirmar que os serviços foram parados, você pode verificar o status com: `sudo systemctl status sav-protect.service`
# 
#     Substitua `sav-protect.service` pelo nome de qualquer outro serviço Sophos que você deseja verificar.
# 
# 5. **Reiniciar o Serviço (Quando Necessário):** Para reiniciar o serviço Sophos Antivirus, use: `sudo systemctl start sav-protect.service`
#     
#     E faça o mesmo para quaisquer outros serviços Sophos que você tenha parado.
# 
# Lembre-se de que desativar o antivírus deixa seu sistema mais vulnerável a malwares e outras ameaças. Portanto, é aconselhável reativar o Sophos Antivirus assim que possível.

# ## 4. Desinstalar o Sophos Antivirus
# 
# Se você instalou o `Sophos Antivirus` em um sistema `Linux Ubuntu` e agora precisa desinstalá-lo usando o `Terminal`, o processo pode variar um pouco dependendo de como o `Sophos` foi instalado inicialmente. Para a maioria das instalações do `Sophos`, um script de desinstalação é fornecido. Aqui está como você pode fazer isso:
# 
# ### 4.1 Usando o Script de Desinstalação
# 
# 1. **Abra o Terminal**: Você pode abrir o Terminal pressionando: `Ctrl + Alt + T`
# 
# 2. **Navegue até o Diretório de Instalação do `Sophos`**: O `Sophos` geralmente é instalado em `/opt/sophos-av` ou em um diretório similar. Mude para este diretório usando o comando: `cd /opt/sophos-av`
# 
# 3. **Execute o Script de Desinstalação**: Dentro deste diretório, deve haver um script chamado `uninstall.sh`. Execute este script com privilégios de superusuário: `sudo ./uninstall.sh`
# 
# 4. **Siga as Instruções**: O script pode pedir confirmações adicionais. Siga as instruções na tela para proceder com a desinstalação.
# 
# ### 4.2 Caso o Script de Desinstalação Não Esteja Presente
# 
# Se por algum motivo o script de desinstalação não estiver presente ou se você enfrentar problemas com o método acima, você pode tentar contatar o suporte da `Sophos` para instruções específicas de desinstalação para a sua versão ou buscar na documentação oficial do `Sophos` por orientações adicionais.
# 
# ### 4.3 Verificação Pós-Desinstalação
# 
# 1. Após a conclusão da desinstalação, você pode querer verificar se todos os componentes do `Sophos` foram devidamente removidos. Execute os seguintes comandos para procurar por quaisquer arquivos ou serviços remanescentes relacionados ao `Sophos`:
# 
#     ```
#     sudo find / -name '*sophos*'
#     systemctl list-units --type=service | grep sophos
#     ```
# 
#     Se algum arquivo ou serviço relacionado ao `Sopho`s ainda estiver presente, você precisará removê-los manualmente ou parar os serviços usando comandos adicionais do `systemctl`.
# 
# ### 4.4 Reiniciar o Sistema
# 
# 1. Após desinstalar o Sophos e verificar a remoção de todos os seus componentes, é recomendável reiniciar o seu sistema para garantir que todas as alterações entrem em vigor: `sudo systemctl reboot`
# 
#     Este é um procedimento geral que deve funcionar para a maioria das instalações do Sophos Antivirus em sistemas Linux. No entanto, dependendo da versão específica do Sophos e de como ele foi configurado, podem existir etapas adicionais necessárias.

# ## Referências
# 
# [1] OPENAI. ***Antivírus para linux ubuntu.*** Disponível em: <https://chat.openai.com/c/0bfa681a-6952-4c86-a386-76d82f4380a1> (texto adaptado). ChatGPT. Acessado em: 28/11/2023 13:51.
# 
# [2] OPENAI. ***Vs code: editor popular.*** Disponível em: <https://chat.openai.com/c/b640a25d-f8e3-4922-8a3b-ed74a2657e42> (texto adaptado). ChatGPT. Acessado em: 28/11/2023 13:51.
