var $ = jQuery.noConflict();
$(document).ready(function(){
    $('#tabla_usuarios').html("");
    for(let i = 0;i < response.lenght;i++){
        let fila = '<tr>';
        fila += '</td>' + (i +1) + '</td>';
        fila += '</td>' + response [i]["fields"]['username'] + '</td>';
        fila += '</tr>';
        $('#tabla_usuarios').append(fila);
    } 
    $('#tabla_usuarios').DataTable({
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
});