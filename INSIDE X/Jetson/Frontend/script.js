const TOPIC = "flexflow/asm/jetson01/#"
let mqtt;
let mqtt_broker;
let mqtt_port;

function init() {
    mqtt_broker = getCookie("processing_server");
    mqtt_port = parseInt(getCookie("ws_port"));

    mqtt = new Paho.MQTT.Client(mqtt_broker, mqtt_port, `inside-client`);

    options = {
        timeout: 5,
        onSuccess: () => { subscribe(); },
        onFailure: () => {
            console.log("MQTT 서버 연결에 문제가 생겼습니다! 설정을 다시 확인하세요!");
        },
    }

    mqtt.connect(options);
}

function subscribe() {
    mqtt.subscribe(TOPIC);
    mqtt.onMessageArrived = onMessage;
}

function onMessage(message) {
    receive_msg = message.payloadString;
    receive_topic = message.destinationName.split("/");

    if (receive_topic[3] == "MEMORY") {
        address = receive_topic[4].split("x");

        // IMAGE DATA
        if (parseInt(address[0]) == 2) {
            query = document.querySelector(`live-image`);
            query.querySelector("img").src = `data:image/jpeg;base64, ${receive_msg}`;
        }

        // COUNTER DATA
        else {
            query = document.querySelector(`M${receive_topic[4]}`);
            query.querySelector("counter-value").innerText = receive_msg;
        }
    }
}