// Nav link active state logic
document.addEventListener('DOMContentLoaded', () => {
    const currentLocation = location.href;
    const menuItem = document.querySelectorAll('.nav-links a');
    const menuLength = menuItem.length;
    for (let i = 0; i < menuLength; i++) {
        if (menuItem[i].href === currentLocation) {
            menuItem[i].style.color = "#ff9a9e";
            menuItem[i].style.borderBottom = "2px solid #ff9a9e";
        }
    }

    console.log("CupcakeWin site is ready!");
});