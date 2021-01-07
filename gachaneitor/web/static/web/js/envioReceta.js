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
            console.log(evt.target.result)
            postReceta(evt.target.result);
        }
    }
    else if ($("#textAreaReceta").val().length) {
        postReceta(Datos.get("textAreaReceta"))
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
    alert("Esta es la receta que se ha enviado: \n" + response.toString());
    if (response["error"] === false) {
        $("#alertaExito").empty()
        $("#alertaExito").prepend(response["result"])
        $("#alertaExito").prepend("<strong>" + "Exito" + "</strong><br>")
        $("#alertaExito").append(<button type="button" class="close" data-dismiss="alert" aria-label="Close">
            <span aria-hidden="true">&times;</span>
        </button>)
        $("#alertaExito").fadeTo(4000, 500)
    }

    if (response["error"] === true) {
        $("#alertaError").empty()
        $("#alertaError").prepend(response["result"])
        $("#alertaError").prepend("<strong>" + "Error" + "</strong><br>")
        $("#alertaError").append(<button type="button" class="close" data-dismiss="alert" aria-label="Close">
            <span aria-hidden="true">&times;</span>
        </button>)
        $("#alertaError").fadeTo(4000, 500)
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