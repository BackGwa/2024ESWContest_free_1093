let processing_server_ip;
let plc_server_ip;
let ws_port;
let tcp_port;

window.onload = () => {
    agent = navigator.userAgent;
    document.querySelector("hardware-info").innerText = agent;

    processing_server_ip = document.querySelector("#serverIP");
    plc_server_ip = document.querySelector("#plcIP");
    ws_port = document.querySelector("#websocketPORT");
    tcp_port = document.querySelector("#tcpPORT");
    get_setting();
}

function software_reboot() {
    parent.reload();
}

async function serverIP() {
    value = await parent.callKeypad("MQTT 서버 주소", getCookie("processing_server"));
    setCookie("processing_server", value, 365);
    get_setting();
}

async function plcIP() {
    value = await parent.callKeypad("PLC 주소", getCookie("plc_server"));
    setCookie("plc_server", value, 365);
    get_setting();
}

async function websocketPORT() {
    value = await parent.callKeypad("MQTT WebSocket 포트", getCookie("ws_port"), false);
    setCookie("ws_port", value, 365);
    get_setting();
}

function get_setting() {
    if (value = getCookie("processing_server")) {
        processing_server_ip.querySelector("item-value").innerText = value;
    } else {
        setCookie("processing_server", "127.0.0.1", 365);
        get_setting();
    }

    if (value = getCookie("plc_server")) {
        plc_server_ip.querySelector("item-value").innerText = value;
    } else {
        setCookie("plc_server", "192.168.48.1", 365);
        get_setting();
    }

    if (value = getCookie("ws_port")) {
        ws_port.querySelector("item-value").innerText = value;
    } else {
        setCookie("ws_port", "1217", 365);
        get_setting();
    }
}

function return_mqtt() {
    ip = getCookie("processing_server");
    port = getCookie("ws_port");
    return [ip, port];
}

function mqttTest(query) {
    value = query.querySelector("item-value");
    value.innerText = "3초 뒤 연결";

    get_mqtt = return_mqtt();
    HOST = get_mqtt[0];
    PORT = parseInt(get_mqtt[1]);

    setTimeout(() => {
        try {
            value.innerText = "통신 시도 중";

            mqtt = new Paho.MQTT.Client(HOST, PORT, `flexflow-client`);

            options = {
                timeout: 3,
                onSuccess: () => {
                    value.innerText = "통신 성공";
                },
                onFailure: () => {
                    value.innerText = "통신 장애";
                },
            }

            mqtt.connect(options);
        } catch (e) {
            value.innerText = `통신 오류 : ${e}`;
        }
    }, 3000)
}