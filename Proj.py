import os
import zipfile

def descompactar_arquivos_zip(pasta):
    arquivos = os.listdir(pasta)
    
    for arquivo in arquivos:
        caminho_arquivo = os.path.join(pasta, arquivo)
        
        if zipfile.is_zipfile(caminho_arquivo):
            print(f'Descompactando {caminho_arquivo}...')
            
            with zipfile.ZipFile(caminho_arquivo, 'r') as zip_ref:
                zip_ref.extractall(pasta)
            
            print('Descompactação concluída.')
        else:
            print(f'O arquivo {caminho_arquivo} não é um arquivo ZIP.')

def main():
    pasta_alvo = input('Digite o caminho da pasta: ')
    
    if os.path.isdir(pasta_alvo):
        descompactar_arquivos_zip(pasta_alvo)
    else:
        print('O caminho da pasta é inválido.')

if __name__ == "__main__":
    main()
