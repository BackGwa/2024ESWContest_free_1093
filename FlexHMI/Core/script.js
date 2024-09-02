let init_screen;
let iframe;

function init() {
    init_screen = document.querySelector('init-screen');
    iframe = document.querySelector('iframe');
    event_register();
    change_source("../SystemUI/container/main/index.html");
}

function event_register() {
    iframe.onload = () => {
        page_onload();
    };
}

function change_source(url) {
    page_loading();
    iframe.src = url;
}

function page_loading() {
    init_screen.classList.add('show-load');
}

function page_onload() {
    setTimeout(() => {
        init_screen.classList.remove('show-load');
    }, 1000);
}