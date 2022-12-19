import shutil
import os



def ignore_client():
    print('\n***********************************\nTrabalhando em clients...\n***********************************')
    for client in clients:
        # print(client)
        if 'CL' not in ''.join(list(client)[0:2]):
            clients.remove(client)
            print(client+' ignorado')
    print("'clients' pronto para a operação!")

def clean_years():
    print('\n***********************************\nTrabalhando em anos ('+client+')...\n***********************************')
    for j in anos:
        # print(j)
        if '.' in str(j):
            anos.remove(j)
            print(j+' ignorado')
    for j in anos:
        try:
            int(j)
            break
        except ValueError:
            anos.remove(j)
            print(j+' ignorado')
    print("'anos' pronto para a operação! ("+client+")")

def zipping_years():
    for j in anos:
        
        print('***********************************\nTrabalhando com '+j+'\n***********************************')
        directoryj = directory+"/"+j

        if int(j) < 2022:
            shutil.make_archive(directoryj, 'zip', directoryj)
            print('Ano de '+j+' zipado!')

            print('Excluindo '+j+' ...')
            try:
                shutil.rmtree(directoryj) # remover pastas vazias
                # os.remove(directoryj) # remover arquivo
                print('Pasta '+j+' excluída com sucesso!')
            except OSError as error:
                print('Erro ao remover pastas: \n'+error)

def clean_months():
    print('\n***********************************\nTrabalhando em meses...\n***********************************')
    for i in meses:
        # print(i.split(",")[0])
        try:
            int(i.split(".")[0]+i.split(".")[-1])
        except ValueError:
            meses.remove(i)
            print(i+' ignorado')
    print("'meses' pronto para a operação! ("+client+")")



directory_master = "G:/Drives compartilhados/3.2. Fechamento Fiscal"


clients = os.listdir(directory_master)
ignore_client()
ignore_client()
clients.sort()
total_clients = str(len(clients))
print('\nClientes detectados: '+total_clients)
print(clients)
print('\n***********************************\nIniciando...\n***********************************')

for client in clients:
    client_index = str(int(clients.index(client))+1)
    print("*********************************** Cliente "+client_index+" de "+total_clients+" ***********************************\n\nPreparando para zipar notas em '"+client+"' ...")
    directory = directory_master+"/"+client

    print('\nCriando os arquivos .zip das pastas...')

    anos = os.listdir(directory)
    # print(anos)
    clean_years()
    clean_years()
    clean_years()
    # print(anos)

    zipping_years()
    anos = os.listdir(directory)
    clean_years()
    clean_years()
    clean_years()
    anos.sort()
    zipping_years()
    print(anos)

    for j in anos:

        directoryj = directory+"/"+j
        
        meses = os.listdir(directoryj)
        meses.sort()
        clean_months()
        clean_months()
        clean_months()
        print(meses)

        for i in meses:
            directoryi = directoryj+"/"+i+"/"
            folder = "11.Notas"
            path = os.path.join(directoryi, folder)

            if os.path.exists(path+'.zip'):
                print('Arquivo '+i+"/"+folder+'.zip já existe!')
            else:
                shutil.make_archive(path, 'zip', path)
                print('Arquivo '+i+"/"+folder+'.zip criado!')
        
            print('Removendo '+path+' ...')
            try:
                os.rmdir(path) # remover pastas vazias
                # os.remove(path) # remover arquivo
                print('Excluído com sucesso: '+path)
            except OSError as error:
                try:
                    shutil.rmtree(path) # remover pastas com arquivos
                    print('Excluído com sucesso: '+path)
                except:
                    print('Pasta não encontrada: '+path)
            else:
                print('Erro ao excluir pastas: /n'+error)

    print('\n***********************************\nTodos os arquivos .zip de '+client+' foram criados!\n')
print('\n***********************************\nTodos os clientes de '+directory_master+' foram trabalhados!\n***********************************\n')