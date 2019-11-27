$(document).ready(function(){
  $("#save").click(function(){
    // alert('Javascript Enabled')
  });
});

$(document).ready(function(){
  $("#id_age").blur(function(){
    var age_value =$(this).val();
    if (age_value>=150){
      alert('Please enter valid age');
      $("#id_age").val("");
    }
    if (age_value<0){
      alert('Please enter valid age');
      $("#id_age").val("");
    }
  });
});


$(document).ready(function(){
  $("#id_name").keyup(function(){
    var name_values=$(this).val();
    var numberRegex = /^[+-]?\d+(\.\d+)?([eE][+-]?\d+)?$/;
    var specialcharacter = /^[A-Za-z0-9 '.-]+$/;


    if(numberRegex.test(name_values)) {

   alert('Number not Allowed');
   // alert(name_values);
   $("#id_name").val("");


}
if(!specialcharacter.test(name_values)) {

alert('Special Characters are  not Allowed');
// alert(name_values);
$("#id_name").val("");


}


  });
});




  var city = $("select[name=city] option"); // the collection of initial options
  $("select[name=country]").change(function(){
      var countryselected = parseInt(this.value); //get drop1 's selected value
      $("select[name=city]")
                       .html(city) //reset dropdown list
                       .find('option').filter(function(){
                          return parseInt(this.value) < countryselected; //get all option with value < drop1's selected value
                        }).remove();  // remove
  });




// var doc_val_check = $('#id_age').attr("value");
//     if (Object.prototype.toString.call(doc_val_check) != '[object String]' ) {
//         doc_val_check = "";
//     }


$(document).ready(function(){
$('#id_zip').blur(function(){
var zip_value=$(this).val();
if (zip_value.length<6  ){
alert('Please Enter valid Zip code');

}
if (zip_value.length>6  ){
alert('Please Enter valid Zip code');

}
// age_val_check=$('#id_age').$(this).val();
// alert(age_val_check);
// if (Object.prototype.toString.call(age_val_check) != '[object String]' ) {
//     age_val_check = "";
// }
});

});



$(document).ready(function(){
  $("#id_country").change(function () {
        var url = $("#personForm").attr("data-cities-url");  // get the url of the `load_cities` view
        var countryId = $(this).val();  // get the selected country ID from the HTML input

        $.ajax({                       // initialize an AJAX request
          url: url,                    // set the url of the request (= localhost:8000/hr/ajax/load-cities/)
          data: {
            'country': countryId       // add the country id to the GET parameters
          },
          success: function (data) {   // `data` is the return of the `load_cities` view function
            $("#id_city").html(data);  // replace the contents of the city input with the data that came from the server
          }
        });

      });
      });
