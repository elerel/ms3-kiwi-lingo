// code snippet from EmailJS and CI Sending Emails Using EmailJS Rosie Walkthrough Project//
const emailResponse = document.getElementById('email_response');

function sendMail(contactForm) {
    emailjs.send("gmail", "template_t5j8d06", {
            "from_name": contactForm.from_name.value,
            "email": contactForm.email.value,
            "message": contactForm.message.value
        })
        .then(
            //Confirm email sent message
            function (success) {
                emailResponse.innerHTML = "Email sent! We will respond as soon as we can. Chur!";
            },
            //If email has not been sent display error message
            function (failed) {
                emailResponse.innerHTML = "Email Not Sent. Please Try Again.";
            }
        );
    //Resets contact form after email sent
    document.getElementById('contact_form').reset();
    return false;
}