window.addEventListener("load", () => {
    clock();
    function clock() {
        const today = new Date();

        // get time components
        const hours = today.getHours();
        const minutes = today.getMinutes();
        const seconds = today.getSeconds();

        // add '0' to hour, minute, and second when fewer than 2 digits
        const hour = hours < 10 ? "0" + hours : hours;
        const minute = minutes < 10 ? "0" + minutes : minutes;
        const second = seconds < 10 ? "0" + seconds : seconds;

        // get date components
        const month = today.getMonth();
        const year = today.getFullYear();
        const day = today.getDate();

        // creating a list of the names of months
        const monthList = [
            "January",
            "February",
            "March",
            "April",
            "May",
            "June",
            "July",
            "August",
            "September",
            "October",
            "November",
            "December"
        ]
        // construct current date and time strings
        const date = monthList[month] + " " + day + "," + year;
        const time = hour + ":" + minute + ":" + second;

        // combine into one string
        const dateTime = date + " " + time;

        // print current dateTime to the DOM
        document.getElementById("date-time").innerHTML = dateTime;
        setTimeout(clock, 1000);
    }
});