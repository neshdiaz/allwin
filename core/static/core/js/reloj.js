relojActual = Date.now();

/*function relojInit(HoraActual){
    relojActual = new Date(HoraActual);
    //setTimeout("relojRefresh()",1000);
}*/

function relojRefresh(){
    horas = "";
    minutos = "";
    segundos = "";
    relojActual.setSeconds(relojActual.getSeconds()+1)
    hor = relojActual.getHours();
    min = relojActual.getMinutes();
    seg = relojActual.getSeconds();
    if (hor < 10){
        horas = "0"+hor;
    } else{
        horas ="" + hor
    }

    if (min < 10){
        minutos = "0"+min;
    } else{
        minutos ="" + min
    }
    
    if (seg < 10){
        segundos = "0"+seg;
    } else{
        segundos ="" + seg
    }
    
    //document.getElementById("reloj").innerHTML="<b> "+horas+":"+minutos+":"+segundos+"</b>";
    //setTimeout("relojRefresh()",1000);
}