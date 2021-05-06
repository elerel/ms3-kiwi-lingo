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

![image](https://res.cloudinary.com/elerel/image/upload/v1620229796/jshint_znig9a.png)

EmailJS:

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



### Contact Form


### Error Pages

Should the user accidentally type the wrong address or land on a page not featured in the site, I added a 404.html page so that the user can be redirected to the site. I tested this by typing http://kiwi-lingo.herokuapp.com/bananas and the below appears:

![image](https://res.cloudinary.com/elerel/image/upload/v1620336775/404_fpsae3.png)

For the "Manage Categories" page, the site admin is the only user with access to it. With the use of jinja templating, if the user is not logged in as site admin, the user will be redirected to an "Acess Denied" message:

![image](https://res.cloudinary.com/elerel/image/upload/v1620337940/accessdenied_kzx3rv.png)


Should a user try and force their way in to the site 



### Links and Navigation Testing

To make sure all links within the site functioned, I manually tested each one so that:
-   each link opened up in a separate tab by using the target_blank attribute
-   the link redirected the user to the correct URL
-   each link has a underline text-decoration when hovered over so that the user knows they will be redirected.

In addition to the links functioning correctly, I also manually tested the navigation links in full screen and mobile view modes. This was to ensure that each link was displaying as it should and that the list of items were correctly displayed.

### Testing User Stories



### [Back to README file](https://github.com/elerel/ms3-kiwi-lingo)