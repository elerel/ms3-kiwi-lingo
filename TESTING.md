# <p align="center">**Testing Section**</p>

## Contents
- [**Testing**](#testing)
    - [Validation](#validation)
    - [Performance](#performance)
    - [Device Testing](#device-testing)
    - [Browser Testing](#browser-testing)
    - [Bugs](#bugs)
    - [Testing CRUD Functionality](#testing-crud-functionality)
    - [Contact Form](#contact-form)
    - [Links and Navigation Testing](#links-and-navigation-testing)
    - [Testing User Stories](#testing-user-stories)
    - [Testing Recap](#testing-recap)

    ---

## **Validation**

To ensure the site had correct code syntax, it was validated using [W3 MarkUp Validation Service](https://validator.w3.org/)

HTML Validation:
    ![image](https://res.cloudinary.com/elerel/image/upload/v1620229064/htmlvalidation_eobnvb.png)

To resolve, I simply replaced the "section" with a "div" and no further errors were found:
    ![image](https://res.cloudinary.com/elerel/image/upload/v1620229196/htmlgood_ru3oxa.png)

CSS Validation- no errors found:
    ![image](https://res.cloudinary.com/elerel/image/upload/v1620229407/cssvalidation_ket6hj.png)


JSHINT:

JSHint picks up Jquery "$"symbol as an undefined variable which can be safely ignored:


![image](https://res.cloudinary.com/elerel/image/upload/v1620229796/jshint_znig9a.png)

EmailJS:

JSHint picks up one unused variable (sendMail) and one undefined variable (emailjs) which I found can be safely ignored as they are functioning as they should:


![image](https://res.cloudinary.com/elerel/image/upload/v1620229849/Picture8_aacxrf.png)

---


PEP8: Trailing White Space 

![image](https://res.cloudinary.com/elerel/image/upload/v1620229562/pep8error_wjdiqp.png)

Which I later resolved:

![image](https://res.cloudinary.com/elerel/image/upload/v1620229651/pep8good_vilveb.png)

---

## Performance

Using Google Chrome's DevTools, these Lighthouse scores are based on the opening page of the site, being viewed on desktop and mobile devices. The lowest score (performance) was mainly due to the loading time of the first carousel image which could be addressed or better formatted at a later stage:

Desktop Score:

![image](https://res.cloudinary.com/elerel/image/upload/v1620249174/lighthousedtop_ko6uv6.png)


Mobile Score:

![image](https://res.cloudinary.com/elerel/image/upload/v1620249180/lighthousemobile_hzkxit.png)


---

### Device Testing

In order to ensure the site worked well, functioning as expected and responsive on all screen sizes, I manually tested the site across various devices which are of the following:

**IOS**

Mobiles:

- IPhone 11 Pro Max on Mobile Safari 13
- IPhone X on Mobile Safari
- IPhone 12 Mini - Chrome
- IPhone 5S - UC Browser

IPads:
- IPad Pro 12.9.2020 on Safari

Mac:
- MAC OS Big Sur Safari 14    


**Android:**

Mobiles: 
- Samsung Galaxy S10
- Samsung Galaxy S21 on Firefox
- Huawei P30 Chrome (Bug: Missing "search" in button on glossary page. Noted below in [bugs](#bugs) section)
- One Plus 8 - Firefox
- Samsung Galaxy Note 20 - Samsung Internet

Tablets:

Samsung Galaxy Tab S7 on Firefox

I used Browserstack, Crossbrowserstack, Google Chrome's Developer Tools (Responsive mode) and a number of different devies available through DevTools. 


### Browser Testing

To ensure the site was responsive and functioning as it should, I tested the site across the following browsers:

- Google Chrome
- Firefox
- Microsoft Edge
- Safari
- Opera (Real Windows 10)
- Internet Explorer 11 (on Windows 10)

No issues or bugs to report, thankfully layout and site functions operating as they should.

Back to [Contents](#contents)

---

### Bugs

The one bug encountered during development was the missing search text in the search button (Glossary page) and the "reset" field is displayed below the button as shown below:

![image](https://res.cloudinary.com/elerel/image/upload/v1620300791/searchresponsive2_gr0jyh.png)

The bug was discovered when resizing in Responsive mode in Chrome Developer Tools and while testing across several devices. Once the width was under 366px the "search" text would disappear then when under 340px, the "reset" text would also go.
To overcome the issue, I tried re-sizing the text font to a much smaller size but it did not work well with the size of the font-awesome icons, as they were much bigger when resized. Instead, I placed each of the buttons in their own div and styled them to have a larger width, but then this took away the consistency of the search/reset buttons from the index/landing page. I then changed the buttons over to the original style, as in the index page and removing the icons to keep it consistent:

![image](https://res.cloudinary.com/elerel/image/upload/v1620330798/searchreset_zpzwye.png)

![image](https://res.cloudinary.com/elerel/image/upload/v1620330854/glossarysearch_ov2xm1.png)


### Remaining Bugs

Nothing reported from other users, but one or two things came up during testing across other browsers via Browserstack. In the Add Word form (Add Word Page) there seems to be a small white figure just below the category select section in the form: 

![image](https://res.cloudinary.com/elerel/image/upload/v1620332018/addwordsnip2_jckauf.png)

This was found while testing on an Iphone 8 on Mobile Safari. It turns out to be an IOS drop-down feature as you can make out below:

![image](https://res.cloudinary.com/elerel/image/upload/v1620332323/iosfeature_ryryqt.png)

Not hugely concerning as it does not overly deflect from the form's function or image so I left it alone.

Another bug that did come up but did not end up being resolved is the category select function not operating correctly on an IPhone X (family member's phone). Once the user selected the category, it then changed and did not remain the same category as previously chosen. For example, if I wanted to choose the "Family" category, it then changed to another random category in the drop-down list:

![image](https://res.cloudinary.com/elerel/image/upload/v1620333487/Screenshot_20210506-213242_WhatsApp_xht5oh.jpg) 

![image](https://res.cloudinary.com/elerel/image/upload/v1620333520/Screenshot_20210506-213632_WhatsApp_bveaz9.jpg)

I could not find this error on any other device and tried looking for it to pop up through Browserstack or DevTools. As I was unable to source it on another device and could not physically see the error (sister's phone who lives abroad) I left it be.


Finally, the Contact Us page bug- once an email has been submitted, the labels move down on top of the placeholder text:

![image](https://res.cloudinary.com/elerel/image/upload/v1620382839/contactbug_ln3iph.png)


It is a minor bug but may give off a negative user experience once the email is sent. I was out of time to try and fix this bug unfortunately, but the good thing is that the labels go back to their original state once re-selected.


Back to [Contents](#contents)

---

### Testing CRUD Functionality

The fundamental learning outcomes in the Data Centric Development module was being able to build an application that includes the Create, Read, Update, and Delete functionalities. Kiwi Lingo users should be able to create a profile and CREATE or add a word/phrase. They should also be able to read other listed/added additions from other users (READ), UPDATE their added word and also DELETE the word should they choose.

I manually tested this in the following steps:

**CREATE**

 - Upon entering the site, I navigate to the "Register" button on the navbar where I can register or *create* a profile.
 - As a new user, I am informed I do not have any added words and can easily spot where I can *create* a new addition (word) to the glossary by clicking on the Add Word button on my profile page.


 **READ**

 - Once my profile is up and running, I add my favourite Kiwi word "Tu meke" to the glossary:

 ![image](https://res.cloudinary.com/elerel/image/upload/v1620334735/addedword1_otv4ui.png)

 - I can then see that my "tu meke" word has been added and is placed in the glossary for others to *read* also:

 ![image](https://res.cloudinary.com/elerel/image/upload/v1620334823/addedword2_waucg2.png)   

 - I can also read my own additions to the site if I head back to my profile page, which makes it easy to see what I have added for my own collection:

 ![image](https://res.cloudinary.com/elerel/image/upload/v1620334978/profile_iwbgdw.png)

 
 **UPDATE**

 - If I want to go in and update my phrase "tu meke",  I can simply stay on my profile page or on the glossary page where I can select the *edit* button. I change the example to a longer sentence and voila, it is updated as expected:

 ![image](https://res.cloudinary.com/elerel/image/upload/v1620335273/update_hpxgdc.png)


 **DELETE**

- In case I want to remove my recently added phrase "tu meke" I can simply *delete* the word by clicking the "delete" button on my profile or glossary page. A confirmation modal will appear confirming the delete and once selected, the word then is removed from the glossary and profile pages:

![image](https://res.cloudinary.com/elerel/image/upload/v1620335529/confirmdelete_fvxwax.png)

![image](https://res.cloudinary.com/elerel/image/upload/v1620335520/profile2_jwii9o.png)

As a user, I can also choose to *delete* my profile by clicking the "delete profile" button towards the bottom of the page. A confirmation modal will still appear confirming the deletion and once selected, my profile is gone and removed from the users collection in the database.

![image](https://res.cloudinary.com/elerel/image/upload/v1620335663/deleteprof_zxurxh.png)
![image](https://res.cloudinary.com/elerel/image/upload/v1620335715/deleteprofile_aoea49.png)
![image](https://res.cloudinary.com/elerel/image/upload/v1620335724/deleteconfim_gvhcmg.png)


The site owner is also able to perform the above with the Categories collection. I manually tested this in the following steps:

- Once logged in, I select "Manage Categories" in the navbar menu.

![image](https://res.cloudinary.com/elerel/image/upload/v1620336178/readcategories_rujkp6.png)

- I am able to read the various categories that have already been added to the categories section "domestic", "everyday", "Maori" etc.
- I click "Add Category" and a form appears the page where I enter the new category name I wish to add, "Home".
- I can then see my new category "Home" is added to the categories page and is displayed like the others in a card format.
- I then *edit* the category name to *Home Use* instead and can see that it has been successfully updated. 
- To remove or *delete* the Home Use category, I click delete, where a confirmation modal appears then once delete is selected, the category is removed from the collection.


Back to [Contents](#contents)

---

### Contact Form

In order to check the contact form was functioning correctly, I manually tested this using the following steps:

1. Click on Give Us Feedback on the Glossary Page (if user already logged in, they can click "Contact" from the navbar)
2. Enter in the following details: name, email and message
3. Once "Submit" is clicked, a confirmation message appears stating that the email has been sent and they will be contacted accordingly.

Contact Page: 

![image](https://res.cloudinary.com/elerel/image/upload/v1620384881/contactpg_bqxy34.png)

Email Sent Confirmation: 

![image](https://res.cloudinary.com/elerel/image/upload/v1620382810/emailsent_p9cgto.png)


The email is then received by Kiwi Lingo, with all the relevant details shown in the below screenshot:

![image](https://res.cloudinary.com/elerel/image/upload/v1620383045/emailjs_kajmir.png)


---

### Error Pages

Should the user accidentally type the wrong address or land on a page not featured in the site, I added a 404.html page so that the user can be redirected to the site. I tested this by typing http://kiwi-lingo.herokuapp.com/bananas and the below appears:

![image](https://res.cloudinary.com/elerel/image/upload/v1620336775/404_fpsae3.png)

For the "Manage Categories" page, the site admin is the only user with access to it. With the use of jinja templating, if the user is not logged in as site admin, the user will be redirected to an "Access Denied" message:

![image](https://res.cloudinary.com/elerel/image/upload/v1620337940/accessdenied_kzx3rv.png)


### Links and Navigation Testing

To make sure all links within the site functioned, I manually tested each one so that:
-   each link opened up in a separate tab by using the target_blank attribute
-   the link redirected the user to the correct URL
-   each link has a underline text-decoration when hovered over so that the user knows they will be redirected.

In addition to the links functioning correctly, I also manually tested the navigation links in full screen and mobile view modes. This was to ensure that each link was displaying as it should and that the list of items were correctly displayed.

Back to [Contents](#contents)

---

### Testing User Stories

#### First Time User Stories
##### As a first time user:
-  I want to be able to fully understand what the site is about.
    - *Upon landing on Kiwi Lingo's main index page, the user will be presented with an eye-catching image of one of the many iconic images of New Zealand (Aoraki or Mount Cook) with a welcome and description about Kiwi Lingo, including an invitation to register. Using a 70vh for the carousel images, the user can also make out the about section which details what the user can get out of using Kiwi Lingo.*

    ![image](https://res.cloudinary.com/elerel/image/upload/v1620378915/landingpg_ypznlz.png)

    What's Kiwi Lingo Section- just below the hero image/carousel:

    ![image](https://res.cloudinary.com/elerel/image/upload/v1620378991/whatskiwi_seqsye.png)

-  I want to be able to navigate easily throughout the site.
    - *So that the user can easily navigate throughout the site, I have included a navbar on all pages that redirects the user to the different pages across the site. The user has a few options on where they can be redirected to the main page (Glossary). The site will also include a footer across all pages where the user can contact the site admin as well as links to social networks and travel information sites about New Zealand. Should the user wish to be brought back to the home page, they can click on the Kiwi Lingo logo on the navbar and side navbar (mobile) to redirect them back to the home-page.*

    Navbar ( as above, incl changed Navbar once user has logged in which is displayed on every page):

    ![image](https://res.cloudinary.com/elerel/image/upload/v1620379218/usernavbar_edsxxc.png)

    Footer: 

    ![image](https://res.cloudinary.com/elerel/image/upload/v1620379225/footer_cojlso.png)


-  I want to be able to search for words and phrases commonly spoken in New Zealand.
    - *The user will be able to find common words and phrases in the Glossary page (available to all users)where they can be redirected from the navbar as well as the glossary button further down the index page. I wanted to make this as accessible as possible for the user so I decided to include a search bar (where the user enters in their word of choice and they can be brought to the Glossary also) on the home/index page, as well as being featured on the glossary page.*

    Glossary Page:

    ![image](https://res.cloudinary.com/elerel/image/upload/v1620379358/glossarypg_yvbcf2.png)

    Search bar on home page:

    ![image](https://res.cloudinary.com/elerel/image/upload/v1620379427/searchbar_tk7wbx.png)

-  I want to be able to set up my own account and add my own words or phrases to the site.
    - *The user will need to click on the "Register" button which appears on both navbars, once there they can create a profile and add a word once profile set up is complete. The user will be redirected to their profile page where the user can add a word by clicking on the "Add Word" button, featured just below their profile card:*

    Register Page:
    ![image](https://res.cloudinary.com/elerel/image/upload/v1620379926/register_qs4xwz.png)

    Profile page where they can add a word or phrase:
    ![image](https://res.cloudinary.com/elerel/image/upload/v1620380063/addword_dzzvo4.png)


-  I want to be able to view popular sayings and phrases by viewing the most popular/least popular additions.
    - *I implemented an approval or voting system into each of the word so that users can click on various words which they like or dislike ("Yeah, bro!" and "Nah, bro"). It is intended to be like a popular use voting system but a good feature left to be implemented would be to introduce a rating system where say for example, on a separate table on the glossary page, the most popular word would appear first.*

Thumbs Up/Thumb Down feature:

![image](https://res.cloudinary.com/elerel/image/upload/v1620380484/likes_uu465o.png)


#### Registered User Stories
##### As a regular user:

- I want to be able to easily log in and out of the site.
    - *Each registered user can easily log in by clicking on "Log In" from the navbar which is a separate page where the user enters their details. Once logged in, they simply click "Log Out" once again appearing on the navbar. Should they click on the Register page they can also be redirected to the Log In page:*

Log In Page:

![image](https://res.cloudinary.com/elerel/image/upload/v1620380859/login_wu7epg.png)

Log Out on Navbar:

![image](https://res.cloudinary.com/elerel/image/upload/v1620380867/logout_zkdaqz.png)

Already Registered?

![image](https://res.cloudinary.com/elerel/image/upload/v1620381048/alreadyreg_utsca8.png)


- I want to be able to edit or delete my additions to the site.
    - *Once the user is signed in, they can either edit or delete their added words/phrases from their profile page or the glossary page. Each of the words they have added will contain a "Edit" or "Delete" button in the collapsible accordion:*

![image](https://res.cloudinary.com/elerel/image/upload/v1620381158/editdelete_zfwbi6.png)    

- I want to be able to view additions by other users.
    - *Each registered user can simply visit the glossary page where all additions to the site will appear. In each of the words added, there will be a "by" field that will display the username who added such word.*

![image](https://res.cloudinary.com/elerel/image/upload/v1620381415/byfield_fvnuke.png)

- I want to be able to edit or delete my profile.
    - *The user can simply delete their profile from clicking on "Delete Profile" (Profile page). They will be notified that their words added will remain unless they delete them off the site. They can re-register should they wish to choose a different username (could add an "Edit Profile" page but something that can be implemented in the future).* 

![image](https://res.cloudinary.com/elerel/image/upload/v1620381757/delete_mar7jy.png)

- I want to be able to contact the site owners.
    - *Both registered and non-registered users can contact the site owners by clicking on "Give Us Feedback" featured on the Glossary page. They can also click the contact link on the footer, should they wish to use their preferred email account. Testing for this has been noted in the [Contact Form](#contact-form) section.

![image](https://res.cloudinary.com/elerel/image/upload/v1620381953/feedback_dhbkpk.png)

![image](https://res.cloudinary.com/elerel/image/upload/v1620381960/contact_np32c7.png)


#### Site Owner User Stories

- To provide information on the site and who it is intended for.
    - *I have ensured that the information about the site is displayed on the home/index page of the site, so that the user does not need to search about what the site is or who it is intended for.*
- To allow the site to be accessible (viewing only) without creating an account.
    - *I thought it would create a better user experience for all users to be able to view the glossary, rather than registering first- it encourages the user to interact with the site and could then possibly lead to the user signing up/registering a profile.*
- To be easily contacted should the user lose their log-in details.
    - *The user can find contact details on the footer of the site as well as being directed from the Contact link (navbar) as well as the feedback button on the Glossary page.*
- To allow users to only edit or delete their own additions.
    - *Using a jinja template, the user once in "session" can edit or delete their added words.*
- To be able to delete any inappopriate content added by a registered user.
    - *Just like above, using a jinja template, only the site owner "elerel" can edit or delete added words from registered users from the Glossary Page.*


---


### Testing Recap

To sum up, each page of the site has been manually tested to ensure that:

1. Kiwi Lingo is responsive and functioning on across all devices
1. All images load properly 
1. Navigation buttons and links redirect to the correct pages in the site and to external links
1. External links located in the footer open in a new tab/window and link to the correct site
1. Registered users have access to a profile page to see which words they have added to the glossary
1. Registered users are able to edit and delete any words they've added to the glossary
1. Once logged in, users can easily log out from their profile
1. Site owner is able to edit and delete any of the words from the glossary
1. Site owner is able to add, edit and delete any of the categories from the site
1. Validation appears on all forms
1. If no search results appear from user search query, the user is notified of the results below the search bar
1. Flash messages appear on the correct pages when a user has:
   * Registered their profile
   * If the user chooses a name already in use
   * Welcomes user to their profile
   * If the user entered an incorrect username/password
   * Goodbye message upon logging out
   * Successfully added a word to the glossary
   * Entered a word already in the glossary
   * Successfully edited their word
   * Successfully deleted their word

### Back to [Contents](#contents)

### [Back to README file](https://github.com/elerel/ms3-kiwi-lingo)