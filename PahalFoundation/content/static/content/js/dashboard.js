// Toggle visibility for general menus
function toggleVisibility(menuId) {
    var menu = document.getElementById(menuId);
    menu.style.display = menu.style.display === "block" ? "none" : "block";
}

// status change animation
document.addEventListener("change", (e) => {
    if (e.target.classList.contains("status-select")) {
        e.target.classList.add("status-changed");
        setTimeout(() => {
            e.target.classList.remove("status-changed");
        }, 300);
    }
});

function toggleMenu(id) {
    document.getElementById(id).classList.toggle("show");
}

document.getElementById('toggle-menu').addEventListener('click', function() {
    var sideMenu = document.getElementById('side-menu');
    var dashboardRight = document.getElementById('dashboard-right');
    sideMenu.classList.toggle('show');
    dashboardRight.classList.toggle('menu-open');
});
