let time_label;

// 시간 업데이트
function time_update() {
    const today = new Date();

    hours = today.getHours();
    hours12 = hours;
    hours = (hours == 0) ? 12 : (hours > 12) ? hours - 12 : hours;
    hours = String(hours).padStart(2, '0');

    minutes = String(today.getMinutes()).padStart(2, '0');

    time_label.innerText = `${(hours12 > 12) ? "오후" : "오전"} ${hours}:${minutes}`;
}

// 시간 업데이트 이벤트 등록
function register_time() {
    setInterval(time_update, 100);
}