// code snippet from EmailJS //
const emailResponse = document.getElementById('email_response');

function sendMail(contactForm) {
    emailjs.send("gmail", "template_t5j8d06", {
            "from_name": contactForm.from_name.value,
            "email": contactForm.email.value,
            "message": contactForm.message.value
        })
        // code credit to fellow student Kirsty Chatterton (https://github.com/KirstChat/how-till-spake-norn-irish/blob/master/static/js/contact.js) and modified: //
        .then(
            //Change button text to confirm feedback has been sent
            function (response) {
                emailResponse.innerHTML = `<p class="email_response">Email sent! We will respond as soon as we can. Chur!</p>`;
            },
            //If feedback fails to send, change button text to ask user to try again
            function (error) {
                emailResponse.innerHTML = `<p class="email_response">Email Not Sent. Please Try Again.</p>`;
            }
        );
    //Resets contact form after email sent
    document.getElementById('contact_form').reset();
    return false;
}