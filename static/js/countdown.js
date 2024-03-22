var countdownInterval = setInterval(function() {
    // Get the current date and time
    var now = new Date().getTime();

    // Calculate the time remaining
    var timeRemaining = targetDate - now;

    // Calculate days, hours, minutes, and seconds
    var days = Math.floor(timeRemaining / (1000 * 60 * 60 * 24));
    var hours = Math.floor((timeRemaining % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
    var minutes = Math.floor((timeRemaining % (1000 * 60 * 60)) / (1000 * 60));
    var seconds = Math.floor((timeRemaining % (1000 * 60)) / 1000);
    
    days = padWithZero(days);
    hours = padWithZero(hours);
    minutes = padWithZero(minutes);
    seconds = padWithZero(seconds);

    // Display the countdown
    document.getElementById('countdown').innerHTML = days + ' : ' + hours + ' : ' + minutes + ' : ' + seconds;

    // If the countdown is over, stop the countdown
    if (timeRemaining < 0) {
        clearInterval(countdownInterval);
        document.getElementById('countdown').innerHTML = 'Countdown expired';
    }
}, 1000); // Update every second

function padWithZero(number) {
    return (number < 10 ? '0' : '') + number;
}