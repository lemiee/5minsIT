// <⚠️ DONT DELETE THIS ⚠️>
//import "./styles.css";
const colors = ["#1abc9c", "#3498db", "#9b59b6", "#f39c12", "#e74c3c"];
// <⚠️ /DONT DELETE THIS ⚠️>
/*
✅ The text of the title should change when the mouse is on top of it.
✅ The text of the title should change when the mouse is leaves it.
✅ When the window is resized the title should change.
✅ On right click the title should also change.
✅ The colors of the title should come from a color from the colors array.
✅ DO NOT CHANGE .css, or .html files.
✅ ALL function handlers should be INSIDE of "superEventHandler"
*/
const userAction = document.querySelector("h1");
console.log(userAction);


userAction.style.color = colors[0];

const superEventHandler = {
    'handleActionMouseenter': () => {
        userAction.innerText="The mouse is here!";
        userAction.style.color = colors[1];
    },
    
    'handleActionMouseleave': () => {
        userAction.innerText="The mouse is gone!";
        userAction.style.color = colors[2];
    },
    
    'handleActionResize': ()=> {
        userAction.innerText="You just resized!";
        userAction.style.color = colors[3];
    },
    
    'handleActionContextmenu': () => {
        userAction.innerText = "That was a right click!";
        userAction.style.color = colors[4];
    },

};

userAction.onmouseenter = superEventHandler.handleActionMouseenter;
userAction.onmouseleave = superEventHandler.handleActionMouseleave;
window.onresize = superEventHandler.handleActionResize;
window.oncontextmenu= superEventHandler.handleActionContextmenu;
