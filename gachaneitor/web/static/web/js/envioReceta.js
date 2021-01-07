var formulario = document.getElementById("formulario");
var btnEnviar = document.getElementById("btnEnviar");
var btnClose = document.getElementsByClassName("close");

var csrfToken = getCookie("csrftoken");

$.ajaxSetup({
    beforeSend: function (xhr) {
        xhr.setRequestHeader("X-CSRFToken", csrfToken);
    }
})

formulario.addEventListener("submit", function (e) {
    e.preventDefault();
    //var Datos = new FormData(formulario);
    var textArea = document.getElementById("textAreaReceta").value;
    var reader = new FileReader();

    $('#alertaExito').slideUp(200)
    $('#alertaCamposVacios').slideUp(200)
    $('#alertaError').slideUp(200)

    if ($('#fileReceta').val()) {
        reader.readAsText(Datos.get("fileReceta"), "UTF-8");
        reader.onload = function (evt) {
            postReceta(evt.target.result);
        }
    }
    else if ($("#textAreaReceta").val().length) {
        postReceta(textArea);
    }
    else {
        $("#alertaCamposVacios").fadeTo(4000, 500).slideUp(500, function () {
            $("#alertaCamposVacios").slideUp(500)
        })
    }
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
            success: function (response) {
                create_feedback(response)
            }
        }
    );
}

function create_feedback(response) {
    //alert("Esta es la receta que se ha enviado: \n" + response.toString());
    if (response["error"] === false) {
<<<<<<< HEAD
        $("#alertaError").hide();
        $("#alertaExito").show();
        $("#alertaExito").html("<strong>" + "Exito" + "</strong><br>" + response["result"])
    }

    if (response["error"] === true) {
        $("#alertaExito").hide();
        $("#alertaError").show()
        $("#alertaError").html("<strong>" + "Error" + "</strong><br>" + response["result"])
=======
        $("#alertaExito").empty()
        $("#alertaExito").slideDown(200)
        $("#alertaExito").prepend(response["result"])
        $("#alertaExito").prepend("<strong>" + "Exito" + "</strong><br>")
        //$("#alertaExito").append("<button type=\"button\" class=\"close\" data-dismiss=\"alert\" aria-label=\"Close\">"+
        //    "<span aria-hidden=\"true\">&times;</span>"+
        //"</button>")
    }

    if (response["error"] === true) {
        $("#alertaError").empty()
        $("#alertaError").slideDown(200)
        $("#alertaError").show()
        $("#alertaError").prepend(response["result"])
        $("#alertaError").prepend("<strong>" + "Error" + "</strong><br>")
        //$("#alertaError").append("<button type=\"button\" class=\"close\" data-dismiss=\"alert\" aria-label=\"Close\">"+
        //    "<span aria-hidden=\"true\">&times;</span>"+
        //"</button>")
>>>>>>> 5698dac279f4bebb5ef2b17a2675c34eb29de133
    }
}

function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}