
window.onload = function() {

    document.querySelector(':root').style.setProperty('--main-color',  window.localStorage.getItem("color"));


    if(window.localStorage.getItem("theme") == "light")console.log("dark");
    else console.log("light");



    // if(window.localStorage.getItem("theme") == "dark")
    // document.querySelector("#theme-close").click();
    // else
    // document.querySelector("#theme-open").click();
// 




    



}


let themeToggler = document.querySelector('.theme-toggler');

themeToggler.onclick = () =>{

    themeToggler.classList.toggle('active');

    if(themeToggler.classList.contains('active')){
        document.body.classList.add('active');
    }else{
        document.body.classList.remove('active');
    }

}

document.querySelectorAll('.theme-colors .color').forEach(color =>{
    color.onclick = () => {
        let background = color.style.background;
        window.localStorage.setItem("color", background)
        document.querySelector(':root').style.setProperty('--main-color',  window.localStorage.getItem("color"));

    }
    

}); 

let theme = document.querySelector('.themes-container');

document.querySelector('#theme-open').onclick = () =>{
    theme.classList.add('active');
    window.localStorage.setItem("theme", "light")
    document.body.style.paddingRight = '350px';
}

document.querySelector('#theme-close').onclick = () =>{
    theme.classList.remove('active');
    window.localStorage.setItem("theme", "dark")
    document.body.style.paddingRight = '0px';
}

