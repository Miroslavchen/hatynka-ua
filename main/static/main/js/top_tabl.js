// var top_table = document.getElementById("top");
// var content = document.getElementById("content");
// var counter = 1;
// var counterforwindow = 1;
// var windmenu = document.getElementById("menuwind");
// try {
//     var log = document.getElementById("v");
//     var reg = document.getElementById("r");
//     var add = document.getElementById("d");
// }finally {
//
// } {
//
// }
// var lastheight = 0;
//     var screenHeight = window.innerHeight;
//     if (screenHeight !== lastheight) {
//         var height = Math.trunc(screenHeight * 0.8859315589354);
//         console.log(height);
//         document.getElementById("ul").style.height = height;
//     }
//     lastheight = screenHeight;
//
//
// function check(el) {
//     counter++;
//
//     if (counter % 2 == 0){
//         top_table.style.opacity = "0";
//         if (add) {
//             add.style.opacity = "0";
//         }
//         if (log) {
//             log.style.opacity = "0";
//             reg.style.opacity = "0";
//         }
//         document.getElementById("open").style.display = 'none';
//         document.getElementById("close").style.display = "flex";
//         document.getElementById("h").style.pointerEvents = "none";
//         if (add) {
//             document.getElementById("d").style.pointerEvents = "none";
//         }
//         if (log) {
//             document.getElementById("v").style.pointerEvents = "none";
//             document.getElementById("r").style.pointerEvents = "none";
//         }
//         console.log("up");
//     } else {
//         top_table.style.opacity = '1';
//         if (add) {
//             add.style.opacity = "1";
//         }
//         if (log) {
//             log.style.opacity = "1";
//             reg.style.opacity = "1";
//         }
//         document.getElementById("close").style.display = 'none';
//         document.getElementById("open").style.display = "flex";
//         document.getElementById('d').style.display = 'flex';
//         document.getElementById("h").style.pointerEvents = "auto";
//         if (add) {
//             document.getElementById("d").style.pointerEvents = "auto";
//         }
//         if (log) {
//             document.getElementById("v").style.pointerEvents = "auto";
//             document.getElementById("r").style.pointerEvents = "auto";
//         }
//         console.log("down");
//     }
//
//     console.log("G");
// }
//
// function wind() {
//     counterforwindow++;
//
//     if (counterforwindow % 2 == 0) {
//         content.style.opacity = "0";
//         content.style.pointerEvents = "none";
//         windmenu.style.display = "flex";
//         if (add) {
//             add.style.display = "flex";
//         }
//         if (log) {
//             log.style.display = "flex";
//             reg.style.display = "flex";
//         }
//     } else {
//         content.style.opacity = "1";
//         content.style.pointerEvents = "auto";
//         windmenu.style.display = "none";
//         if (add) {
//             add.style.display = "none";
//         }
//         if (log) {
//             log.style.display = "none";
//             reg.style.display = "none";
//         }
//     }
// }


