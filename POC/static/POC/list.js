// $(document).ready(function(){
//   $("#test").focus(function(){
//     alert('hiii')
//   });
// });


$(document).ready(function(){
$('#test').focus(function(){
$('#test1').val("");
$('#test2').val("");

    });
    });

$(document).ready(function(){
$('#test1').focus(function(){
$('#test').val("");
    $('#test2').val("");

        });
        });

$(document).ready(function(){
$('#test2').focus(function(){
$('#test').val("");
$('#test1').val("");

                });
                });





  $(document).ready(function(){
  $('#test2').focus(function(){
  $('#test').val("");
  $('#test1').val("");

                                });
                                });


$(document).ready(function(){
$('button').click(function(){
var x=$('#test').val();
var y=$('#test1').val();
var z=$('#test2').val();
if (x=='' & y=='' & z=='')
{
  alert("Please enter some searchable data in order to search");
  return false;
}
});
  });


  $(document).on('click', '#deletebtn', function(){
      return confirm('Are you sure you want to delete this?');
  })
