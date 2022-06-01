var $ = jQuery.noConflict();
function listadoUsuarios(){
            $.ajax({
                url:"/usuarios/listar_usuarios/",
                type:'GET',
                datatype: 'json',
                succes: function(response){
                    $('#lista_usuarios tbody').html("");
                    for(let i = 0;i < response.lenght;i++){
                        let fila = '<tr>';
                        fila += '</td>' + (i +1) + '</td>';


                        fila += '</tr>';
                        $('#lista_usuarios tbody').append(fila);
                    }
                    $('#lista_usuarios').DataTable({
                        language: {
                            decimal: "",
                            emptyTable: "No hay información",
                            info: "Mostrando _START_ a _END_ de _TOTAL_ Entradas",
                            infoEmpty: "Mostrando 0 to 0 of 0 Entradas",
                            infoFiltered: "(Filtrado de _MAX_ total entradas)",
                            infoPostFix: "",
                            thousands: ",",
                            lengthMenu: "Mostrar _MENU_ Entradas",
                            loadingRecords: "Cargando...",
                            processing: "Procesando...",
                            search: "Buscar:",
                            zeroRecords: "Sin resultados encontrados",
                            paginate: {
                              first: "Primero",
                              last: "Ultimo",
                              next: "Siguiente",
                              previous: "Anterior",
                            },
                        }, 
                    });
                },
                error: function(error){
                    console.log(error);
                }
            })
}
$(document).ready(function(){
    listadoUsuarios();
})

$(document).ready( function (){
    $('#tabla_usuarios').DataTable()
    });