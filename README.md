# facialRecognitionLogin
Login de Reconhecimento Facial

O sistema de reconhecimento facial é dividido em 3 partes.

* 1a Passo: 

Primeiro precisamos ter um dataset das faces da pessoa a ser reconhecida. 
Na tela de cadastro de usuário da aplicação ter uma opção que realize o uplod de imagens da face do aluno no servidor na pasta "dataset"

dataset/<<Identificar do Usuario>>: diretorio onde serão salvos as imagens

Exemplo: dataset/1_Fabiano

[ATENÇÃO]: CADA USUARIO DEVERA TER UMA PASTA COM SEU IDENTIFICADOR, PARA O LAB SALVAR COM O ID DO BANCO DE DADOS E SALVAR O PATH DO DATASET EM UMA TABELA 

--------------------------------------------------------------------------------------------------------------------------
* 2a Passo:

Agora necessário codificar as faces coletadas, ou seja, realizar o treinamento das faces gerando arquivo de "encodings" para cada usuario.

##Como executar.

$ python3 decodificador_faces.py --dataset dataset/<<Identificar do Usuario>> --encodings encodings/<<Identificar do Usuario>>/encodings.pickle --detection-method hog

encodings/<<Identificar do Usuario>>: diretorio onde será salvo o encoding do usuário

[ATENÇÃO]: MONTAR UM ARQUIVO PICLE PARA CADA ALUNO DO LAB COM O ID DELE NO NOME DE ARQUIVO E GUARDE SEU PATH EM UM BANCO DE DADOS

Exemplo: encodings/1_Fabiano

Exemplo de Execução:

python3 decodificador_faces.py --dataset dataset/1_Fabiano --encodings encodings/1_Fabiano/encodings.pickle --detection-method hog

--------------------------------------------------------------------------------------------------------------------------

3a Passo:

Reconhecimento Facial

##Como executar.

$ python3 facial_recognition_login_image.py --cascade haarcascade_frontalface_default.xml --encodings encodings/<<Identificar do Usuario>>/encodings.pickle --image <<imagem capturada no login do sistema>> --login <<Identificar do Usuario>>

Retorno Json:

{"name": "<<Identificar do Usuario>>", "loginSuccess": true}

Exemplo de Execução: 

python3 facial_recognition_login_image.py --cascade haarcascade_frontalface_default.xml --encodings encodings/1_Fabiano/encodings.pickle --image Fabiano.png --login 1_Fabiano

Retorno:
{"name": "1_Fabiano", "loginSuccess": true}
