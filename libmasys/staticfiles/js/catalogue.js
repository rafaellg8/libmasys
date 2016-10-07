$(document).ready(function() {

    $('#tableResultLibros').dataTable({
        "processing": true,
        "bLengthChange": false,
        "language": {
            "sProcessing": "Procesando...",
            "sLengthMenu": "Mostrar _MENU_ registros",
            "sZeroRecords": "No se encontraron resultados",
            "sEmptyTable": "Ningún dato disponible en esta tabla",
            "sInfo": "Mostrando registros del _START_ al _END_ de un total de _TOTAL_ registros",
            "sInfoEmpty": "Mostrando registros del 0 al 0 de un total de 0 registros",
            "sInfoFiltered": "(filtrado de un total de _MAX_ registros)",
            "sInfoPostFix": "",
            "sSearch": "Buscar:",
            "sUrl": "",
            "sInfoThousands": ",",
            "sLoadingRecords": "Cargando...",
            "oPaginate": {
                "sFirst": "Primero",
                "sLast": "Último",
                "sNext": "Siguiente",
                "sPrevious": "Anterior"
            },
            "oAria": {
                "sSortAscending": ": Activar para ordenar la columna de manera ascendente",
                "sSortDescending": ": Activar para ordenar la columna de manera descendente"
            }
        },
        "ajax": {
            "processing": true,
            "url": { % url 'catalogoJSONLibros' %
            },
            "dataSrc": "",
        },

        "columns": [{
            "data": "fields.titulo"
        }, {
            "data": "fields.autor"
        }, {
            "data": "fields.descripcion"
        }, {
            "data": "fields.anio"
        }, {
            "data": "fields.editorial"
        }, {
            "data": "fields.genero"
        }, {
            "data": "fields.estanteria"
        }, {
            "data": "fields.codigo"
        }]
    });
});


$(document).ready(function() {

    $('#tableResultDVDs').dataTable({
        "processing": true,
        "bLengthChange": false,
        "showNEntries": false,
        "language": {
            "sProcessing": "Procesando...",
            "sLengthMenu": "Mostrar _MENU_ registros",
            "sZeroRecords": "No se encontraron resultados",
            "sEmptyTable": "Ningún dato disponible en esta tabla",
            "sInfo": "Mostrando registros del _START_ al _END_ de un total de _TOTAL_ registros",
            "sInfoEmpty": "Mostrando registros del 0 al 0 de un total de 0 registros",
            "sInfoFiltered": "(filtrado de un total de _MAX_ registros)",
            "sInfoPostFix": "",
            "sSearch": "Buscar:",
            "sUrl": "",
            "sInfoThousands": ",",
            "sLoadingRecords": "Cargando...",
            "oPaginate": {
                "sFirst": "Primero",
                "sLast": "Último",
                "sNext": "Siguiente",
                "sPrevious": "Anterior"
            },
            "oAria": {
                "sSortAscending": ": Activar para ordenar la columna de manera ascendente",
                "sSortDescending": ": Activar para ordenar la columna de manera descendente"
            }
        },
        "ajax": {
            "processing": true,
            "url": { % url 'catalogoJSONDVDs' %
            },
            "dataSrc": ""
        },

        "columns": [{
            "data": "fields.titulo"
        }, {
            "data": "fields.autor"
        }, {
            "data": "fields.descripcion"
        }, {
            "data": "fields.anio"
        }, {
            "data": "fields.editorial"
        }, {
            "data": "fields.genero"
        }, {
            "data": "fields.estanteria"
        }, {
            "data": "fields.codigo"
        }]
    });
});



    $(document).ready(function() {

        $("#showTableDVD").click(function() {
            $("#tableResultDVDs").show();
            $("#tableResultLibros").hide();
        });

        $("#showTableBooks").click(function() {
            $("#tableResultLibros").show();
            $("#tableResultDVDs").hide();
        });
    });
