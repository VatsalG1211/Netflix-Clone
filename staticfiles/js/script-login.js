const email = document.getElementById('email');
const password = document.getElementById('password');

const label_email =document.getElementById('placehol-email');
const label_pass =document.getElementById('placehol-pass');

window.addEventListener('pageshow',function(event){
    if (event.persisted){

        window.location.reload();
    }
});



window.addEventListener('pagehide', function(event) {
    var content = document.querySelector('body');
    content.style.transform = 'translateX(60%)' // Start the fade-out effect
  });









email.addEventListener("focusin",()=>{

    
        label_email.style.fontSize = '0.75rem';
        label_email.style.right = '-12px';
        label_email.style.top = '-50px';
        
  
});

email.addEventListener("focusout",()=>{

    if(email.value==""){
        label_email.style.fontSize = '1rem';
        label_email.style.right = '-10px';
        label_email.style.top = '-37px';

    }
});


password.addEventListener("focusin",()=>{

   
        label_pass.style.fontSize = '0.75rem';
        label_pass.style.right = '-12px';
        label_pass.style.top = '-50px';
        
    
});

password.addEventListener("focusout",()=>{

    if(password.value==""){
        label_pass.style.fontSize = '1rem';
        label_pass.style.right = '-10px';
        label_pass.style.top = '-37px';


    }
})