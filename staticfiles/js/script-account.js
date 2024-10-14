add_btn = document.getElementById('add-profile-btn');
profile_name = document.getElementById('name');
profile_delete = document.getElementById('delete-profile');
profile_delete_confirm = document.querySelector('.delete-confirm')

pop_wrapper = document.querySelector('.profile-adder-wrapper');

detWrapper = document.querySelector('.det-wrapper')
footer = document.querySelector('footer')
header = document.querySelector('header')
html = document.querySelector('html')




function add_profile(){
  if(pop_wrapper.style.scale == "0.7")
  {
    pop_wrapper.style.scale = "0";
    pop_wrapper.style.opacity = "0";
    detWrapper.style.pointerEvents = "all";
    footer.style.pointerEvents = "all";
    header.style.pointerEvents = "all";
    html.style.overflowY = "auto";
  }
  else{
       pop_wrapper.style.scale = "0.7";
       pop_wrapper.style.opacity = "100%";
       detWrapper.style.pointerEvents = "none";
       footer.style.pointerEvents = "none";
       header.style.pointerEvents = "none";
       html.style.overflowY = "hidden";

  }
}

function delete_profile()
{
  profile_delete_confirm.classList.toggle('show');
  if(profile_delete_confirm.classList.contains('show'))
  {
    detWrapper.style.pointerEvents = "none";
       footer.style.pointerEvents = "none";
       header.style.pointerEvents = "none";
       html.style.overflowY = "hidden";
  }
  else{
    detWrapper.style.pointerEvents = "all";
    footer.style.pointerEvents = "all";
    header.style.pointerEvents = "all";
    html.style.overflowY = "auto";
  }
  
}



// add_btn.addEventListener('click',()=>{
//       if (profile_name.value == ""){
//         }
//         else{
//           add_profile()
//         }
// });