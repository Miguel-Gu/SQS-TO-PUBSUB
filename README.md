# SQS-TO-PUBSUB

Modelo de Cloud [Function](https://cloud.google.com/functions/docs/concepts/overview?hl=pt-br) para receber os dados de uma Fila SQS e envia-lós para um tópico PubSub.


## Linguagem
Essa aplicação utiliza como linguagem o [Python 3.9](https://www.python.org/).


## Demais
- AWS SDK for Python [Boto3](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html) para conexão com a fila SQS.
- Python Client for Google Cloud [Pub/Sub](https://cloud.google.com/python/docs/reference/pubsub/latest) para envio das mensagens para o tópico Pub/Sub.


### Execução local
Para execução do programa localmente, instale os pacotes presentes no requirements.txt e configure as variáveis de ambiente de acordo com as informações da sua fila SQS e do seu tópico Pub/Sub.