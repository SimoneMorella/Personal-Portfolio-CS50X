# Personal-Portfolio-CS50X
#### Video Demo:  <URL https://youtu.be/G977rcyWHM4?si=ds5hktl6T_pSyeZl>
#### Description:
Hi, this project contains my personal portfolio. I especially focused on the Front-end of the webpage. Inserting animations, fading, scroll behaviors, responsive buttons, etc.
This webpage is also completely responsive. I created in the css file different behaviors that the page must have when it is shrinked or when it is opened by a smartphone or tablets. Especially, when it is opened on a display way smaller than a laptop the header changes showing a burger menu that has to be clicked to open the different links to other parts of the portfolio.
As I said before, the website is fully responsive: not only the text and buttons are fully functional in different resolutions but also the animations.
In the html file you can see the structure of what the portfolio contains. It is a single html file that contains different sections. Each section cover perfectly the window size on any mointor as the height has been set through the css style file to 100vh. Also here I linked all the buttons, especially the social media one, to my real social media!
In the style.css file it is possible to check the style decisions made for the portfolio. For the 4 colors that I used I scanned my photo on the home page of the Portfolio with an AI scanner that gave me the right palette of colours based on the image. in the CSS file there are also all the animation that you can see on the project. Mostly of them were done through the ::before feature given by css. Also, in this file there is the @media part on the end that manage all the responsivness of the website. To get the correct data for each display ChatGPT was extremely helpful.
In the Script.js file there is not much information. I mainly used it to manage the scroll behaviors of the portfolio and to manage the change of the section classes to highlight them during their display on the screen.
Finally, in the app.py there is a Flask script that was only needed to associate the Contact Me form with an actual email to receive messages from the form. This is the only backend functionality that I included as at the start I didn't thought that I needed Flask to actually create this function! In the end of the front-end part I thought that linking the form to an actual email would have been easier and could have be done with JS. But through some research I understood that my options were PHP and Flask. I choose the second one as we used it during the week 9 exercises and it was much more familiar to me than PHP. 
I used the smtplib library, with Mailtrap (later i discovered that I could have used Flask-mail) because Gmail was blocked for third part use, and I managed to get my contact form to send me actual email!!

Thanks again for this amazing course I learnt a lot!

Simone Morella
