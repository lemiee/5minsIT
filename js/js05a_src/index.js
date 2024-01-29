const windowContent = document.querySelector("body");

const handleResize = function() {
    if (window.innerWidth < 600){
        windowContent.className="shortWidth";
        console.log(window.innerWidth);
    }
    else if(600 <= window.innerWidth && window.innerWidth<800){
        windowContent.className= "midWidth";
        console.log(window.innerWidth);
    }
    else {
        windowContent.className = "wideWidth";
        console.log(window.innerWidth);
    }
}

window.onresize = handleResize;