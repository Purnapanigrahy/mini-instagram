const menus = document.querySelectorAll(".menu");
const dropdowns = document.querySelectorAll(".dropdown");

menus.forEach(menu => {
    menu.addEventListener("click", (e) => {
        e.stopPropagation();

        const currentDropdown = menu.querySelector(".dropdown");

        // Close all other dropdowns
        dropdowns.forEach(dropdown => {
            if (dropdown !== currentDropdown) {
                dropdown.style.display = "none";
            }
        });

        // Toggle current dropdown
        if (currentDropdown.style.display === "block") {
            currentDropdown.style.display = "none";
        } else {
            currentDropdown.style.display = "block";
        }
    });
});

// Close dropdown when clicking anywhere else
document.addEventListener("click", () => {
    dropdowns.forEach(dropdown => {
        dropdown.style.display = "none";
    });
});