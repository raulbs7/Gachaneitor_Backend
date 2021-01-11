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

    if ($('#fileReceta').val()) {
        reader.readAsText(Datos.get("fileReceta"), "UTF-8");
        reader.onload = function (evt) {
            postReceta(evt.target.result);
        }
    }
    else if ($("#textAreaReceta").val().length) {
        postReceta(Datos.get("textAreaReceta"))
    }
    else {
        $("#alertaError").hide();
        $("#alertaExito").hide();
        $("#alertaCamposVacios").show()
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
    alert("Se ha enviado la receta");
    if (response["error"] === false) {
        $("#alertaCamposVacios").hide()
        $("#alertaError").hide();
        $("#alertaExito").show();
        $("#alertaExito").html("<strong>" + "Exito" + "</strong><br>" + response["result"])
    }

    if (response["error"] === true) {
        $("#alertaCamposVacios").hide()
        $("#alertaExito").hide();
        $("#alertaError").show()
        $("#alertaError").html("<strong>" + "Error" + "</strong><br>" + response["result"])
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