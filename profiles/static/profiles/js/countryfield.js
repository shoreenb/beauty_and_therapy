 let countrySelected = $('#id_default_country').val();
 if (!countrySelected) {
     $('#id_default_country').css('colour', '#aab7c4');
 };
 $('#id_default_country').change(function () {
     countrySelected = $(this).val();
     if (!countrySelected) {
         $(this).css('color', '#000');
     } else {
         $(this).css('color', '#000');
     }
 });