relojActual = Date.now();
lista_desplegada = 1;
primera_carga = false;
url_listas = "";
url_lista_content = "";
mis_listas = [];

function init(){
    compartirReferido(); 
    get_listas(url_listas);
    get_lista_content(url_lista_content, 1);
    relojInit(relojActual);
    get_lista_clones(url_clones);   
    websocket();
}

function compartirReferido(){
    btn = document.getElementById("btnWhatsapp");  
    btn = document.getElementById("btnCopiar");  
    txt = document.getElementById("txtEnlaceReferido");
    btn.onclick = function(){
        txt.select()
        document.execCommand("copy");
    }
    btnWhatsapp.onclick = function(){
        redir = "whatsapp://send?text=Haz sido invitado a pasamano.com%20" + txt.value
        window.location.href = redir
    }
}

function relojInit(HoraActual){
    relojActual = new Date(HoraActual);
    setTimeout("relojRefresh()",1000);
}

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
    
    document.getElementById("reloj").innerHTML="<b> "+horas+":"+minutos+":"+segundos+"</b>";
    setTimeout("relojRefresh()",1000);
}

// Ajax para notificaciones
function websocket(){
    var chatSocket = new WebSocket('ws://' + window.location.host +
    '/ws/home/');
    chatSocket.onmessage = function(e) {
      var data = JSON.parse(e.data);
      var message = data['message'];
      if (message == "Nuevo jugador en lista"){
        setTimeout("actualizar_pantalla()", 1000);
      }
      document.querySelector('#chat-log').innerHTML += (message + '\n');
    }
}

function actualizar_pantalla(){
    get_listas(url_listas)
    get_lista_content(url_lista_content, lista_desplegada);
    get_lista_clones(url_clones);
    
}

// Tokens de seguridad para ajax
function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}


// ajax para cargar las listas del usuario
function get_listas(url_listas){
    var csrftoken = getCookie('csrftoken');
    $.ajax({
        url: url_listas,
        method: "post",
        beforeSend: function (xhr, settings) {
            var csrftoken = getCookie('csrftoken');
            function csrfSafeMethod(method) {
                // these HTTP methods do not require CSRF protection
                return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
            }
            if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }
        },   
        success: function(respuesta){
            listas_json = JSON.parse(respuesta);
            //actualizar el contenido del div        
            displayListas(listas_json);
        }        
    });
}        

function displayListas(listas_json){
    console.log("mostrando las listas");
    if(listasContainer){
        ContenedorListas = document.getElementById("listasContainer");
        htmlListas = "";
        htmlListas += "<div class ='btn-group role='group'>";
        htmlListas += "  <div class = 'btn-group-vertical'>";
        listas_json.forEach(function(item, index){
            url = url_lista_content;
            htmlListas += "    <button class='btn btn-primary' onclick=get_lista_content('" + url + "'," + item.id + ");> Lista" + item.id + " " + item.nivel +" </button>";
        })
        htmlListas += "</div></div>";
        ContenedorListas.innerHTML = htmlListas;
    }
}

// ajax para cargar los datos de la lista
function get_lista_content(url_lista_content, id){
    $.ajax({
        url: url_lista_content + id + "/",
        method: "post",
        beforeSend: function (xhr, settings) {
            var csrftoken = getCookie('csrftoken');
            function csrfSafeMethod(method) {
                // these HTTP methods do not require CSRF protection
                return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
            }
            if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }
        },   
        success: function(respuesta){
            lista_json = JSON.parse(respuesta);
            lista_desplegada = id;
            // actualizar el contenido del div
            displayListaContent(lista_json);
        }        
    });
}

function get_lista_clones(url_lista_clones){
    $.ajax({
        url: url_lista_clones,
        method: "post",
        beforeSend: function (xhr, settings) {
            var csrftoken = getCookie('csrftoken');
            function csrfSafeMethod(method) {
                // these HTTP methods do not require CSRF protection
                return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
            }
            if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }
        },   
        success: function(respuesta){
            lista_json = JSON.parse(respuesta);
            // actualizar el contenido del div
            displayListaClones(lista_json);
        }        
    });
}

function displayListaClones(clones_json){
    if(clonesContainer){
        ContenedorClones = document.getElementById("clonesContainer");
        htmlClones = "";
        htmlClones += "<div class ='btn-group role='group'>";
        htmlClones += "<div class = 'btn-group-vertical'>";
        clones_json.forEach(function(item, index){
            url = url_clones;
            htmlClones += "    <a href = " + url_activar_clon + item.id +">" + "Clon " + item.estado + " " + item.nivel + " </a>" ;
        })
        htmlClones += "</div></div>";
        ContenedorClones.innerHTML = htmlClones
    }
}

function displayListaContent(lista_json){
    console.log("mostrando contenido de la lista");
    $("#j0").text(lista_json[0].user); 
    $("#j0").css({"color": lista_json[0].color});
    
    $("#j1").text(lista_json[1].user); 
    $("#j1").css({"color": lista_json[1].color}); 

    $("#j2").text(lista_json[2].user); 
    $("#j2").css({"color": lista_json[2].color}); 

    $("#j3").text(lista_json[3].user); 
    $("#j3").css({"color": lista_json[3].color}); 

    $("#j4").text(lista_json[4].user); 
    $("#j4").css({"color": lista_json[4].color}); 

    $("#j5").text(lista_json[5].user); 
    $("#j5").css({"color": lista_json[5].color}); 

    $("#j6").text(lista_json[6].user); 
    $("#j6").css({"color": lista_json[6].color}); 

    enc = 'Lista ' + lista_json[7].lista_id + ' ' + lista_json[7].estado + ' ' + lista_json[7].nivel
    $("#encabezado_lista").text(enc);

}
