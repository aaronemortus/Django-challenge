function format(data){
  return '<div style="float:left;width:30%;">'+
         '<table class="details-table" cellpadding="5" cellspacing="0" border="0" >' +
      '<tr>' +
        '<td>Full name</td>' +
        '<td>' + data[2] + ' ' + data[3] + '</td>' +
      '</tr>' +
      '<tr>' +
          '<td>Email</td>' +
          '<td>' + data[4] + '</td>' +
      '</tr>' +
      '<tr>' +
          '<td>Gender</td>' +
          '<td>' + data[5] + '</td>' +
      '</tr>' +
      '<tr>' +
          '<td>Company</td>' +
          '<td>' + data[6] + '</td>' +
      '</tr>' +
      '<tr>' +
          '<td>City</td>' +
          '<td>' + data[7] + '</td>' +
      '</tr>' +
      '<tr>' +
          '<td>Title</td>' +
          '<td>' + data[8] + '</td>' +
      '</tr>' +
      '<tr>' +
          '<td>Location</td>' +
          '<td>lat: ' + data[9] + '<br>lng: ' + data[10] + '</td>' +
      '</tr>' +
  '</table></div>'+
  '<div style="float:left;width:70%;">'+
       '<iframe width="100%" height="450" style="border:0" loading="lazy" allowfullscreen src="https://www.google.com/maps/embed/v1/place?key='+google_api+'&q='+data[9]+ ','+data[10]+'"></iframe>'+
   '</div>'
  ;
}

$(document).ready(function(){
  $.ajax({
    type: "GET",
    url: api_url,
    contentType: "application/json; charset=utf-8",
    dataType: "json",
    success: function(data){
      $('#customersTable > tbody').empty();
      $.each(data, function (i, item) {
        var customersTable = $('#customersTable > tbody');
        var rows =
          '<tr>' +
          '<td class="details-control"><i class="fa fa-list-alt" data-toggle="tooltip" title="Click here to expand map!"></i></td>' +
          '<td>' + item.id +'</td>' +
          '<td>' + item.first_name +'</td>' +
          '<td>' + item.last_name +'</td>' +
          '<td>' + item.email +'</td>' +
          '<td>' + item.gender +'</td>' +
          '<td>' + item.company +'</td>' +
          '<td>' + item.city +'</td>' +
          '<td>' + item.title +'</td>' +
          '<td>' + item.latitude +'</td>' +
          '<td>' + item.longitude +'</td>' +
          '</tr>';
          $('#customersTable thead').removeClass('d-none');
          customersTable.append(rows);
      });
      $('#customersTable').DataTable({
        "columnDefs": [
           {
             "targets": [ 5 ],
             "visible": false,
           },
           {
             "targets": [ 9 ],
             "visible": false
           },
           {
             "targets": [ 10 ],
             "visible": false
           }
         ]
       } );
    },
    failure: function (data) {
      alert(data.responseText);
    },
    error: function (data) {
      alert(data.responseText);
    }
  });

  $('#customersTable tbody').on('click', 'td.details-control', function(event){
      var tr = $(this).closest('tr');
      var row = $('#customersTable').DataTable().row(tr);
      if(row.child.isShown()){
          row.child.hide();
          tr.removeClass('shown');
          $(this).removeClass('detail-shown');
      }
      else{
          row.child(format(row.data())).show();
          tr.addClass('shown');
          $(this).addClass('detail-shown');
      }
  });
});
