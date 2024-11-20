const email = document.getElementById('email-index');
const email_label = document.getElementById('email-label');


window.addEventListener('pageshow',function(event){
    if (event.persisted){

        window.location.reload();
    }
});







if(email != null)
{
    email.addEventListener("focusin",()=>{
    
        email_label.style.top = '-10%';
        email_label.style.fontSize = '0.7rem';
        email_label.style.transform = 'translateX(-5%)';
    
    });
    
    email.addEventListener("focusout",()=>{
    
        if(email.value=="")
        {
            email_label.style.top = '0';
            email_label.style.fontSize = '0.9rem';
            email_label.style.transform = 'translateY(15%)';
        }
        
    
    });
}



// for footer email controlling



const email1 = document.getElementById('email-index1');
const email_label1 = document.getElementById('email-label1');

if(email1 != null)

    {
        email1.addEventListener("focusin",()=>{
    
            email_label1.style.fontSize = '0.7rem';
            email_label1.style.transform = 'translateY(18%)';
        });
        
        email1.addEventListener("focusout",()=>{
        
            if(email1.value=="")
            {
                email_label1.style.top = '0';
                email_label1.style.fontSize = '0.9rem';
                email_label1.style.transform = 'translateY(38%)';
            }
            
        
        });

    }




// For SLider

const movie_poster = document.querySelectorAll('.movie-list-slider  .movie-list');
const movie_slider = document.querySelector('.movie-list-slider');
let count = 0;
const prebtn = document.getElementById('prev');
const nextbtn = document.getElementById('next');



prebtn.addEventListener("click",()=>{
    movie_slider.scrollBy({ left: -200, behavior: 'smooth' });

  
});

nextbtn.addEventListener("click",()=>{
    movie_slider.scrollBy({ left: 200, behavior: 'smooth' }); 
    
});


// FAQ Accordion

let faq = document.querySelectorAll('.faq');

faq.forEach(item=>{

    item.querySelector('.ques').addEventListener("click",()=>{

        if(item.classList.contains('active')){
            item.classList.remove('active');
            item.querySelector('.answer').style.height = "0px";
            item.querySelector('.ques span').style.transform = "rotate(0deg)";
        }
        else{

            faq.forEach(item1=>{
            // item1.querySelector('.answer').style.display = 'none';
            item1.querySelector('.answer').style.height = "0px";
            item1.querySelector('.ques span').style.transform = "rotate(0deg)";
            item1.classList.remove('active');
            });

            item.querySelector('.answer').style.height = `${item.scrollHeight-30}px`;
            item.querySelector('.ques span').style.transform = "rotate(45deg)";
            item.classList.add('active');
        }
    });

});