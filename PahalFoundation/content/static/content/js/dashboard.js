function toggleMenu(menuId) {
        var menu = document.getElementById(menuId);
        menu.style.display = menu.style.display === "block" ? "none" : "block";
    }


// Handle status change animation
    document.addEventListener("change", (e) => {
      if (e.target.classList.contains("status-select")) {
        e.target.classList.add("status-changed")
        setTimeout(() => {
          e.target.classList.remove("status-changed")
        }, 300)
      }
    })