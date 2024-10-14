add_btn = document.getElementById('add-profile-btn');
profile_name = document.getElementById('name');

pop_wrapper = document.querySelector('.profile-adder-wrapper');



function add_profile(){
  if(pop_wrapper.style.scale == "1")
  {
    pop_wrapper.style.scale = "0";
    pop_wrapper.style.opacity = "0";
  }
  else{
       pop_wrapper.style.scale = "1";
       pop_wrapper.style.opacity = "100%";

  }
}



add_btn.addEventListener('click',()=>{
      if (profile_name.value == ""){
        }
        else{
          add_profile()
        }
});

function redirectToPage(profile_id) {
  window.location.href = '/account/profile/' + profile_id +'/';
}