<script>
    var $ = jQuery.noConflict();
    $(document).ready( function (){
    $('#tabla_usuarios').DataTable()
    });
</script>


var $ = jQuery.noConflict();
function listadoUsuarios(){
    $.ajax({
        url: "/usuarios/listar_usuarios",
        type:"get",
        dataType: "json",
        succes: function(response){
            $('#lista_usuarios').Datatable();
        },
        error: function(error){
            console.log(error);
        }
    });
}
$(document).ready(function (){
    listadoUsuarios();
})