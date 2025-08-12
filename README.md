Script para Deletar Executáveis Específicos no Windows

Este script em **Python** foi criado para remover automaticamente arquivos executáveis específicos de uma pasta no Windows.  
Ele pode ser útil para manutenção de sistemas, limpeza de arquivos antigos ou remoção de programas indesejados.

Funcionalidades
- Localiza arquivos específicos dentro de um diretório.
- Remove arquivos se encontrados.
- Exibe mensagens de status (`OK`, `ERRO`, `INFO`).
- Aguarda alguns segundos antes da execução para garantir que o sistema carregou.

Tecnologias Utilizadas
- **Python 3.10.11**
- Bibliotecas padrão: `os`, `time`

Obs.: O arquivo `.bat` utiliza o **pythonw.exe** para executar o script Python em segundo plano, sem abrir a tela preta do terminal.
