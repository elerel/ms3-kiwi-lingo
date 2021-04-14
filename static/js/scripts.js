$(document).ready(function () {
    $(".sidenav").sidenav({
        edge: "right"
    });
    $('.collapsible').collapsible();

    // Code snippet (to confirm pw's match) from Stackoverflow https://stackoverflow.com/questions/21727317/how-to-check-confirm-password-field-in-form-without-reloading-page/21727518    
    $('#password, #confirm_password').on('keyup', function () {
        if ($('#password').val() == $('#confirm_password').val()) {
            $('#message').html('Passwords Match!').css('color', 'green');
        } else
            $('#message').html('Password Do Not Match!').css('color', 'red');
    });
});