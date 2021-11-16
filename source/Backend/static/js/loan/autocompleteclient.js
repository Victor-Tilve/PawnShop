$( function() {
    var availableTags = [
    {% for cliente in clientes %}
    {
      value: "{{cliente.pk}}",
      label: "{{cliente.nombre}}",
      last_name: "{{cliente.apellido}}",
    },
    {% endfor %}
    // "{{cliente.pk}} {{cliente.nombre}} {{cliente.apellido}}",
    // "{{cliente.nombre}}",
    ];
    $( "#cliente-name" ).autocomplete({
                                    minLength: 1,
                                    source: availableTags,
                                    focus: function( event, ui ) {
                                      $( "#cliente-name" ).val( ui.item.label + ' ' + ui.item.last_name );
                                      return false;
                                    },
                                    select: function( event, ui ) {
                                                                    $( "#cliente-name" ).val( ui.item.label + ' ' + ui.item.last_name );
                                                                    $( "#client-id" ).val( ui.item.value );                  
                                                                    return false;
                                                                  }
                                  })
    .autocomplete( "instance" )._renderItem = function( ul, item ) {
    return $( "<li>" )
      .append( "<div>" + item.label + " " + item.last_name + "</div>" )
      .appendTo( ul );
      };
} );