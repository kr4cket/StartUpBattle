from rabbitmq.Rabbitmq import Rabbitmq

if __name__ == "__main__":

    print('Worker started')
    Rabbitmq().listen()
