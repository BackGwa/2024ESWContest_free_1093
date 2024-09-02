function setCookie(key, value, expiredDays) {
    let today = new Date();
    today.setDate(today.getDate() + expiredDays);
    document.cookie =
        key + '=' + JSON.stringify(value) +
        '; path=/; expires=' + today.toGMTString() + ';';
}

function getCookie(key) {
    const cookies = document.cookie.split(`; `).map((el) => el.split('='));
    let getItem = [];

    for (let i = 0; i < cookies.length; i++) {
        if (cookies[i][0] === key) {
            getItem.push(cookies[i][1]);
            break;
        }
    }

    if (getItem.length > 0) {
        try {
            return JSON.parse(getItem[0]);
        } catch {
            return "";
        }
    }
}
