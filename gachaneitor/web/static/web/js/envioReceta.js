var formulario = document.getElementById("formulario");

var csrfToken = getCookie("csrftoken");

$.ajaxSetup({
    beforeSend: function (xhr) {
        xhr.setRequestHeader("X-CSRFToken", csrfToken);
    }
})
formulario.addEventListener("submit", function (e) {
    e.preventDefault();
    var Datos = new FormData(formulario);
    var reader = new FileReader();

    if( $('#inputArchivo').val() ){
        reader.readAsText(Datos.get("fileReceta"), "UTF-8");
        reader.onload = function (evt) {
            postReceta(evt.target.result);
        }
    }
    else if( $("#textAreaReceta").val().length ) {
        postReceta(Datos.get("textAreaReceta"))
    }
    else {
        $("#alertaCamposVacios").fadeTo(4000, 500).slideUp(500, function () {
            $("#alertaCamposVacios").slideUp(500)
        })
    }


    //let req = new Request(uri, options);
})

async function postReceta(text) {
    var url = '/';

    $.ajax(
    {
        type: 'POST',
        url: url,
        data: {
            "receta": text
        },
        dataType: 'json',
        success: function(response) {
            create_feedback(response)
        }
    }
);
}

function create_feedback(response) {
    alert("Esta es la receta que se ha enviado: \n" + response.toString());
    if (response["error"] === true) {
        $("#alertaErrorLexico").prepend("Traza del procesado")
        $("#alertaErrorLexico").prepend("<strong>"+"Error léxico"+"</strong><br>")
        $("#alertaErrorLexico").fadeTo(4000, 500)
    }
}

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