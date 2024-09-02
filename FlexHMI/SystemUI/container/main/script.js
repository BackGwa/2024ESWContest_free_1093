let content_area;
let button;
let keypad;
let keypad_target;

window.onload = () => {
    time_label = document.querySelector("time-label");
    button = document.querySelectorAll("label-button");
    content_area = document.querySelector("content-area");
    keypad = document.querySelector("user-keypad");
    register_time();
    event_register();
}

function event_register() {
    inputs = document.querySelectorAll("input");
    inputs.forEach(i => {
        i.onblur = (e) => {
            console.log(e);
            hiddenKeypad(e.explicitOriginalTarget);
        };
        
        i.onfocus = (e) => {
            rect = e.target.getBoundingClientRect();
            coord = [parseInt(rect.x + (e.target.clientWidth / 2)), parseInt(rect.y)];
            showKeypad(coord)
            keypad_target = i;
        };
    });
}

function tab_switch(id, button_element) {
    if (!button_element.classList.contains("focus")) {
        clear_class(content_area);
        clear_focus(button);
        content_area.classList.add(`tab${id}`);
        button_element.classList.add("focus");
        play_animation(content_area, "tab-switch-animation", 400);
    }
}

function clear_focus(element) {
    element.forEach(i => {
        i.classList.remove("focus");
    });
}

function clear_class(element) {
    element.classList.forEach(i => {
        element.classList.remove(i);
    });
}

function play_animation(element, animation_name, time) {
    element.classList.add(animation_name);
    setTimeout(() => {
        element.classList.remove(animation_name);
    }, time);
}

function reload() {
    parent.location.href = "../../../Core/index.html";
}

function callKeypad(title, value, ip_mode = true) {
    document.querySelector("input-text-area").classList.forEach(i => {
        document.querySelector("input-text-area").classList.remove(i);
    });

    document.querySelector("dialog-title").innerText = title;

    if (ip_mode) {
        document.querySelector("input-text-area").classList.add("mode-ip");
        document.querySelector("placeholder-label").innerText = "IPv4 주소";

        ip = value.split(".");

        ip1 = document.querySelector("#ipaddr-1");
        ip2 = document.querySelector("#ipaddr-2");
        ip3 = document.querySelector("#ipaddr-3");
        ip4 = document.querySelector("#ipaddr-4");

        ip1.value = ip[0];
        ip2.value = ip[1];
        ip3.value = ip[2];
        ip4.value = ip[3];

        keypad_area = document.querySelector("keypad-area");
        keypad_area.classList.add("keypad-show");

        return new Promise ((resolve) => {
            document.querySelector("confirm-button").onclick = () => {
                keypad_area.classList.remove("keypad-show");
                hiddenKeypad("{CONFIRM}");
                resolve(`${ip1.value}.${ip2.value}.${ip3.value}.${ip4.value}`);
            };

            document.querySelector("cancel-button").onclick = () => {
                keypad_area.classList.remove("keypad-show");
                hiddenKeypad("{CONFIRM}");
                resolve(value);
            }
        });
    } else {
        document.querySelector("input-text-area").classList.add("mode-port");
        document.querySelector("placeholder-label").innerText = "포트 번호";

        port = document.querySelector("#port-addr");
        port.value = value;

        keypad_area = document.querySelector("keypad-area");
        keypad_area.classList.add("keypad-show");

        return new Promise ((resolve) => {
            document.querySelector("confirm-button").onclick = () => {
                keypad_area.classList.remove("keypad-show");
                hiddenKeypad("{CONFIRM}");
                resolve(port.value);
            };

            document.querySelector("cancel-button").onclick = () => {
                keypad_area.classList.remove("keypad-show");
                hiddenKeypad("{CONFIRM}");
                resolve(value);
            }
        });
    }
}

function showKeypad(coord) {
    x = coord[0];
    y = coord[1] + 54;

    keypad.classList.add("keypad-enable");
    keypad.style.left = x + "px";
    keypad.style.top = y + "px";
}

function hiddenKeypad(target) {
    if (target == "{CONFIRM}" || target.offsetParent.localName != "user-keypad") {
        keypad.classList.remove("keypad-enable");
    }
}

function key_event(key) {
    switch (key) {
        case "enter":
            hiddenKeypad("{CONFIRM}");
            break;
        case "backspace":
            if (keypad_target.value.length > 0) {
                keypad_target.value = keypad_target.value.substr(0, keypad_target.value.length - 1);
            }
            break;
        default:
            keypad_target.value += key;
    }
}