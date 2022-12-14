# python 3.6

import random
import time

from paho.mqtt import client as mqtt_client


broker = 'broker.emqx.io'
port = 8083
topic = "python/mqtt"
# generate client ID with pub prefix randomly
my_client_id = f'python-mqtt-{random.randint(0, 1000)}'
# username = 'tsmmqttuser'
# password = 'ZFjN39bfg4YgCL9d'

def connect_mqtt():
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("Connected to MQTT Broker!")
        else:
            print("Failed to connect, return code %d\n", rc)
    mytransport = 'websockets' # or 'tcp'
   
    client = mqtt_client.Client(client_id = my_client_id, transport=mytransport,
                         protocol=mqtt_client.MQTTv311,
                         clean_session=True)
    print(f"Mqtt Client 1`{client}`")
    

    # client.username_pw_set(username, password)
    # client.ws_set_options(path="/mqtt", headers=None)
    # client.tls_set(ca_certs="C:\\Users\\nidhgupt\\Downloads\\broker.emqx.io-ca.crt")
    client.on_connect = on_connect
    client.connect(host=broker, port=port, keepalive=60)
    return client


def publish(client):
    msg_count = 0
        msg = f"messages: {msg_count}"
        result = client.publish(topic, msg)
        # result: [0, 1]
        status = result[0]
        if status == 0:
            print(f"Send `{msg}` to topic `{topic}`")
        else:
            print(f"Failed to send message to topic {topic}")
        msg_count += 1


def run():
    client = connect_mqtt()
    print(f"Mqtt Client `{client}`")
    client.loop_start()
    publish(client)


if __name__ == '__main__':
    run()
