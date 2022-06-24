
//navbar
const navmenu = document.getElementById('nav_menu'),
    togglemenu = document.getElementById('toggle_menu'),
    closemenu = document.getElementById('close_menu');

togglemenu.addEventListener('click', () =>{
    navmenu.classList.toggle('show')
})
closemenu.addEventListener('click', () =>{
    navmenu.classList.remove('show')
})