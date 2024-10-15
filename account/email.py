from django.core.mail import send_mail,EmailMultiAlternatives
from .models import *
from django.urls import reverse
from django.conf import settings

def send_email_activation_link(email,email_token):

    subject = "Activation link of Your Account"
    link = reverse("activate-email",kwargs={'email_token':email_token})
    full_link = f"http://13.60.179.53{link}"
    body = f"You need to click on this link to activate your account :\n{full_link}"
    from_email = settings.EMAIL_HOST_USER

    
    send_mail(subject,body,from_email,[email])

def send_password_reset_link(scheme,host,email,email_token):

    subject = "Password Reset link of Your Account"
    link = reverse("password-reset-page",kwargs={'email_token':email_token})

   
    full_link = f"{scheme}://{host}{link}"
    

    body=f"""
    <html>
    <body>
    <div style="display:flex;justify-content:center">

     <table align="center" width="35%" border="0" class="m_6356931864151141868envelope" cellpadding="0" cellspacing="0" style="background-color:#eaeaea" bgcolor="#eaeaea"><tbody><tr><td align="center" style="background-color:#eaeaea;margin-top:0" bgcolor="#eaeaea"><table align="center" border="0" class="m_6356931864151141868content" cellpadding="0" cellspacing="0" style="background-color:#eaeaea;width:500px" width="500" bgcolor="#ffffff"><tbody><tr><td><table class="m_6356931864151141868image" width="100%" cellpadding="0" cellspacing="0"><tbody><tr><td class="m_6356931864151141868cell m_6356931864151141868content-padding" align="center" style="padding-left:40px;padding-right:40px;padding-top:0">
   <tbody>
    <tr>
        <td align="center"><a
                href="https://www.netflix.com/browse?g=78b89ba7-c794-4480-b032-c46b47a7376b&amp;lkid=URL_LOGO&amp;lnktrk=EVO"
                style="color:inherit" target="_blank"
                data-saferedirecturl="https://www.google.com/url?q=https://www.netflix.com/browse?g%3D78b89ba7-c794-4480-b032-c46b47a7376b%26lkid%3DURL_LOGO%26lnktrk%3DEVO&amp;source=gmail&amp;ust=1729061155876000&amp;usg=AOvVaw3iWgqyqymS_z7RNXRFLukv">
                <table class="m_6356931864151141868image" width="100%" cellpadding="0" cellspacing="0">
                    <tbody>
                        <tr>
                            <td class="m_6356931864151141868cell m_6356931864151141868content-padding" align="left"
                                style="padding-left:40px;padding-right:40px;padding-top:20px"><img
                                    src="https://ci3.googleusercontent.com/meips/ADKq_NanW4CgGwRjEPu6W145C0FAUPkNSUfK2Qk70Sk3Zn2ekP6aADG4-gVTyNoqEz-XDsiJ_6ZWMnkWI3bZTOwiLtj2anEZ2dc=s0-d-e1-ft#https://assets.nflxext.com/us/email/gem/nflx.png"
                                    alt="Netflix" width="24" border="0"
                                    style="border:none;outline:none;border-collapse:collapse;display:block;border-style:none"
                                    class="CToWUd" data-bit="iit"></td>
                        </tr>
                    </tbody>
                </table>
            </a>
            <table align="left" width="100%" cellpadding="0" cellspacing="0">
                <tbody>
                    <tr>
                        <td align="left" class="m_6356931864151141868content-padding"
                            style="padding-left:40px;padding-right:40px;font-family:NetflixSans-Bold,Helvetica,Roboto,Segoe UI,sans-serif;font-weight:700;font-size:36px;line-height:43px;letter-spacing:-1px;padding-top:20px;color:#221f1f">
                            Reset your password</td>
                    </tr>
                </tbody>
            </table>
            <table align="left" width="100%" cellpadding="0" cellspacing="0">
                <tbody>
                    <tr>
                        <td align="left" class="m_6356931864151141868content-padding"
                            style="padding-left:40px;padding-right:40px;font-family:NetflixSans-Regular,Helvetica,Roboto,Segoe UI,sans-serif;font-weight:400;font-size:16px;line-height:21px;padding-top:20px;color:#221f1f">
                            Hi, <span style="word-break:break-all"></span></td>
                    </tr>
                </tbody>
            </table>
            <table align="left" width="100%" cellpadding="0" cellspacing="0">
                <tbody>
                    <tr>
                        <td align="left" class="m_6356931864151141868content-padding"
                            style="padding-left:40px;padding-right:40px;font-family:NetflixSans-Regular,Helvetica,Roboto,Segoe UI,sans-serif;font-weight:400;font-size:16px;line-height:21px;padding-top:20px;color:#221f1f">
                            Let's reset your password in 1 minute so you can get back to watching.</td>
                    </tr>
                </tbody>
            </table>
            <table class="m_6356931864151141868single-button m_6356931864151141868mobile-100w" align="center"
                width="100%" cellpadding="0" cellspacing="0">
                <tbody>
                    <tr>
                        <td class="m_6356931864151141868content-padding" align="center"
                            style="padding-left:40px;padding-right:40px;padding-top:20px">
                            <table style="background-color:#e50914;border-radius:4px;width:100%" cellpadding="0"
                                cellspacing="0" width="100%" bgcolor="#e50914">
                                <tbody>
                                    <tr>
                                        <td align="center"
                                            style="font-family:NetflixSans-Bold,Helvetica,Roboto,Segoe UI,sans-serif;font-weight:700;font-size:14px;line-height:17px;letter-spacing:-0.2px;padding-top:20px;padding:14px 40px;color:#ffffff">
                                            <a href="{full_link}"
                                                style="font-family:NetflixSans-Bold,Helvetica,Roboto,Segoe UI,sans-serif;font-weight:700;font-size:14px;line-height:17px;letter-spacing:-0.2px;text-align:center;text-decoration:none;display:block;color:#ffffff"
                                                target="_blank"
                                                data-saferedirecturl="#">Reset
                                                Password</a></td>
                                    </tr>
                                </tbody>
                            </table>
                        </td>
                    </tr>
                </tbody>
            </table>
            <table align="left" width="100%" cellpadding="0" cellspacing="0">
                <tbody>
                    <tr>
                        <td align="left" class="m_6356931864151141868content-padding"
                            style="padding-left:40px;padding-right:40px;font-family:NetflixSans-Regular,Helvetica,Roboto,Segoe UI,sans-serif;font-weight:400;font-size:16px;line-height:21px;padding-top:20px;color:#221f1f">
                            If you did not ask to reset your password, you may want to review your <a
                                href="#"
                                style="color:inherit;text-decoration:underline" target="_blank"
                                data-saferedirecturl="#">recent
                                account access</a> for any unusual activity.</td>
                    </tr>
                </tbody>
            </table>
            <table align="left" width="100%" cellpadding="0" cellspacing="0">
                <tbody>
                    <tr>
                        <td align="left" class="m_6356931864151141868content-padding"
                            style="padding-left:40px;padding-right:40px;font-family:NetflixSans-Regular,Helvetica,Roboto,Segoe UI,sans-serif;font-weight:400;font-size:16px;line-height:21px;padding-top:20px;color:#221f1f">
                            We're here to help if you need it. Visit the <a
                                href="#"
                                style="color:inherit;text-decoration:underline" target="_blank"
                                data-saferedirecturl="#">Help
                                Centre</a> for more info or <a
                                href="https://help.netflix.com/contactus?g=78b89ba7-c794-4480-b032-c46b47a7376b&amp;lkid=URL_CONTACT&amp;lnktrk=EVO"
                                style="color:inherit;text-decoration:underline" target="_blank"
                                data-saferedirecturl="#">contact
                                us</a>.</td>
                    </tr>
                </tbody>
            </table>
            <table align="left" width="100%" cellpadding="0" cellspacing="0">
                <tbody>
                    <tr>
                        <td align="left" class="m_6356931864151141868content-padding"
                            style="padding-left:40px;padding-right:40px;font-size:14px;line-height:17px;letter-spacing:-0.2px;font-family:NetflixSans-Medium,Helvetica,Roboto,Segoe UI,sans-serif;font-weight:700;padding-top:20px;color:#221f1f">
                            By <span class="il">Vatsal Goswami's</span>Netflix-Clone</td>
                    </tr>
                </tbody>
            </table>
            <table width="100%" cellpadding="0" cellspacing="0">
                <tbody>
                    <tr>
                        <td class="m_6356931864151141868content-padding"
                            style="padding-left:40px;padding-right:40px;padding-top:30px">
                            <table align="center" width="100%" cellpadding="0" cellspacing="0">
                                <tbody>
                                    <tr>
                                        <td
                                            style="font-size:0;line-height:0;border-style:solid;border-bottom-width:0;border-color:#221f1f;border-top-width:2px">
                                            &nbsp;</td>
                                    </tr>
                                </tbody>
                            </table>
                        </td>
                    </tr>
                </tbody>
            </table>
        </td>
    </tr>
   </tbody>
    </table>
    </div>
   
    </body>
    </html>

    """
     # Create the email
    from_email = settings.EMAIL_HOST_USER
    email_message = EmailMultiAlternatives(subject, body, from_email, [email])
    email_message.attach_alternative(body, "text/html")  # Attach HTML content

    # Send the email
    email_message.send()

    print(link)

    


   