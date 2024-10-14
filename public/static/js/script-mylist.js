const main_tag_list = document.querySelector('main');

window.addEventListener("scroll",()=>{
    menu_wrapper.classList.remove('open_menu');
      const header = document.querySelector('header')
      if(window.innerWidth > 500)
      {
        header.classList.toggle('active',window.scrollY>0);
      }
      
  })
  
  
// My List in Pop Window

const listWrapper = document.querySelector('.list-wrapper');
const lists = document.querySelectorAll('.list');

lists.forEach(list => {
  list.addEventListener("click", () => {

    OpenPopWindow(list);
    listWrapper.style.pointerEvents = 'none';

  })
})

// 

// pop Closes onclicking main_tag while popwindow is Opened  
main_tag_list.addEventListener("click", () => {
  
  if (pop_movie.classList.contains('active')) {
    closePopWindow();
  }
  listWrapper.style.pointerEvents = 'all';
})
